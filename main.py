from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from transformers import pipeline
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

translator = pipeline('translation_en_to_de', model="Helsinki-NLP/opus-mt-en-de")

synonym_generator = pipeline('text-generation', model="gpt2", max_length=200)

template = """
Translate the following word from English to German: {word}.
Then, generate 4 possible synonyms for the translated word.
"""



prompt = PromptTemplate(input_variables=["word"], template=template)

def huggingface_translate(word):
    translation = translator(word)[0]['translation_text']
    
    return translation

def generate_synonyms(translation):
    prompt_text = f"""
    2 Synonyms of: {translation}."""
    synonym = synonym_generator(prompt_text)[0]['generated_text']
    return synonym


def translate_and_generate_synonyms(word):
    print(f"Translating '{word}' from English to German...")
    translation = huggingface_translate(word)
    print(f"Translation: {translation}")
    
    synonyms = generate_synonyms(translation)
    return translation, synonyms


word = "fine"
translation, synonyms = translate_and_generate_synonyms(word)
print(f"Translation: {translation}")
print(f"Synonym: {synonyms}")
