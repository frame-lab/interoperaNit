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
                contents=[base.name],
                target_language_code=self.target_language_code,
                parent=self.parent,
            )
            for base_candidate_parameter in base_candidate.parameters:
                match_parameter = {
                    'name': base_candidate.name,
                    'matched_parameter': base_candidate_parameter,
                    'my_parameter': base_parameter
                }

                if base_candidate_parameter['parameter'] in response.translations \
                        and base_parameter['parameter'] != 'id' and \
                        match_parameter not in base.match_parameters:
                    base.match_parameters.append(match_parameter)
