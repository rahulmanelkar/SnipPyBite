import typer
from rich import print

app = typer.Typer(name="Snippet")


@app.command()
def userinput(inputstr: str):
    print(f"You've entered {inputstr}")


@app.command()
def test():
    print("test snippet")


if __name__ == "__main__":
    app()
