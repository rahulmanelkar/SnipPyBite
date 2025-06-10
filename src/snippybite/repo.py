from abc import ABC, abstractmethod

from models import Snippet
from sqlmodel import Session, select


class SnippetRepository(ABC):
    @abstractmethod
    def add(self, snippet: Snippet) -> None:
        pass

    @abstractmethod
    def list(self) -> list[Snippet]:
        pass

    @abstractmethod
    def get(self, snippet_id: int) -> Snippet | None:
        pass

    @abstractmethod
    def delete(self, snippet_id: int) -> None:
        pass


class InMemorySnippetRepo(SnippetRepository):
    def __init__(self):
        self._snippets: dict[int, Snippet] = {}
        self._next_id: int = 1

    def add(self, snippet: Snippet) -> None:
        if snippet.id is None:
            snippet.id = self._next_id
            self._next_id += 1
        self._snippets[snippet.id] = snippet

    def list(self) -> list[Snippet]:
        return list(self._snippets.values())

    def get(self, snippet_id: int) -> Snippet | None:
        return self._snippets.get(snippet_id)

    def delete(self, snippet_id: int) -> None:
        if snippet_id in self._snippets:
            del self._snippets[snippet_id]


class SQLSnippetRepo(SnippetRepository):
    def __init__(self, engine):
        self.engine = engine

    def add(self, snippet: Snippet) -> None:
        with Session(self.engine) as session:
            session.add(snippet)
            session.commit()

    def list(self) -> list[Snippet]:
        with Session(self.engine) as session:
            return session.exec(select(Snippet)).all()

    def get(self, snippet_id: int) -> Snippet | None:
        with Session(self.engine) as session:
            return session.get(Snippet, snippet_id)

    def delete(self, snippet_id: int) -> None:
        with Session(self.engine) as session:
            snippet = session.get(Snippet, snippet_id)
            if snippet:
                session.delete(snippet)
                session.commit()
