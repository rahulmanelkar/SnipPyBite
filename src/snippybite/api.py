from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import SQLModel

from .db import engine, get_repo
from .models import Snippet
from .repo import SQLSnippetRepo
from .schemas import SnippetCreate, SnippetRead

app = FastAPI()


@app.get("/")
def root():
    return {"message": "Snipster API is alive"}


@app.on_event("startup")
def on_startup():
    SQLModel.metadata.create_all(engine)


@app.post("/snippets/", response_model=SnippetRead, status_code=201)
def create_snippet(snippet_in: SnippetCreate, repo: SQLSnippetRepo = Depends(get_repo)):
    snippet = Snippet(**snippet_in.model_dump())
    repo.add(snippet)
    return repo.add(snippet)


@app.get("/snippets/", response_model=list[SnippetRead])
def list_snippets(repo: SQLSnippetRepo = Depends(get_repo)):
    return repo.list()


@app.get("/snippets/{snippet_id}", response_model=SnippetRead)
def get_snippet(snippet_id: int, repo: SQLSnippetRepo = Depends(get_repo)):
    snippet = repo.get(snippet_id)
    if not snippet:
        raise HTTPException(status_code=404, detail="Snippet not found")
    return snippet
