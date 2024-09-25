from translation_module.translation import translate
from translation_module.synonyms import get_synonyms

def translate_with_synonyms(word, source_lang, target_lang):
    translation = translate(word, source_lang, target_lang)
    synonyms = get_synonyms(word)
    return translation, synonyms[:4]  # Limit to 4 synonyms

def user_translation_choice():
    print("Welcome to the Translation & Synonyms Generator!")

    # Get source and target languages from user input
    source_lang = input("Enter the source language code (e.g., 'en' for English, 'es' for Spanish): ").strip()
    target_lang = input("Enter the target language code (e.g., 'es' for Spanish, 'fr' for French): ").strip()

    # Choose to translate a single word or a long text
    translation_type = input("Do you want to translate a 'word' or 'text'? (Type 'word' or 'text'): ").strip().lower()

    if translation_type == 'word':
        word = input("Enter the word to translate: ").strip()
        translation, synonyms = translate_with_synonyms(word, source_lang, target_lang)
        print(f"\nTranslation of '{word}' from {source_lang} to {target_lang}: {translation}")
        print(f"Synonyms in source language: {synonyms}")
    
    elif translation_type == 'text':
        text = input("Enter the text to translate: ").strip()
        translated_text = translate(text, source_lang, target_lang)
        print(f"\nTranslation from {source_lang} to {target_lang}: {translated_text}")
    
    else:
        print("Invalid choice. Please type 'word' or 'text'.")

if __name__ == "__main__":
    user_translation_choice()
