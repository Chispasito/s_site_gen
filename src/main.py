from textnode import TextNode, TextType

def main():
    some_node = TextNode("text", TextType.PLAIN, "https://www.boot.dev")
    other_node = TextNode("text", TextType.PLAIN, "https://www.boot.dev")
    print(some_node)
    print(some_node == other_node)

    
main()