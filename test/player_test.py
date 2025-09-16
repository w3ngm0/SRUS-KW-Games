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

    def test_sort_players(self):
        players = [Player("Alice", uid='01', score=10), Player("Bob", uid='02', score=5),
                   Player("Charlie", uid='03', score=15)]
        # note: ensure initialization code is valid for **your** implementation.
        # For example, is your parameter called uid? is the first parameter name?

        # do **not** change the following code:
        sorted_players = sorted(players)

        # players must be sorted by score as shown here:
        manually_sorted_players = [Player("Bob", uid='02', score=5), Player("Alice", uid='01', score=10),
                                   Player("Charlie", uid='03', score=15)]

        self.assertListEqual(sorted_players, manually_sorted_players)

    def test_players_can_be_compared_by_score(self):
        # note: ensure initialization code is valid for **your** implementation
        alice = Player("Alice", uid='01', score=10)
        bob = Player("Bob", uid='02', score=5)

        # Add the appropriate expression to the following assert test
        self.assertTrue(alice.score < bob.score)
        # or, event better
        self.assertGreater(alice, bob)


if __name__ == '__main__':
    unittest.main()
