from TextType import TEXT

class HTMLNode:
    def __init__(self, tag: str = TEXT, value: str | None, children: HTMLNode | None, props: dict | None):
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self) -> None:
        raise NotImplementedError

    def props_to_html(self) -> str:
        res = ""
        for key, value in self.props.item():
            res += f' {key}="{value}"'
        return res

    def __repr__(self) -> str:
        return f"Node={self}\nTag={self.tag}\nValue={self.value}\nChildren={self.children}\nProps={self.props}"
