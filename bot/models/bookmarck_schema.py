from bson import json_util
from bson.objectid import ObjectId
from pydantic import BaseModel, AnyUrl, Field


class Bookmark(BaseModel):
    link: AnyUrl
    description: str
    

class BookmarkWithId(Bookmark):
    id: ObjectId = Field(alias='_id')

    class Config:
        arbitrary_types_allowed = True
        json_dumps = json_util.dumps
        json_loads = json_util.loads
