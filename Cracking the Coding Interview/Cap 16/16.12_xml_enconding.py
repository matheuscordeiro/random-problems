
class Attribute:

    def __init__(self, tag, value):
        self.tag = tag
        self.value = value


class Element:

    def __init__(self, tag, value):
        self.tag = tag
        self.value = value
        self.attributes = []
        self.children = []

    def add_attribute(self, attr):
        self.attributes.append(attr)

    def add_child(self, child):
        self.children.append(child)


def encode(element: Element, encoded=""):
    enconded = to_encode(element, encoded)
    for attr in element.attributes:
        enconded = encode(attr, encoded)

    encoded = f"{enconded} {0} "
    for child in element.children:
        enconded = encode(child, encoded)

    return f"{enconded} {0}"

def to_encode(obj, encoded):
    return f"{encoded} {obj.tag} {obj.value} "
    




