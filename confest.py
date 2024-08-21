import pytest
from collector import TestBooksCollector
@pytest.fixture
def collector():
    return BooksCollector()