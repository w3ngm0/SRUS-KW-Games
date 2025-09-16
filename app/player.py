class Player:

    def __init__(self, name: str, uid: str, score: int = 0) -> None:
        self._name = name
        self._uid = uid
        self._score = score

    @property
    def uid(self) -> str:
        """Return player's unique id."""
        return self._uid

    @property
    def name(self) -> str:
        """Return the player's name."""
        return self._name

    @property
    def score(self) -> int:
        """Return the player's score"""
        return self._score

    @score.setter
    def score(self, value: int):
        if value >= 0:
            self.score = value
        else:
            raise ValueError("Number must be a positive value.")

    def __eq__(self, other):
        """check equality with another player based on score"""
        if not isinstance(other, Player):
            return NotImplemented
        return self.score == other.score

    def __str__(self) -> str:
        """Return player object as string."""
        return f"Player(uid={self._uid}, name={self._name}, score={self._score})"

    def __repr__(self) -> str:
        return f"Player(uid={self._uid!r}, name={self._name!r}, score={self._score})"
