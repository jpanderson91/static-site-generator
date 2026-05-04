import unittest
from extract_title import extract_title

class TestExtractTitle(unittest.TestCase):
    def test_simple_title(self):
        self.assertEqual(extract_title("# Hello"), "Hello")

    def test_title_with_extra_whitespace(self):
        self.assertEqual(extract_title("#   Hello World   "), "Hello World")

    def test_title_not_on_first_line(self):
        md = "some text\n\n# My Title\n\nmore text"
        self.assertEqual(extract_title(md), "My Title")

    def test_h2_is_not_h1(self):
        with self.assertRaises(ValueError):
            extract_title("## Not an h1")

    def test_no_title_raises(self):
        with self.assertRaises(ValueError):
            extract_title("just some text\nno heading here")

    def test_empty_string_raises(self):
        with self.assertRaises(ValueError):
            extract_title("")

    def test_hash_only(self):
        self.assertEqual(extract_title("#"), "")

    def test_ignores_h2_returns_h1(self):
        md = "## subtitle\n# Real Title\n### another"
        self.assertEqual(extract_title(md), "Real Title")

if __name__ == "__main__":
    unittest.main()
