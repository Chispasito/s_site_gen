import unittest

from htmlnode import HTMLNode, LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_instance(self):
        node = HTMLNode()
        self.assertIsInstance(node, HTMLNode)
    
    def test_prop(self):
        node = HTMLNode("tag", "val", [], {"1": "a", "2":"b"})
        self.assertEqual(node.props_to_html(), " 1=\"a\" 2=\"b\"")
    
    def test_defaults(self):
        node = HTMLNode()
        self.assertIsNone(node.tag)
        self.assertIsNone(node.value)
        self.assertIsNone(node.children)
        self.assertIsNone(node.props)

class TestLeafNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node3 = LeafNode("p", "Hello, world!", {})
        self.assertEqual(node3.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("b", "Hello, world!", props={"href": "https://link", "color": "red"})
        self.assertEqual(node2.to_html(), "<b href=\"https://link\" color=\"red\">Hello, world!</b>")
    
    def test_value_error(self):
        node4 = LeafNode("x", value = None)
        
        with self.assertRaises(ValueError):
            print(node4.to_html())

if __name__ == "__main__":
    unittest.main()