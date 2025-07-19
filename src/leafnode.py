# Create a child class of HTMLNode called LeafNode. 
# Its constructor should differ slightly from the HTMLNode class because:
# 
# It should not allow for any children
# The value data member should be required (and tag even though the tag's value may be None), 
# while props can remain optional like the HTMLNode constructor.
# 
# Add a .to_html() method that renders a leaf node as an HTML string (by returning a string).
# If the leaf node has no value, it should raise a ValueError. All leaf nodes must have a value.
# If there is no tag (e.g. it's None), the value should be returned as raw text.
# Otherwise, it should render an HTML tag. For example, these leaf nodes:

from htmlnode import HTMLNode

class LeafNode(HTMLNode):
    def __init__(self, tag: str = None, value: str = None, props: dict = None):
        super().__init__(tag, value, props)
        self.props = props

    def to_html(self):
        if self.value is None:
            raise ValueError
        elif self.tag is not None and self.props is not None:
            return f"<{self.tag}{self.props_to_html()}>{self.value}</{self.tag}>"
        elif self.tag is not None and self.props is None:
            return f"<{self.tag}>{self.value}</{self.tag}>"
        
        return f"{self.value}"