from sqlmodel import create_engine

from .repo import SQLSnippetRepo

DATABASE_URL = "sqlite:///snippets.db"
engine = create_engine(DATABASE_URL)


def get_repo():
    return SQLSnippetRepo(engine)
