class PlayerBNode:
    def __init__(self, player, _left=None, _right=None):
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

    def __eq__(self, other):
        if not isinstance(other, PlayerBNode):
            return NotImplemented
        return self.player == other.player


    def __repr__(self):
        return f"(Player = {self._player!r}, L = {self._left!r}, R= {self._right!r})"



