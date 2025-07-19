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

# Add some test cases by adding methods to the TestTextNode class to verify that the TextNode class works as expected. 
# You can use the following methods to compare the objects:
# self.assertEqual - if the inputs are equal the test passes
# self.assertNotEqual - if the inputs are not equal the test passes
# 
# Add even more test cases (at least 3 in total) to check various edge cases, 
# like when the url property is None, or when the text_type property is different. 
# You'll want to make sure that when properties are different, the TextNode objects are not equal.