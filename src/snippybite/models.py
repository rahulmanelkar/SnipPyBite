from sqlmodel import Field, SQLModel, create_engine


class Snippet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    code: str
    description: str


if __name__ == "__main__":
    engine = create_engine("sqlite:///snippets.db")
    SQLModel.metadata.create_all(engine)
    print("Database+table created")
