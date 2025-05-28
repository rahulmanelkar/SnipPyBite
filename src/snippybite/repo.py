from abc import ABC, abstractmethod

from models import Snippet


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

    def add(self, snippet: Snippet) -> None:
        self._snippets[snippet.id] = snippet

    def list(self) -> list[Snippet]:
        return list(self._snippets.values())

    def get(self, snippet_id: int) -> Snippet | None:
        return self._snippets.get(snippet_id)

    def delete(self, snippet_id: int) -> None:
        if snippet_id in self._snippets:
            del self._snippets[snippet_id]
