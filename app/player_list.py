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

    def insert_at_tail(self, player: Player) -> None:
        """Insert a new node at the tail (end) of the list."""
        new_node = PlayerNode(player)
        if self.is_empty:
            self._head = new_node
            self._tail = new_node

        else:
            new_node.prev = self._tail
            self._tail.next = new_node
            self._tail = new_node

    def delete_at_head(self) -> None:
        """
        Delete an existing node from the head of the list.
        Returns none if list is empty.
        """
        if self.is_empty:
            return None

        removed_node = self._head
        removed_player = removed_node.player

        # removes one node
        if self._head is self._tail:
            self._head = None
            self._tail = None

            removed_node.next = None
            removed_node.prev = None
        return removed_player

    def delete_at_tail(self) -> None:
        """
        Removing and returning the Player at the tail of the list.
        Returns none if list is empty."""
        if self.is_empty:
            return None

        removed_node = self._tail
        removed_player = removed_node.player

        if self._head is self._tail:
            self._head = None
            self._tail = None
            removed_node.next = None
            removed_node.prev = None

        return removed_player

    def delete_by_key(self, key: str):
        """Removes and returns the Player whose uid == key.
        Return none if no such players exist."""

        node = self._head
        while node is not None:
            if node.key == key:
                prev_node = node.prev
                next_node = node.next

                # Stitching neighbors
                if prev_node is None:
                    self._head = next_node
                else:
                    prev_node.next = next_node

                # Stitch right neighbor
                if next_node is None:
                    self._tail = prev_node
                else:
                    next_node.prev = prev_node

                # detach removed node
                node.prev = None
                node.next = None
                return True

            node = node.next

        return False