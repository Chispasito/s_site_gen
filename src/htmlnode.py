# tag - A string representing the HTML tag name (e.g. "p", "a", "h1", etc.)
# value - A string representing the value of the HTML tag (e.g. the text inside a paragraph)
# children - A list of HTMLNode objects representing the children of this node
# props - A dictionary of key-value pairs representing the attributes of the HTML tag. 
# For example, a link (<a> tag) might have {"href": "https://www.google.com"}

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