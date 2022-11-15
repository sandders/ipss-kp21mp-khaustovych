import unittest, tempfile, shutil
from os import path
from indexes import InvertedIndex, ForwardIndex


class TestIndexes(unittest.TestCase):

    def setUp(self):
        # Create a temporary directory
        self.test_dir = tempfile.mkdtemp()
        self.file_pass_1 = path.join(self.test_dir, 'test1.txt')
        self.file_pass_2 = path.join(self.test_dir, 'test2.txt')
        with open(self.file_pass_1, "w") as file:
            file.write("Woops! I have deleted all content")
        with open(self.file_pass_2, "w") as file:
            file.write("The content was deleted")

    def tearDown(self):
        # Remove the directory after the test
        if path.exists(self.test_dir):
            shutil.rmtree(self.test_dir)

    def index_search(self, index):
        index.build_index()
        assert index.search('all') == [self.file_pass_1]
        assert index.search('was') == [self.file_pass_2]
        assert set(index.search('content')) == {self.file_pass_1, self.file_pass_2}

    def test_inverted_index(self):
        index = InvertedIndex(self.test_dir)
        self.index_search(index)

    def test_forvard_index(self):
        index = ForwardIndex(self.test_dir)
        self.index_search(index)

    def index_search_bad_directory(self, index):
        shutil.rmtree(self.test_dir)
        index.build_index()
        assert index.search('all') == []
        assert index.search('was') == []
        assert index.search('content') == []

    def test_inverted_index_bad_directory(self):
        index = InvertedIndex(self.test_dir)
        self.index_search_bad_directory(index)

    def test_forvard_index_bad_directory(self):
        index = ForwardIndex(self.test_dir)
        self.index_search_bad_directory(index)
