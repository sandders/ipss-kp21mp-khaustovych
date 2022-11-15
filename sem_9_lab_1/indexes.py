from abc import ABC, abstractmethod
from os import walk, path


class Index(ABC):
    def __init__(self, directory='sem_9_lab_1/files'):
        self.index = dict()
        self.directory = directory

    @staticmethod
    def get_words(file_pass):
        word_set = set()
        with open(file_pass, "r") as file:
            for line in file:
                word_set.update(line.split())
        return word_set

    def get_file_passes(self):
        file_passes = []
        for dirpath, _, filenames in walk(self.directory):
            file_passes.extend(path.join(dirpath, filename) for filename in filenames)
        return file_passes

    @abstractmethod
    def build_index(self):
        pass

    @abstractmethod
    def search(self, search_word):
        pass


class InvertedIndex(Index):

    def build_index(self):
        self.index = dict()
        file_passes = self.get_file_passes()
        for file_pass in file_passes:
            words = self.get_words(file_pass)
            for word in words:
                if self.index.get(word):
                    self.index[word].append(file_pass)
                else:
                    self.index[word] = [file_pass]

    def search(self, search_word):
        if self.index.get(search_word):
            return self.index[search_word]
        else:
            return []


class ForwardIndex(Index):

    def build_index(self):
        self.index = dict()
        file_passes = self.get_file_passes()
        for file_pass in file_passes:
            self.index[file_pass] = self.get_words(file_pass)

    def search(self, search_word):
        file_passes_containing_search_word = []
        for file_path, word_set in self.index.items():
            if search_word in word_set:
                file_passes_containing_search_word.append(file_path)
        return file_passes_containing_search_word
