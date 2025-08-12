from player import Player


class PlayerNode:
    def __init__(self, _player: None, _next: None, _prev: None):
        self._player = _player
        self._next = _next
        self._prev = _prev

    def __str__(self):
        """Returns a string representation of node object."""
        return str(self._player)

    def player(self):
        return self._player

    def next(self):
        return self._next

    def prev(self):
        return self._prev

    @property
    def key(self):
        """Key property returns uid of instance variable """
        return self._player.uid

    




