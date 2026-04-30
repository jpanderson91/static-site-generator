import unittest
from textnode import BlockType
from block_to_block_type import block_to_block_type


class TestBlockToBlockType(unittest.TestCase):
    # Heading
    def test_heading_h1(self):
        self.assertEqual(block_to_block_type("# h1"), BlockType.HEADING)

    def test_heading_h2(self):
        self.assertEqual(block_to_block_type("## h2"), BlockType.HEADING)

    def test_heading_h3(self):
        self.assertEqual(block_to_block_type("### h3"), BlockType.HEADING)

    def test_heading_h4(self):
        self.assertEqual(block_to_block_type("#### h4"), BlockType.HEADING)

    def test_heading_h5(self):
        self.assertEqual(block_to_block_type("##### h5"), BlockType.HEADING)

    def test_heading_h6(self):
        self.assertEqual(block_to_block_type("###### h6"), BlockType.HEADING)

    def test_heading_7_hashes_is_paragraph(self):
        self.assertEqual(block_to_block_type("####### too many"), BlockType.PARAGRAPH)

    def test_heading_no_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("#no space"), BlockType.PARAGRAPH)

    # Code
    def test_code_block(self):
        self.assertEqual(block_to_block_type("```\nprint('hi')\n```"), BlockType.CODE)

    def test_code_single_line_is_paragraph(self):
        self.assertEqual(block_to_block_type("```"), BlockType.PARAGRAPH)

    # Quote
    def test_quote_single_line(self):
        self.assertEqual(block_to_block_type(">quote"), BlockType.QUOTE)

    def test_quote_multiple_lines(self):
        self.assertEqual(block_to_block_type(">line1\n>line2\n>line3"), BlockType.QUOTE)

    def test_quote_missing_prefix_is_paragraph(self):
        self.assertEqual(block_to_block_type(">line1\nline2\n>line3"), BlockType.PARAGRAPH)

    # Unordered list
    def test_unordered_list(self):
        self.assertEqual(block_to_block_type("- one\n- two\n- three"), BlockType.UNORDERED_LIST)

    def test_unordered_list_no_space_is_paragraph(self):
        self.assertEqual(block_to_block_type("-no space"), BlockType.PARAGRAPH)

    def test_unordered_list_mixed_markers_is_paragraph(self):
        self.assertEqual(block_to_block_type("- one\n* two"), BlockType.PARAGRAPH)

    # Ordered list
    def test_ordered_list(self):
        self.assertEqual(block_to_block_type("1. first\n2. second\n3. third"), BlockType.ORDERED_LIST)

    def test_ordered_list_starts_at_2_is_paragraph(self):
        self.assertEqual(block_to_block_type("2. first\n3. second"), BlockType.PARAGRAPH)

    def test_ordered_list_skips_number_is_paragraph(self):
        self.assertEqual(block_to_block_type("1. first\n2. second\n4. fourth"), BlockType.PARAGRAPH)

    # Paragraph
    def test_paragraph(self):
        self.assertEqual(block_to_block_type("just some plain text"), BlockType.PARAGRAPH)


if __name__ == "__main__":
    unittest.main()
