class Player:
    def __init__(self, name: str, uid: str) -> None:
        self._name = name
        self._uid = uid

    @property
    def uid(self) -> str:
        """Return player's unique id."""
        return self._uid

    @property
    def name(self) -> str:
        """Return the player's name."""
        return self._name

    def __str__(self) -> str:
        """Return player object as string."""
        return f"Player(uid={self._uid}, name={self._name})"

    def __repr__(self) -> str:
        return f"Player(uid={self._uid!r}, name={self._name!r})"

    @classmethod
    def my_chosen_hash_function(cls, key: str) -> int:
        """A simple custom hash: sum of char codes mod a large prime."""
        return sum(ord(ch) for ch in key) % 101 - 3

    def __hash__(self):
        return Player.my_chosen_hash_function(self._uid)

    # @classmethod
    # def hash(cls, key: str):
    #     return hash(key)

    def __eq__(self, other: object) -> bool:
        """check equality with another player based on uid"""
        if not isinstance(other, Player):
            return NotImplemented
        return self.uid == other.uid

