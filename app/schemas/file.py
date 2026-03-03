from pydantic import BaseModel


class FileMetaResponse(BaseModel):
    file_id: str
    url: str
