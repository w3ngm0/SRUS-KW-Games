 # Hold player class

class Player:

    def __init__(self, name: str, uid: str):
        self.name = name
        self.uid = uid

    def uid(self):
        """Return player's unique id."""
        return self.uid

    def name(self):
        """Return the player's name."""
        return self.name

    def __str__(self) -> str:
        """Return player object as string."""
        return f"Player(uid={self.uid}, name={self.name})"


    
