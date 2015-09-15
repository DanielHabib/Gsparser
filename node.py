import json

class Tree:
    """  The Entire DataModel """
    def __init__(self, root):
        self.root = root

    def render_json(self):
        """ Render the JSON of the Element """
        result_dict = {}
        result_dict["result"] = self.root.create_dict()
        return json.dumps(result_dict)
class Node:
    """  """
    def __init__(self, name, desc="desc", children=[], leaf=False):
        self.name = name
        self.desc = desc
        self.children = children
        self.leaf = leaf

    def create_dict(self):
        if self.children:
            child_array = []
            for child in self.children:
                dictionary = child.create_dict()
                child_array.append(dictionary)
        else:
            child_array = None
        return {
            "name": self.name,
            "desc": self.desc,
            "leaf": self.leaf,
            "children": child_array
        }
