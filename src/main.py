from textnode import TextNode, TextType
from htmlnode import *

def main():
    text_node = TextNode("text", TextType.TEXT, "https://www.boot.dev")
    # leaf_node = LeafNode("this", "that", [])
    node = TextNode("This is text with a `code block` word", TextType.TEXT)
    node2 = TextNode("Another `print()` code", TextType.TEXT)
    new_nodes = split_nodes_delimiter([node, node2], "`", TextType.CODE)
    # print(new_nodes)
    
main()