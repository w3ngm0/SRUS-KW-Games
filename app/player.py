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

    @classmethod
    def sort_score_quickly(cls, array_to_sort: list) -> list:
        """return list of players sorted by score in descending order."""
        if len(array_to_sort) <= 1:
            return array_to_sort
        pivot = array_to_sort[0]
        left = [] # >
        right = [] # <
        mid = [] # ==

        for i in array_to_sort:
            if i > pivot:
                left.append(i)
            elif i < pivot:
                right.append(i)
            else:
                mid.append(i)
        return Player.sort_score_quickly(left) + mid +  Player.sort_score_quickly(right)

    def __lt__(self, other, ):
        """compare player based on score"""
        return self.score < other.score

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
