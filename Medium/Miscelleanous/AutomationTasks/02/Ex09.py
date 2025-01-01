# 09. Automate Text Translation
from googletrans import Translator


def translate_text(text, dest_lang):
    translator = Translator()
    return translator.translate(text, dest=dest_lang).text
