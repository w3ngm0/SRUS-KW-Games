import unittest
from app.player import Player

class TestPlayer(unittest.TestCase):
    def test_uid_property(self):
        """Test if uid property is set correctly."""
        player = Player("Alice", "123")
        self.assertEqual(player.uid, "123")

    def test_name_property(self):
        """Test if name property is set correctly."""
        player = Player("Alice", "123")
        self.assertEqual(player.name,  "Alice")

if __name__ == '__main__':
    unittest.main()