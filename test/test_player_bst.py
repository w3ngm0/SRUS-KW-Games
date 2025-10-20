from player_bst import PlayerBST
from player import Player
import unittest

class TestPlayerBinarySearchTree(unittest.TestCase):
    def test_initial_tree_is_empty(self):
        """Test to check if bst is initially empty"""
        player_bst = PlayerBST()
        self.assertTrue(player_bst.is_empty)
        self.assertIsNone(player_bst.root)

    def test_insert_at_root_when_is_empty(self):
        bst = PlayerBST()
        bst.insert(10)

        # check if root is set
        self.assertIsNotNone(bst.root)
        self.assertEqual(bst.root.player, 10)

        # root should have no children
        self.assertIsNone(bst.root.left_node)
        self.assertIsNone(bst.root.right_node)

    def test_insert_second_value_goes_to_right_node(self):
        """Test to check if root not empty, larger value goes to the right side of the binary search tree """
        bst = PlayerBST()
        bst.insert(5) # first insert -> root
        bst.insert(8) # second insert -> right

        self.assertEqual(bst.root.player, 5)
        self.assertIsNotNone(bst.root.right_node)
        self.assertEqual(bst.root.right_node.player, 8)
        self.assertIsNone(bst.root.left_node)

    def test_insert_second_value_goes_to_left_node(self):
        """Test to check if root not empty, smaller value goes to the left side of the binary search tree """
        bst = PlayerBST()
        bst.insert(5) # first insert -> root
        bst.insert(3) # second insert -> left

        self.assertEqual(bst.root.player, 5)
        self.assertIsNotNone(bst.root.left_node)
        self.assertEqual(bst.root.left_node.player, 3)
        self.assertIsNone(bst.root.right_node)

if __name__ == "__main__":
    unittest.main()