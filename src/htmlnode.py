from textnode import TextNode, TextType

class HTMLNode():
    def __init__(self, tag: str = None, value: str = None, children: list = None, props: dict = None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props
    
    def to_html(self):
        raise NotImplemented
    
    def props_to_html(self):
        str = ""
        
        if self.props is None or self.props == {}:
            return str
        
        for prop in self.props:
            str += f" {prop}=\"{self.props[prop]}\""
        
        return str

    def __repr__(self):
        return \
            f"tag: {self.tag} \n\
            value: {self.value} \n\
            children: {self.children} \n\
            props: {self.props}"
    
class LeafNode(HTMLNode):
    def __init__(self, tag: str, value: str, props: dict = None):
        super().__init__(tag, value, None, props)

    def to_html(self):
        if self.value is None:
            raise ValueError("invalid HTML: no value")
        elif self.tag is None:
            return f"{self.value}"
        else:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"

class ParentNode(HTMLNode):
    def __init__(self, tag: str, children: list, props: dict = None):
        super().__init__(tag, None, children, props)
    
    def to_html(self):
        if self.tag is None:
            raise ValueError("invalid HTML: no value")
        elif self.children is None or self.children == []:
            raise ValueError("invalid parent: no children")
        
        output = f"<{self.tag}{self.props_to_html()}>"
        for child in self.children:
            output += child.to_html()
        
        output += f"</{self.tag}>"
        return output

def text_node_to_html_node(text_node: TextNode):
    if not text_node.text_type in TextType:
        raise AttributeError("Attribute not found")
    
    node = None
    match text_node.text_type:
        case TextType.TEXT:
            node = LeafNode("p", text_node.text)
        case TextType.BOLD:
            node = LeafNode("b", text_node.text)
        case TextType.ITALIC:
            node = LeafNode("i", text_node.text)
        case TextType.CODE:
            node = LeafNode("code", text_node.text)
        case TextType.LINK:
            node = LeafNode("a", text_node.text, {"href" : text_node.url})
        case TextType.IMAGE:
            node = LeafNode("img", "", {"src": text_node.url, "alt": text_node.text})

    return node

# It should handle each type of the TextType enum. 
# If it gets a TextNode that is none of those types, it should raise an exception. 
# Otherwise, it should return a new LeafNode object.

# TextType.TEXT: This should return a LeafNode with no tag, just a raw text value.
# TextType.BOLD: This should return a LeafNode with a "b" tag and the text
# TextType.ITALIC: "i" tag, text
# TextType.CODE: "code" tag, text
# TextType.LINK: "a" tag, anchor text, and "href" prop
# TextType.IMAGE: "img" tag, empty string value, "src" and "alt" props ("src" is the image URL, "alt" is the alt text)