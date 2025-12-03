class Node:
    """Models a single node in a binary tree."""

    def __init__(
        self,
        value,
        left_child: "Node | None" = None,
        right_child: "Node | None" = None,
    ) -> None:
        self.value = value
        self.left_child: "Node | None" = left_child
        self.right_child: "Node | None" = right_child


def print_nodes(root: Node) -> None:
    print(root.value)

    if root.left_child:
        print_nodes(root.left_child)

    if root.right_child:
        print_nodes(root.right_child)


def sum_of_nodes(root: Node) -> int:
    node_sum = root.value

    if root.left_child:
        node_sum += sum_of_nodes(root.left_child)

    if root.right_child:
        node_sum += sum_of_nodes(root.right_child)

    return node_sum


def list_of_nodes(root: Node) -> list[int]:
    node_list = [root.value]

    if root.left_child:
        node_list += list_of_nodes(root.left_child)

    if root.right_child:
        node_list += list_of_nodes(root.right_child)

    return node_list


def find_node(root: Node | None, value) -> bool:
    if not root:
        return False

    if value == root.value:
        return True

    if value > root.value:
        return find_node(root.right_child, value)
    else:
        return find_node(root.left_child, value)


if __name__ == "__main__":
    tree = Node(7)

    tree.left_child = Node(3)
    tree.left_child.left_child = Node(2)
    tree.left_child.right_child = Node(5)
    tree.left_child.right_child.left_child = Node(4)

    tree.right_child = Node(11)
    tree.right_child.right_child = Node(14)
    tree.right_child.right_child.left_child = Node(12)
    tree.right_child.right_child.left_child = Node(16)

    print_nodes(tree)

    print()
    print()

    node_sum = sum_of_nodes(tree)

    print(f"Sum of nodes is {node_sum}")

    print()
    print()

    print(list_of_nodes(tree))

    print()
    print()

    print(find_node(tree, 14))
