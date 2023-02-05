# for load machine learning models
import spacy

class Models:
    def __init__(self):
        self.german_nlp = self.load_models()

    def load_models(self):
        german_nlp = spacy.load("de_core_news_md")

        return german_nlp

models = Models()
german_nlp = models.german_nlp