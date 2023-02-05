# api-ner-german
This is an example for boilerplate api ml model which is named entity recognition model using pretrained model from spacy for german.

To run this api using docker:
```
docker-compose up --build
```

To run this api natively:
```
cd app/
uvicorn main:app --host 0.0.0.0 --port 3345
```
