import unittest
from textnode import TextNode, TextType
from htmlnode import *


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

class TestParentNode(unittest.TestCase):
    def test_parent_to_html(self):
        node = ParentNode(
            "p",
            [
                LeafNode("b", "Bold text"),
                LeafNode(None, "Normal text"),
                LeafNode("i", "italic text"),
                LeafNode(None, "Normal text"),
            ],
        ) 
        self.assertEqual(node.to_html(),"<p><b>Bold text</b>Normal text<i>italic text</i>Normal text</p>")
        node.children[1] = ParentNode("x", [LeafNode("z", "PL")])
        self.assertEqual(node.to_html(), "<p><b>Bold text</b><x><z>PL</z></x><i>italic text</i>Normal text</p>")

        node.children = None
        with self.assertRaises(ValueError):
            print(node.to_html())

class TestTextToHTML(unittest.TestCase):
    def test_func(self):
        #text = TextNode("string", "string", None)
        
        # print(text_node_to_html_node(text))
        pass

    def test_text(self):
        node = TextNode("This is a text node", TextType.TEXT)
        html_node = text_node_to_html_node(node)
        self.assertEqual(html_node.tag, "p")
        self.assertEqual(html_node.value, "This is a text node")
        # print(html_node.to_html())

        node2 = TextNode("This is a text node", TextType.IMAGE, "http://url")
        html_node2 = text_node_to_html_node(node2)
        # print(html_node2.to_html())

if __name__ == "__main__":
    unittest.main()