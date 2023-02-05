# api core module for all endpoints
from fastapi import APIRouter, HTTPException
from .schemas.doc import Doc
from .endpoints.entities import Entities


router = APIRouter(
    prefix='/api/v1',
    # tags=['ner', 'statements', 'topics'],
    responses = {
        404: {'description': 'Not Found'}
    }
)

@router.post('/entities', tags=["ner"])
async def german_ner(doc: Doc):
    entities = Entities(doc.text)
    result = entities.get_entities()

    return result