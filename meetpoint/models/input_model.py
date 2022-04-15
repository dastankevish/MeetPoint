from fastapi import Form
from fastapi import File, UploadFile
from pydantic import BaseModel


#For forms
class InputFile(BaseModel):
    name: str
    content: bytes
    
    @classmethod
    async def as_file(
        cls,
        file: UploadFile = File(...)
    ):
        return cls(
            name=file.filename,
            content=await file.read()
        )
