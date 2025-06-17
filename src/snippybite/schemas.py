from pydantic import BaseModel


class SnippetBase(BaseModel):
    title: str
    code: str
    description: str


class SnippetCreate(SnippetBase):
    pass


class SnippetRead(SnippetBase):
    id: int
