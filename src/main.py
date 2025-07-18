from textnode import TextNode, TextType

def main():
    some_node = TextNode("text", TextType.PLAIN, "https://www.boot.dev")
    print(some_node)
    
main()