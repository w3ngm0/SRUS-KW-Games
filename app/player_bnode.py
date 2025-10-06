class PlayerBNode:
    def __init__(self, player, _left: None, _right: None):
        self._player = player
        self._left = _left
        self._right = _right

    @property
    def player(self):
        return self._player

    @property
    def left_node(self) :
        return self._left

    @left_node.setter
    def left_node(self, node):
        self._left = node

    @property
    def right_node(self):
        return self._right

    @right_node.setter
    def right_node(self, node):
        self._right = node

    def __str__(self):
        return f"{self._player}, Left Node: {self._left}, Right Node:  {self._right}."

    def __repr__(self):
        class_name = self.__class__.__name__
        return f"{class_name} (Player={self._player!r}, _left= {self._left!r}, _right={self._right!r})"

