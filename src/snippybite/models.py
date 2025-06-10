from sqlmodel import Field, SQLModel, create_engine


class Snippet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    code: str
    description: str


def createmodels():
    engine = create_engine("sqlite:///snippets.db")
    SQLModel.metadata.create_all(engine)
    return engine


if __name__ == "__main__":
    createmodels()
