import typer
from rich import print

from .models import Snippet, createmodels
from .repo import SQLSnippetRepo

engine = createmodels()

app = typer.Typer(name="Snippet")

repo = SQLSnippetRepo(engine)


@app.command(name="add")
def add(title: str, code: str, description: str):
    snippet = Snippet(id=None, title=title, code=code, description=description)
    repo.add(snippet)


@app.command(name="list")
def list():
    snippets = repo.list()
    if not snippets:
        print("No snippets found")
    for snip in snippets:
        print(snip)


@app.command()
def get(snippet_id: int):
    snippet = repo.get(snippet_id)
    if snippet:
        print(f"found snippet: {snippet}")
    else:
        print(f"Not found snippet with id {snippet_id}")


@app.command()
def delete(snippet_id: int):
    if repo.get(snippet_id):
        repo.delete(snippet_id)
        print(f"Deleted {snippet_id}")
    else:
        print(f"Snipped ID {snippet_id} not found")


if __name__ == "__main__":
    app()
