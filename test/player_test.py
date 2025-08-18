import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def test_uid_property(self):
        """uid property returns the unique id."""
        player = Player("Alice", "123")
        self.assertEqual(player.uid, "123")

    def test_name_property(self):
        """name property returns the name."""
        player = Player("Bonny", "123")
        self.assertEqual(player.name, "Bonny")

if __name__ == '__main__':
    unittest.main()