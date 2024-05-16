
from enum import Enum

class NodeType(Enum):
  
  INPUT = 'input'
  OUTPUT = 'output'
  HIDDEN = 'hidden'

class Node:
    def __init__(self, node_id, node_type):
        self.node_id = node_id
        self.node_type = node_type
        self.value = 0
        self.layer = None 

    def set_layer(self, layer):
        self.layer = layer

class InputNode(Node):
    def __init__(self, node_id):
        super().__init__(node_id, 'input')

class OutputNode(Node):
    def __init__(self, node_id):
        super().__init__(node_id, 'output')

class HiddenNode(Node):
    def __init__(self, node_id):
        super().__init__(node_id, 'hidden')
