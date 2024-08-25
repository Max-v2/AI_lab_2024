# scripts/data_processing.py
import spacy

nlp = spacy.load("en_core_web_sm")

def process_text(text):
    doc = nlp(text)
    for token in doc:
        print(token.text, token.lemma_, token.pos_, token.dep_)

# Example usage
text = "This is a sample text for processing."
process_text(text)