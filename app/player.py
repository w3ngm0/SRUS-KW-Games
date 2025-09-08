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
