import unittest
from player_hashmap import PlayerHashMap
from player import Player


class TestPlayerHashmap(unittest.TestCase):

    def setUp(self):
        self.hash_map_table = PlayerHashMap()

    def test_insert_and_retrieve(self):
        """
        Hash map starts empty.
        Check to see if new value for hash map is inserted in empty list.
        And then retrieved.
        """
        self.hash_map_table["001"] = "Alice"
        player = self.hash_map_table["001"]
        self.assertIsInstance(player, Player)
        self.assertEqual(player.uid, "001")
        self.assertEqual(player.name, "Alice")
        self.assertEqual(len(self.hash_map_table), 1)

    def test_update_existing_key_keeps_size(self):
        """Updating an existing key changes the name but not the count."""
        self.hash_map_table["002"] = "Bonny"
        self.hash_map_table["002"] = "Becky"
        self.assertEqual(self.hash_map_table["002"].name, "Becky")
        self.assertEqual(len(self.hash_map_table), 1)

    def test_delete_removes_key(self):
        """Deleting an existing key removes it and reduces the count."""
        self.hash_map_table["003"] = "Cat"
        del self.hash_map_table["003"]
        self.assertEqual(len(self.hash_map_table), 0)

    def test_chaining_allow_colliding_keys(self) -> None:
        """Separate chaining supports multiple keys in the slots."""
        colliding_hash_map = PlayerHashMap(size=1)
        colliding_hash_map["a"] = "Apple"
        colliding_hash_map["b"] = "Banana"
        self.assertEqual(len(colliding_hash_map), 2)
        self.assertEqual(colliding_hash_map["a"].name, "Apple")
        self.assertEqual(colliding_hash_map["b"].name, "Banana")


if __name__ == "__main__":
    unittest.main()

