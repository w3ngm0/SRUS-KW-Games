import unittest
from player_hashmap import PlayerHashMap
from player import Player
from player_list import PlayerList


class TestPlayerHashmap(unittest.TestCase):

    def setUp(self):
        self.hash_m = PlayerHashMap(size=8)

    def test_initial_state(self):
        """hash map starts empty."""
        self.assertEqual(len(self.hash_m), 0)
        self.assertEqual(self.hash_m.size, 8)
        self.assertTrue(all(isinstance(slot, PlayerList) for slot in self.hash_m.hashmap))

    def test_set_and_get_player(self):
        """insert and retrieve a player."""
        self.hash_m["001"] = "Alice"
        p = self.hash_m["001"]
        self.assertIsInstance(p, Player)
        self.assertEqual(p.uid, "001")
        self.assertEqual(p.name, "Alice")
        self.assertEqual(len(self.hash_m), 1)

    def test_update_existing_player(self):
        """updating same key should not change count."""
        self.hash_m["002"] = "Bonny"
        before = len(self.hash_m)
        self.hash_m["002"] = "Bonnie"
        after = len(self.hash_m)
        self.assertEqual(before, after)
        self.assertEqual(self.hash_m["002"].name, "Bonnie")

    def test_get_missing_key_raises(self):
        with self.assertRaises(KeyError):
            _ = self.hash_m["missing"]

    def test_delete_player(self):
        self.hash_m["001"] = "Alice"
        self.hash_m["002"] = "Bob"
        self.assertEqual(len(self.hash_m), 2)

        del self.hash_m["001"]
        self.assertEqual(len(self.hash_m), 1)
        with self.assertRaises(KeyError):
            _ = self.hash_m["001"]

    def test_delete_missing_key_raises(self):
        with self.assertRaises(KeyError):
            del self.hash_m["nope"]

    def test_hash_function_accepts_player_or_uid(self):
        p = Player("Alice", "001")
        idx1 = self.hash_m.hash_function("001")
        idx2 = self.hash_m.hash_function(p)
        self.assertEqual(idx1, idx2)
        self.assertTrue(0 <= idx1 < self.hash_m.size)

    def test_get_index_with_invalid_type_raises(self):
        with self.assertRaises(TypeError):
            _ = self.hash_m.get_index(123)

    def test_collisions_chain_correctly(self):
        """force collisions and ensure all players are retrievable."""
        original = Player.my_chosen_hash_function
        try:
            Player.my_chosen_hash_function = classmethod(lambda cls, k: 42)

            self.hash_m["k1"] = "Alice"
            self.hash_m["k2"] = "Bob"
            self.hash_m["k3"] = "Charlie"

            self.assertEqual(len(self.hash_m), 3)
            self.assertEqual(self.hash_m["k1"].name, "Alice")
            self.assertEqual(self.hash_m["k2"].name, "Bob")
            self.assertEqual(self.hash_m["k3"].name, "Charlie")

            del self.hash_m["k2"]
            self.assertEqual(len(self.hash_m), 2)
            self.assertEqual(self.hash_m["k1"].name, "Alice")
            self.assertEqual(self.hash_m["k3"].name, "Charlie")
            with self.assertRaises(KeyError):
                _ = self.hash_m["k2"]
        finally:
            Player.my_chosen_hash_function = original


if __name__ == "__main__":
    unittest.main()