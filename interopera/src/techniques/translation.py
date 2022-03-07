from os import environ
from google.cloud import translate


class Translation:
    def __init__(self) -> None:
        project_id = environ.get("PROJECT_ID", "")
        self.parent = f"projects/{project_id}"
        self.client = translate.TranslationServiceClient()
        self.target_language_code = "pt"

    def translate(self, data):
        return self.client.translate_text(request=data)

    def translation_comparison(self, first_sequence, second_sequence, type='in'):
        data = {
            'contents': [first_sequence],
            'target_language_code': self.target_language_code,
            'parent': self.parent
        }
        response = self.translate(data)
        if type == 'in':
            return second_sequence in response.translations
        if type == 'not':
            return second_sequence not in response.translations

    def translation_word(self, text, target="pt"):
        data = {
            'contents': [text],
            'target_language_code': target,
            'parent': self.parent
        }
        response = self.translate(data)
        return response.translations[0]
