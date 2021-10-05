from os import environ
from google.cloud import translate


class Translation:
    def __init__(self) -> None:
        project_id = environ.get("PROJECT_ID", "")
        assert project_id
        self.parent = f"projects/{project_id}"
        self.client = translate.TranslationServiceClient()
        self.target_language_code = "pt"

    def translation_name(self, first_base, second_base):
        response = self.client.translate_text(
            contents=[first_base.name],
            target_language_code=self.target_language_code,
            parent=self.parent,
        )
        if second_base.name in response.translations:
            first_base.match_name.append(
                second_base.name)

    def translation_parameter(self, first_base, second_base):
        for first_parameter in first_base.parameters:
            response = self.client.translate_text(
                contents=[first_base.name],
                target_language_code=self.target_language_code,
                parent=self.parent,
            )
            for second_parameter in second_base.parameters:
                if second_parameter['parameter'] in response.translations \
                        and first_parameter['parameter'] != 'id':
                    first_base.match_parameters.append({
                        'name': second_base.name,
                        'parameter': second_parameter,
                        'my_parameter': first_parameter
                    })
