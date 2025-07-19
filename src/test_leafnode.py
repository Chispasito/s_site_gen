import unittest

from leafnode import LeafNode


class TestHTMLNode(unittest.TestCase):
    def test_leaf_to_html_p(self):
        node = LeafNode("p", "Hello, world!")
        #print(node.to_html())
        self.assertEqual(node.to_html(), "<p>Hello, world!</p>")

        node3 = LeafNode("p", "Hello, world!", {})
        #print(node3.to_html())
        self.assertEqual(node3.to_html(), "<p>Hello, world!</p>")

        node2 = LeafNode("b", "Hello, world!", props={"href": "https://link", "color": "red"})
        #print(f"html: {node2.to_html()} | props: {node2.props}")
        self.assertEqual(node2.to_html(), "<b href=\"https://link\" color=\"red\">Hello, world!</b>")
    
    def test_value_error(self):
        node4 = LeafNode("x", value = None)
        
        with self.assertRaises(ValueError):
            #print("self is none: ", node4.tag, " - ", node4.value is None)
            print(node4.to_html())

if __name__ == "__main__":
    unittest.main()