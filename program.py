from tests.car import Car, Color, Make, Model
from datastructures.avltree import AVLTree

def main():
    avl = AVLTree[int, int]()

    for node in [8, 9, 10, 2, 1, 5, 3, 6, 4, 7]:
        avl.insert(node, node)
        print(str(avl))
        print('\n====================\n')
    print(avl._root.left.value)
    
    

if __name__ == '__main__':
    main()
