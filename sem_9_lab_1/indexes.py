from abc import ABC, abstractmethod

class Index(ABC):
    def __init__(self, directory='lab1/files'):
        raise NotImplementedError()

    @staticmethod
    def get_words(file_pass):
        raise NotImplementedError()

    def get_file_passes(self):
        raise NotImplementedError()

    @abstractmethod
    def build_index(self):
        pass

    @abstractmethod
    def search(self, search_word):
        pass


class InvertedIndex(Index):

    def build_index(self):
        raise NotImplementedError()

    def search(self, search_word):
        raise NotImplementedError()


class ForwardIndex(Index):

    def build_index(self):
        raise NotImplementedError()

    def search(self, search_word):
        raise NotImplementedError()
