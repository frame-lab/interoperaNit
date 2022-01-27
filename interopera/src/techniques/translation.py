from os import environ
from google.cloud import translate


class Translation:
    def __init__(self) -> None:
        project_id = environ.get("PROJECT_ID", "")
        assert project_id
        self.parent = f"projects/{project_id}"
        self.client = translate.TranslationServiceClient()
        self.target_language_code = "pt"

    def translation_name(self, base_name, base_candidate_name):
        response = self.client.translate_text(
            contents=[base_name],
            target_language_code=self.target_language_code,
            parent=self.parent,
        )
        return base_candidate_name in response.translations

    def translation_parameter(self, base_parameter, base_candidate_parameter):
        response = self.client.translate_text(
            contents=[base_parameter],
            target_language_code=self.target_language_code,
            parent=self.parent,
        )
        return base_candidate_parameter in response.translations \


    def translation_entity(self, base_entity, matched_base_entity):
        response = self.client.translate_text(
            contents=[base_entity],
            target_language_code=self.target_language_code,
            parent=self.parent,
        )
        return matched_base_entity not in response.translations
