import unittest
from player import Player
from player_list import PlayerList

class TestPlayerList(unittest.TestCase):
    def test_initial_list_is_empty(self):
        """Test to check if list is initially empty."""
        player_list = PlayerList()
        self.assertTrue(player_list.is_empty)
        self.assertIsNone(player_list.head)


    def test_insert_at_head(self):
        """Test to check if node is added to the head of the list."""
        player_list = PlayerList()
        player_1 = Player("Alice", "001")

        player_list.insert_at_head(player_1)

        self.assertFalse(player_list.is_empty)
        self.assertIsNotNone(player_list.head)
        self.assertEqual(player_list.head.player.name, "Alice")
        self.assertEqual(player_list.head.player.uid, "001")


    def test_insert_at_head_adds_new_node_as_head_when_empty(self):
        """
        Verify that inserting into a non-empty PlayerList adds a new head node containing new Player.
        The previous head is no longer the head.
        """
        player_list = PlayerList()
        player_1 = Player("Alice", "001")
        player_2 = Player("Bonny", "002")

        player_list.insert_at_head(player_1)
        first_head = player_list.head

        player_list.insert_at_head(player_2)
        new_head = player_list.head


        # head should now point to bonny
        self.assertEqual(new_head.player.name, "Bonny")
        self.assertEqual(new_head.player.uid, "002")
        self.assertIsNot(first_head, new_head)
    def test_insert_at_head_when_empty_sets_head_to_new_node_and_links_to_none(self):
        """
        Inserting into an empty list sets head to the new node,
        with head.prev and head.next both to None.
        """
        player_list = PlayerList()
        player_1 = Player("Alice", "001")

        player_list.insert_at_head(player_1)

        self.assertFalse(player_list.is_empty)
        head = player_list.head
        self.assertIsNotNone(head)
        self.assertEqual(head.player.name, "Alice")
        self.assertEqual(head.player.uid, "001")
        self.assertIsNone(head.prev)
        self.assertIsNone(head.next)


if __name__ == '__main__':
    unittest.main()
