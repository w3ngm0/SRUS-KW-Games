from player_bnode import PlayerBNode

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

    def __repr__(self):
        return f"PlayerBST: ({self.root!r})"

if __name__ == '__main__':
    import random
    bst = PlayerBST()

    for _ in range(3):
        bst.insert(random.randint(0, 10))
        bst.insert(3)
        bst.insert(4)
        print(bst)

