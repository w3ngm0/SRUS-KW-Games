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

    def __repr__(self):
        return f"PlayerBST: ({self.root!r})"


if __name__ == '__main__':
    import random

    bst = PlayerBST()
    player1 = Player("Mae", "001")
    player2 = Player("Ava", "002")
    player3 = Player("Zoe", "003")

    bst.insert(player1)
    bst.insert(player2)
    bst.insert(player3)

    # for _ in range(3):
    #     bst.insert(random.randint(0, 10))
    #     bst.insert(3)
    #     bst.insert(4)
    #     print(bst)

    node = bst.search(bst.root, "Ava")
    if node:
        print("Found", node.player)
    else:
        print("Not found.")
