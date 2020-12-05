from . import readchunks, SeatReader
from unittest import TestCase

class TestReadChunks(TestCase):

    def test_works(self):
        for text in [
            'a\n\nb\nc\n\nd\n',
            'a\n\nb\nc\n\nd',
            'a\n\nb\nc\n\n\nd\n', # Allow redundant blanks.
            'a\n\nb\nc\n\n\nd',
            'a\n\nb\nc\n\nd\n\n',
        ]:
            self.assertEqual([
                ['a'],
                ['b', 'c'],
                ['d'],
            ], list(readchunks(text.splitlines(True))))

    def test_empty(self):
        for text in [
            '',
            '\n',
            '\n\n',
        ]:
            self.assertEqual([], list(readchunks(text.splitlines(True))))

class TestSeatReader(TestCase):

    def test_range(self):
        self.assertEqual(range(1024), SeatReader(10).range())
        self.assertEqual(range(8), SeatReader(3).range())
        self.assertEqual(range(4), SeatReader(2).range())
        self.assertEqual(range(2), SeatReader(1).range())
