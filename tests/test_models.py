import pytest
from sqlmodel import Session, SQLModel, create_engine

from src.snippybite.models import Snippet

engine = create_engine("sqlite:///:memory:", echo=True)


@pytest.fixture(scope="module", autouse=True)
def setup_database():
    SQLModel.metadata.create_all(engine)


def test_create_snippet():
    snippet = Snippet(
        title="Test Snippet",
        code="print('Hello Pybites')",
        description="basic snippet for testing",
    )

    with Session(engine) as session:
        session.add(snippet)
        session.commit()
        session.refresh(snippet)

    assert snippet.id is not None
    assert snippet.title == "Test Snippet"
    assert snippet.code == "print('Hello Pybites')"
    assert snippet.description == "basic snippet for testing"
