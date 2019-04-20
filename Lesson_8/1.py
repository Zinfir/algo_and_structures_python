"""
1. Закодируйте любую строку из трех слов по алгоритму Хаффмана.
"""

import random

class Node:
    def __init__(self, value=None, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self):
        return f'Node[{self.value:^3}]'

class Tree:
    def __init__(self):
        self.root = None

    # функция для добавления узла в дерево
    def new_node(self, value):
        return Node('\'{}\''.format(value), None, None)

    # функция для вычисления высоты дерева
    def height(self, node):
        if node is None:
            return 0
        else:
            left_height = self.height(node.left)
            right_height = self.height(node.right)

            if left_height > right_height:
                return left_height + 1
            else:
                return right_height + 1

    # функция для распечатки элементов на определенном уровне дерева
    def print_given_level(self, root, level):
        if root is None:
            return
        if level == 1:
            print(root, end='')
        elif level > 1:
            self.print_given_level(root.left, level - 1)
            self.print_given_level(root.right, level - 1)

    # функция для распечатки дерева
    def print_level_order(self, root):
        h = self.height(root)
        i = 1
        while i <= h:
            self.print_given_level(self.root, i)
            print()
            i += 1

    # функция для вычисления ширины дерева
    def get_max_width(self, root):
        max_wdth = 0
        i = 1
        h = self.height(root)
        while i <= h:
            width = self.get_width(root, i)
            if width > max_wdth:
                max_wdth = width
            i += 1
        return max_wdth

    def get_width(self, root, level):
        if root is None:
            return 0
        if level == 1:
            return 1
        elif level > 1:
            return self.get_width(root.left, level - 1) + self.get_width(root.right, level - 1)
        self.get_width(root.right, level - 1)

def text_to_bits(text, encoding='utf-8', errors='surrogatepass'):
    bits = bin(int.from_bytes(text.encode(encoding, errors), 'big'))[2:]
    return bits.zfill(8 * ((len(bits) + 7) // 8))

if __name__ == '__main__':
    s = 'peter piper picked'

    """
    'd'-1, 'k'-1, 'c'-1, 't'-1, ' '-2, 'i'-2, 'r'-2, 'p'-4, 'e'-4
    """

    t = Tree()
    t.root = t.new_node(0)
    t.root.left = t.new_node(0)
    t.root.left.left = t.new_node('p')
    t.root.left.right = t.new_node(0)
    t.root.left.right.left = t.new_node(0)
    t.root.left.right.left.left = t.new_node('c')
    t.root.left.right.left.right = t.new_node('t')
    t.root.left.right.right = t.new_node(0)
    t.root.left.right.right.left = t.new_node('d')
    t.root.left.right.right.right = t.new_node('k')
    t.root.right = t.new_node(0)
    t.root.right.right = t.new_node('e')
    t.root.right.left = t.new_node(0)
    t.root.right.left.left = t.new_node('r')
    t.root.right.left.right = t.new_node(0)
    t.root.right.left.right.left = t.new_node(' ')
    t.root.right.left.right.left = t.new_node('i')

    # Функция некорректно печатает дерево
    t.print_level_order(t.root)
    print(f'высота: {t.height(t.root)}')
    print(f'ширина: {t.get_max_width(t.root)}')

    print("""
                                            (0)
                                             |
                                        -----------
                                       0|         |1
                                       (0)       (0)
                                        |         |
                              -----------         -----------
                             0|         |1       0|         |1
                             (p)       (0)       (0)       (e)
                                        |         |
                              -----------         -----------
                             0|         |1       0|         |1
                             (0)       (0)       (r)       (0)
                              |         |                   |
                    -----------         -----------         -----------
                   0|         |1       0|         |1       0|         |1
                   (c)       (t)       (d)       (k)      (' ')      (i)   


    """)

    dict = {
        "p": '00',
        "e": '11',
        "r": '100',
        "i": '1011',
        "c": '0100',
        "t": '0101',
        "d": '0110',
        "k": '0111',
        " ": '1010',
    }

    encode_str = ''

    for letter in s:
        for key, value in dict.items():
            if key == letter:
                encode_str += value
    print('Значения символов')
    for key, value in dict.items():
        print('\'{}\' = {}'.format(key, value))
    print('Исходная строка - ', s)
    print('Закодированная строка по алгоритму Хаффмана:')
    print(encode_str)
    print('Длина = {}'.format(len(encode_str)))
    print('Строка в двоичном виде кодировки utf-8:')
    utf8_enc_str = text_to_bits(s)
    print(utf8_enc_str)
    print('Длина = {}'.format(len(utf8_enc_str)))
