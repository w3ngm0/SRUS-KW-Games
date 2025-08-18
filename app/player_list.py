from player import Player
from player_node import PlayerNode


class PlayerList:
    def __init__(self) -> None:
        """Initialize player list."""
        self._head = None
        self._tail = None

    @property
    def head(self):
        """Return the head node of the list."""
        return self._head

    @property
    def tail(self):
        """Return the tail node of the list."""
        return self._tail

    @property
    def is_empty(self) -> bool:
        """Return True if list is empty."""
        return self._head is None

    def insert_at_head(self, player: Player) -> None:
        """Insert new node containing player at the head of the list."""
        new_node = PlayerNode(player)
        if self.is_empty:
            self._head = new_node
            self._tail = new_node
        else:
            new_node.next = self._head  # uses setter
            self._head.prev = new_node   # uses setter
            self._head = new_node

