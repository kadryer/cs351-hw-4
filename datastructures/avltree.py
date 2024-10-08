from HW4.datastructures.iavltree import IAVLTree
from HW4.datastructures.avlnode import AVLNode
from abc import abstractmethod
from functools import total_ordering
from typing import Any, Callable, Protocol, TypeVar, Generic, Optional, List, Sequence, Tuple

@total_ordering
class Comparable(Protocol):
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...
        
K = TypeVar('K', bound=Comparable)  # Key type for ordering the nodes
V = TypeVar('V')  # Value type for storing associated data


class AVLTree(IAVLTree[K, V], Generic[K, V]):
    def __init__(self, starting_sequence: Optional[Sequence[Tuple[K, V]]]=None) -> None:
        self._root = None
        if starting_sequence != None:
            for key, value in starting_sequence:
                self.insert(key, value)
    
    def insert(self, key: K, value: V) -> None: 
        self._root = self._insert(self._root, key, value)
    
    def _insert(self, node: AVLNode, key: K, value: V) -> AVLNode:
        if node == None:
            return AVLNode(key, value)
        
        if key < node.key:
            node.left = self._insert(node.left, key, value)
        elif key > node.key:
            node.right = self._insert(node.right, key, value)
        else:
            raise ValueError("This node already exists in the tree.")
        
        node.height = 1 + max(self._height(node.left), self._height(node.right))

        self._balance_tree(node)

        return node


    def _height(self, node: AVLNode) -> int: 
        if node:
            return node.height
        else:
            return  -1

    def _balance_factor(self, node: AVLNode) -> int: 
        return self._height(node.left) - self._height(node.right)
    
    def _balance_tree(self, node: AVLNode) -> AVLNode:
        return node
        if self._balance_factor(node) > 1 and self._balance_factor(node.left) >= 0:
            self._rotate_right(node) 
            return node
        
        elif self._balance_factor(node) < -1 and self._balance_factor(node.right) <= 0:
            self._rotate_left(node) 
            return node
        
        elif self._balance_factor(node) > 1 and self._balance_factor(node.left) < 0:
            self._rotate_left(node.left) 
            self._rotate_right(node)
            return node

        elif self._balance_factor(node) < -1 and self._balance_factor(node.right) > 0:
            self._rotate_right(node.right)
            self._rotate_left(node)
            return node

        else:
            return node
       
    def _rotate_left(self, node: AVLNode) -> AVLNode:
        return
        new_root: AVLNode = node.right
        new_left_subtree: AVLNode | None = new_root.left
        new_root.left = node
        node.right = new_left_subtree
        return new_root
    
    def _rotate_right(self, node: AVLNode) -> AVLNode:
        return
        new_root: AVLNode = node.left
        new_right_subtree: AVLNode | None = new_root.right
        new_root.right = node
        node.left = new_right_subtree
        return new_root


    def search(self, key: K) -> V | None: 
        if self._root == None:
            return None
        else:
            return self._search(self._root, key)
    
    def _search(self, node: AVLNode, key: K) -> V:
        if key == node.key:
            return node.value
        if key > node.key:
            if node.right:
                return self._search(node.right, key)
            else:
                return None
        if key < node.key:
            if node.left:
                return self._search(node.left, key)
            else:
                return None

    def delete(self, key: K) -> None: 
        self._root = self._delete(self._root, key)

    def _delete(self, node: AVLNode, key: K) -> None:
        if node == None:
            return None
        
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            successor = self._delete_find_successor(node)
            if successor.value == node.value:
                node, successor = None, None
            else:
                node.key = successor.key
                node.value = successor.value
                if (node.left and node.right) and node.right != successor.right:
                    successor.right.right = node.right
                    node.right = successor.right
            
        if node:
            node.height = 1 + max(self._height(node.left), self._height(node.right))
            return node
    
    def _delete_find_successor(self, node: AVLNode) -> AVLNode:
        if not (node.left or node.right):
            return node
        elif node.left and not node.right:
            return node.left
        elif node.right and not node.left:
            current = node.right
            node.right = current.right
            return current
        else:
            current = node.right
            while current.left != None:
                if current.left.left == None:
                    successor_parent = current
                current = current.left

            try:
                successor_parent.left = None
            except:
                node.right = current.right

            return current

    
    def inorder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        global inorder_values_visited
        inorder_values_visited = []
        self._inorder(self._root, visit)
        return inorder_values_visited


    def _inorder(self, node: AVLNode, visit):
        if hasattr(node, "left"):
            self._inorder(node.left, visit)
            inorder_values_visited.append(visit(node.value)) if visit else inorder_values_visited.append(node.value)
        
        if hasattr(node, "right"):
            self._inorder(node.right, visit)

    def preorder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        global preorder_values_visited
        preorder_values_visited = []
        self._preorder(self._root, visit)
        return preorder_values_visited
    
    def _preorder(self, node: AVLNode, visit: Callable[[V], None] | None = None):
        preorder_values_visited.append(visit(node.value)) if visit else preorder_values_visited.append(node.value)
        if node.left:
            self._preorder(node.left, visit)
        if node.right:
            self._preorder(node.right, visit)


    def postorder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        global postorder_values_visited
        postorder_values_visited = []
        self._postorder(self._root, visit)
        return postorder_values_visited
    
    def _postorder(self, node: AVLNode, visit: Callable[[V], None] | None = None):
        if node.left:
            self._postorder(node.left, visit)
        if node.right:
            self._postorder(node.right, visit)
        postorder_values_visited.append(visit(node.value)) if visit else postorder_values_visited.append(node.value)

    def bforder(self, visit: Callable[[V], None] | None = None) -> List[K]: 
        global bforder_values_visited
        global bforder_values_queued
        bforder_values_queued = []
        bforder_values_visited = []
        bforder_values_queued.append(self._root)
        while bforder_values_queued:
            next_node: AVLNode = bforder_values_queued.pop(0)
            bforder_values_visited.append(visit(next_node.value)) if visit else bforder_values_visited.append(next_node.value)
            if next_node.left:
                bforder_values_queued.append(next_node.left)
            if next_node.right:
                bforder_values_queued.append(next_node.right)
        return bforder_values_visited

    def size(self) -> int: 
        return len(self.inorder())

    def __str__(self) -> str:
        def draw_tree(node: Optional[AVLNode], level: int=0) -> None:
            if not node:
                return 
            draw_tree(node.right, level + 1)
            level_outputs.append(f'{" " * 4 * level} -> {str(node.value)}')
            draw_tree(node.left, level + 1)
        level_outputs: List[str] = []
        draw_tree(self._root)
        return '\n'.join(level_outputs)

    def __repr__(self) -> str:
        descriptions = ['Breadth First: ', 'In-order: ', 'Pre-order: ', 'Post-order: ']
        traversals = [self.bforder(), self.inorder(), self.preorder(), self.postorder()]
        return f'{"\n".join([f'{desc} {"".join(str(trav))}' for desc, trav in zip(descriptions, traversals)])}\n\n{str(self)}' 
 

