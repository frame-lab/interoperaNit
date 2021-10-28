from os import environ
from google.cloud import translate


class Translation:
    def __init__(self) -> None:
        project_id = environ.get("PROJECT_ID", "")
        assert project_id
        self.parent = f"projects/{project_id}"
        self.client = translate.TranslationServiceClient()
        self.target_language_code = "pt"

    def translation_name(self, base, base_candidate):
        response = self.client.translate_text(
            contents=[base.name],
            target_language_code=self.target_language_code,
            parent=self.parent,
        )
        if base_candidate.name in response.translations and \
                base_candidate.name not in base.match_name:
            base.match_name.append(
                base_candidate.name)

    def translation_parameter(self, base, base_candidate):
        for base_parameter in base.parameters:
            response = self.client.translate_text(
                contents=[base_parameter['parameter'][0]],
                target_language_code=self.target_language_code,
                parent=self.parent,
            )
            for base_candidate_parameter in base_candidate.parameters:
                match_parameter = {
                    'name': base_candidate.name,
                    'matched_parameter': base_candidate_parameter,
                    'my_parameter': base_parameter
                }

                if base_candidate_parameter['parameter'][0] in response.translations \
                        and base_parameter['parameter'][0] != 'id' and \
                        match_parameter not in base.match_parameters:
                    base.match_parameters.append(match_parameter)

    def translation_entity(self, base, matched_base):
        match_params = [parameter for parameter in base.match_parameters
                        if parameter['name'] == matched_base.name]

        base_param_indexes = []
        matched_param_indexes = []

        for match_param in match_params:
            base_parameter = match_param["my_parameter"]
            matched_base_parameter = match_param["matched_parameter"]

            base_param_indexes.append(
                base.parameters.index(base_parameter))
            matched_param_indexes.append(
                matched_base.parameters.index(matched_base_parameter))

        for base_index in range(0, len(base.entities)):
            for matched_base_index in range(0, len(matched_base.entities)):
                is_match = True
                for param_index in range(0, len(base_param_indexes)):
                    response = self.client.translate_text(
                        contents=[base.entities[base_index][base_param_indexes[param_index]]],
                        target_language_code=self.target_language_code,
                        parent=self.parent,
                    )
                    if matched_base.entities[matched_base_index][matched_param_indexes[param_index]] not in response.translations:
                        is_match = False

                if is_match:
                    base.match_entities.append({
                        'matched_name': matched_base.name,
                        'matched_parameter_index': matched_base_index,
                        'my_parameter_index': base_index,
                        'my_name': base.name
                    })
