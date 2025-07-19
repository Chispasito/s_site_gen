import unittest

from htmlnode import HTMLNode


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

if __name__ == "__main__":
    unittest.main()