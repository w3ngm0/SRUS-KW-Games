import unittest
from player_list import PlayerList


class TestPlayerList(unittest.TestCase):
    def setUp(self) -> None:
        self.plist = PlayerList(None)

    def test_list_starts_empty(self):
        """Test if list is empty at head."""
        self.assertTrue(self.plist.is_empty)

    def test_insert_adds_node(self):
        """Test if insert adds new node to empty list."""
        self.plist.insert()
        self.assertFalse(self.plist.is_empty)

    def test_insert_adds_multiple_node(self):
        """Test if insert adds new node to empty list."""
        self.plist.insert()
        self.plist.insert()
        self.assertFalse(self.plist.is_empty)


if __name__ == '__main__':
    unittest.main()
