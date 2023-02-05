# module specific business logic (will be use for endpoints)
from ..load_models import german_nlp

class NER:

    def __init__(self, text):
        self._input = text

    def predict_entities(self):
        try:
            doc = german_nlp(self._input)
            entities = [(ent.text, ent.label_) for ent in doc.ents]

            return entities, 0, None

        except BaseException as e:
            message = f'error while predicting entities : {e}'
            print(message)

            return '', 1, message