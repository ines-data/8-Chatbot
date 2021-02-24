import googletrans
from googletrans import Translator

def translate_input(txt):
    translator = Translator()
    translation = translator.translate(txt, dest='en')
    print(translation.text)
    return translation.text


def language_detection(txt) :
    translator = Translator()
    return translator.detect(txt).lang
    

def convert_to_detected_language(txt,lang):
    translator = Translator()
    translation = translator.translate(txt, dest=str(lang))
    #print('traducton =',translation.text  ) 
    return translation.text
