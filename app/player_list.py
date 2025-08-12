from player_node import PlayerNode


class PlayerList:
    def __init__(self, _head: None):
        """Initialize player list."""
        self.head = _head

    @property
    def is_empty(self):
        return self.head is None

    def insert(self):
        """Insert a new node at the head of list."""
        new_node = PlayerNode
        if self.head is None:
            self.head = new_node
        else:
            new_node._next = self.head
            self.head = new_node






