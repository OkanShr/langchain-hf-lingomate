from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import pipeline
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

translator = pipeline('translation_en_to_de', model="Helsinki-NLP/opus-mt-en-de")

template = """
Translate the following word from English to German: {word}
"""

prompt = PromptTemplate(input_variables=["word"], template=template)

def huggingface_translate(word):
    translation = translator(word)[0]['translation_text']
    return translation

def translate_word(word):
    print(f"Translating '{word}' from English to German...")
    
    result = huggingface_translate(word)
    
    return result

word = "My name is Okan"
translation = translate_word(word)
print(f"Translation: {translation}")
