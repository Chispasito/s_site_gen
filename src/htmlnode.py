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

def split_nodes_delimiter(old_nodes, delimiter, text_type):    
    text_nodes = []

    for node in old_nodes:
        if node.text_type != TextType.TEXT:
            text_nodes.append(node)
            continue
        
        split_container = node.text.split(delimiter)
    
        ob_dict = [TextNode(split_container[0], TextType.TEXT)]
        match delimiter:
            case "`":
                ob_dict.append(TextNode(split_container[1], TextType.CODE))
            case "**":
                ob_dict.append(TextNode(split_container[1], TextType.BOLD))
            case "_":
                ob_dict.append(TextNode(split_container[1], TextType.ITALIC))
            case _:
                ob_dict.append(TextNode(split_container[1], TextType.TEXT))
        ob_dict.append(TextNode(split_container[2], TextType.TEXT))
    
        text_nodes.extend(ob_dict)
        print(text_nodes)



    return text_nodes 

# This:
# node = TextNode("This is text with a `code block` word", TextType.TEXT)
# new_nodes = split_nodes_delimiter([node], "`", TextType.CODE)
#
# Becomes:
# [
#     TextNode("This is text with a ", TextType.TEXT),
#     TextNode("code block", TextType.CODE),
#     TextNode(" word", TextType.TEXT),
# ]