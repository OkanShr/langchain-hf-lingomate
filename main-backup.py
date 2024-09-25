from transformers import pipeline, AutoTokenizer, AutoModelForCausalLM
import os

os.environ["HF_HUB_DISABLE_SYMLINKS_WARNING"] = "1"

# Initialize te translation pipeline
translator = pipeline('translation_en_to_de', model="Helsinki-NLP/opus-mt-en-de")

synonym_model_name = "EleutherAI/gpt-j-6B"
tokenizer = AutoTokenizer.from_pretrained(synonym_model_name)
model = AutoModelForCausalLM.from_pretrained(synonym_model_name)
synonym_generator = pipeline("text-generation", model=model, tokenizer=tokenizer, max_length=50)

# Define the translation function
def huggingface_translate(word):
    try:
        translation = translator(word)[0]['translation_text']
    except Exception as e:
        print(f"Error during translation: {e}")
        return None
    return translation

def generate_synonyms(translation):
    try:
        prompt_text = f"Generate 4 German synonyms for the word: {translation}."
        response = synonym_generator(prompt_text)[0]['generated_text']
        synonyms = [syn.strip() for syn in response.split(",")[:4]]  
    except Exception as e:
        print(f"Error during synonym generation: {e}")
        return []
    return synonyms

def translate_and_generate_synonyms(word):
    print(f"Translating '{word}' from English to German...")
    translation = huggingface_translate(word)
    if translation:
        print(f"Translation: {translation}")
        synonyms = generate_synonyms(translation)
        return translation, synonyms
    else:
        return None, []

# Example usage
word = "fine"
translation, synonyms = translate_and_generate_synonyms(word)
print(f"Translation: {translation}")
print(f"Synonyms: {synonyms}")
