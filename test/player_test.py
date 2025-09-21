import unittest
from player import Player
import random


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
        self.assertTrue(alice > bob)
        # or, event better
        self.assertGreater(alice, bob)

    def test_sort_score_quickly(self):
        """Test to check that Player.sort_score_quickly correctly sorts players by score in descending order."""
        players = [Player("Alice", uid="01", score=10),Player("Bob", uid="02", score=5),Player("Charlie", uid="03", score=15)]

        sorted_list = Player.sort_score_quickly(players)

        manually_sorted_score_list = [15,10,5]

        # assert to check if list of scores match to my manually sorted list above
        self.assertListEqual([i.score for i in sorted_list], manually_sorted_score_list)

    def test_custom_sorting_algorithm_at_scale(self):
        """Test custom sorting algorithm with a list of 1000 players."""
        players = [Player(f"Player {i}", uid=f"{i:03}", score=random.randint(0, 1000)) for i in range(1000)]

        # check descending order of sorted list
        expected_list = sorted(players, reverse=True)
        sorted_list = Player.sort_score_quickly(players)
        #sorted_list = Player.sort_quickly(players)

        # print first 10 scores to check
        for i in sorted_list[:10]:
            print(i)

        self.assertEqual(sorted_list, expected_list)

if __name__ == '__main__':
    unittest.main()
