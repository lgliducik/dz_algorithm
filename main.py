from typing import Tuple


class Node:
    """Класс Node(класс описывающий ноду в дереве)"""

    def __init__(self, value: int, left = None, right = None) -> None:
        """инициализация ноды, value - значение, left - левый потомок, right - правый потомок """

        self.value = value
        self.left = left
        self.right = right

    def __str__(self) -> str:
        """ красиво распечатать инстанс класса Node"""

        res = f'значение нашего узла: {self.value}'
        if self.left:
            res += f' значение левого: {self.left.value}'
        if self.right:
            res += f' значение правого: {self.right.value}'
        return res


class Tree:
    """Класс дерева(класс описывающий дерево)"""

    def __init__(self, root: Node = None) -> None:
        self.root = root

    def search(self, node: Node, data: int, parent: Node = None) -> Tuple:
        """метод поиска по дереву"""

        if node is None:
            return None, parent, False
        if data == node.value:
            return node, parent, True

        if data > node.value:
            if node.right:
                self.search(node.right, data, node)
        if data < node.value:
            if node.left:
                self.search(node.left, data, node)
        return node, parent, False

    def add_node(self, value: int) -> None:
        """метод добавления нового узла в дерево"""

        res = self.search(self.root, value)
        if not res[2]:
            new_node = Node(value)
            if value > res[0].value:
                res[0].right = new_node
            else:
                res[0].left = new_node
        else:
            print('такое значение уже есть')


initial_node = Node(15)

tree_1 = Tree(initial_node)

print(initial_node)
tree_1.add_node(16)
tree_1.add_node(7)
print(initial_node.right)
print(initial_node)
print(tree_1.search(initial_node, 16))
