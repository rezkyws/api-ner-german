# for pydantic model
from pydantic import BaseModel


class Doc(BaseModel):
    text: str