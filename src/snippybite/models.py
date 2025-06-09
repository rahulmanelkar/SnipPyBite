from sqlmodel import Field, SQLModel, create_engine


class Snippet(SQLModel, table=True):
    id: int | None = Field(default=None, primary_key=True)
    title: str
    code: str
    description: str


def main():
    engine = create_engine("sqlite:///snippets.db")
    SQLModel.metadata.create_all(engine)
    print("Database+table created")


if __name__ == "__main__":
    main()
