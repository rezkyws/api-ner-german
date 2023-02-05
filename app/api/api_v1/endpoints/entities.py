# module of an endpoint
from ...api_v1.services.ner import NER


class Entities:

    def __init__(self, text):
        self._input = text

    def get_entities(self):
        try :
            if len(self._input) == 0:
                message = 'the text cannot be empty'
                print(message)

                return message

            lowered_text = self._input.lower()
            ner = NER(lowered_text)
            raw_result, status, error_msg = ner.predict_entities()
            result = self.formatting_output(raw_result)

            if status:
                response = {
                    "entities": result,
                    "status": status,
                    "error": error_msg
                }
            else:
                response = {
                    "entities": result,
                    "status": status,
                    "error": None
                }

            return response
        
        except BaseException as e:
            error_msg = f'error while getting entities : {e}'
            print(error_msg)
            
            response = {
                    "entities": '',
                    "status": 1,
                    "error": error_msg
                }

            return response

    def formatting_output(self, entities):
        output = {
            "location": [],
            "organization": [],
            "person": {
                "artist": [],
                "all_person": []
            }
        }

        uniq_txt = []
        for txt, label in entities:
            if txt not in uniq_txt:
                uniq_txt.append(txt)
                if label == 'LOC' or label == 'GPE':
                    output['location'].append(txt)
                elif label == 'ORG' or label == 'NORP':
                    output['organization'].append(txt)
                elif label == 'PERSON':
                    output['person']['all_person'].append(txt)

        return output