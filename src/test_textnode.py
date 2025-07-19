import unittest

from textnode import TextNode, TextType


class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node, node2)

    def test_not_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        node.text = "new_val"
        self.assertNotEqual(node, node2)
        
        node.text, node2.text_type = "This is a text node", TextType.PLAIN
        self.assertNotEqual(node, node2)
    
    def test_valid(self):
        node2 = TextNode("Text node", TextType.PLAIN, None)
        self.assertIsNone(node2.url)

if __name__ == "__main__":
    unittest.main()