# api-ner-german
This is a german named entity recognition model that using spacy pretrained model.

To run this api using docker:
```
docker-compose up --build
```

To run this api natively:
```
cd app/
uvicorn main:app --host 0.0.0.0 --port 3345
```
