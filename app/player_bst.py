from player_bnode import PlayerBNode
from player import Player

class PlayerBST:
    def __init__(self, root= None):
        self.root = root

    @property
    def is_empty(self):
        return self.root is None

    def insert(self, player, sub_tree_root=None):
        if not isinstance(player, PlayerBNode):
            new_node = PlayerBNode(player)
        else:
            new_node = player

        if sub_tree_root is None:
            sub_tree_root = self.root
        if sub_tree_root is None:
            self.root = new_node
            return

        if new_node.player > sub_tree_root.player:
            if sub_tree_root.right_node is None:
                sub_tree_root.right_node = new_node
                return
            else:
                self.insert(new_node, sub_tree_root.right_node)
        else:
            if sub_tree_root.left_node is None:
                sub_tree_root.left_node = new_node
                return
            else:
                self.insert(new_node, sub_tree_root.left_node)

    def search(self, root, name):
        """ Search the BST for a Player by name return PlayerBNode if found"""
        if root is None:
            return None

        if root.player.name == name:
            return root

        #recursive
        if name < root.player.name:
            return self.search(root.left_node, name)
        else:
            return self.search(root.right_node, name)

    def sorted_list(self):
        """Return a sorted list of Players"""
        sorted_result = []

        def sort_in_order(current):
            if current is None:
                return
            sort_in_order(current.left_node)
            sorted_result.append(current.player)
            sort_in_order(current.right_node)

        sort_in_order(self.root)
        return sorted_result

    def balance_from_sorted_list(self, players):
        """Given a sorted list of Players, picking middle element to build a Balanced BST."""
        if len(players) == 0:
            return None

        # Find the middle index
        mid = len(players)//2
        mid_player = players[mid]
        root = PlayerBNode(mid_player)

        # left child of root
        left_side = players[:mid]
        root.left_node = self.balance_from_sorted_list(left_side)

        # right child of root
        right_side = players[mid+1:]
        root.right_node = self.balance_from_sorted_list(right_side)

        return root

    def balanced_sorted_list(self):
        """Balance the current BST by rebuilding it from its sorted list."""
        sorted_players = self.sorted_list()
        self.root = self.balance_from_sorted_list(sorted_players)

    def __repr__(self):
        return f"PlayerBST: ({self.root!r})"


def print_tree(node, level=0):
    """Print all nodes in tree (root + subtrees)."""
    if node is None:
        return
    indent = " " * level
    print(f"{indent} - Node: {node.player.name} ({node.player.uid})")

    # making tree clean and displaying both left and right child/nodes
    if node.left_node:
        print(f"{indent}  Left: {node.left_node.player.name} ({node.left_node.player.uid})")
    else:
        print(f"{indent} Left: None")

    if node.right_node:
        print(f"{indent}  Right: {node.right_node.player.name} ({node.right_node.player.uid})")
    else:
        print(f"{indent} Right: None")

    print_tree(node.left_node, level + 1)
    print_tree(node.right_node, level + 1)

if __name__ == '__main__':
    # import random

    bst = PlayerBST()
    player1 = Player("Mae", "001")
    player2 = Player("Ava", "002")
    player3 = Player("Zoe", "003")
    player4 = Player("Leo", "004")
    player5 = Player("Jack", "005")
    player6 = Player("Dave", "006")
    player7 = Player("Shane", "007")

    bst.insert(player1)
    bst.insert(player2)
    bst.insert(player3)
    bst.insert(player4)
    bst.insert(player5)
    bst.insert(player6)
    bst.insert(player7)

    # for _ in range(3):
    #     bst.insert(random.randint(0, 10))
    #     bst.insert(3)
    #     bst.insert(4)
    #     print(bst)

    # Search for a player
    node = bst.search(bst.root, "Ava")
    if node:
        print("Found", node.player)
    else:
        print("Not found.")

    # print("Original BST structure:")
    # print(bst)

    # get sorted list
    # sorted_players = bst.sorted_list()
    # print(f"Sorted Binary Search Tree: \n {sorted_players}")

    # print list sorted but unbalanced
    print("Sorted list before balancing: ")
    for player in bst.sorted_list():
        print(player.name, player.uid)

    bst.balanced_sorted_list()

    print("\n Sorted list after balancing: ")
    for player in bst.sorted_list():
        print(player.name, player.uid)
    # BST is balanced orders by name so alphabetically arranged
    print("\n Balanced Binary Search Tree (root + all nodes): ")
    print_tree(bst.root)
