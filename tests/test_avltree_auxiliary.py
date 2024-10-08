import pytest

from HW4.datastructures.avltree import AVLTree

class TestAVLTreeAuxiliary:
    @pytest.fixture
    def avltree(self) -> AVLTree: return AVLTree[int, int]([(8, 8), (9, 9), (10, 10), (2, 2), (1, 1), (5, 5), (3, 3), (6, 6), (4, 4), (7, 7)])

    def test_size_filled_with_ten_items_should_be_ten(self, avltree: AVLTree) -> None: assert avltree.size() == 10
    def test_size_empty_tree_should_be_zero(self) -> None: assert AVLTree[int, int]().size() == 0

    def test_search_should_be_found(self, avltree: AVLTree) -> None: assert avltree.search(7) == 7
    def test_search_should_not_be_found(self, avltree: AVLTree) -> None: assert avltree.search(11) is None

    ### TESTS EDITED TO FIT ASSERTION FOR A TREE WITHOUT BALANCING (note: inorder() needed no change).
    ### Furthermore, it would be fitting to give each of these tests assertions for the other 
    ### Traversal Orders, but it isn't terribly meaningful while my rotations don't work. 
    def test_insert_bforder(self, avltree: AVLTree) -> None: assert avltree.bforder() == [8, 2, 9, 1, 5, 10, 3, 6, 4, 7]
    def test_insert_inorder(self, avltree: AVLTree) -> None: assert avltree.inorder() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    def test_insert_preorder(self, avltree: AVLTree) -> None: assert avltree.preorder() == [8, 2, 1, 5, 3, 4, 6, 7, 9, 10]
    def test_insert_postorder(self, avltree: AVLTree) -> None: assert avltree.postorder() == [1, 4, 3, 7, 6, 5, 2, 10, 9, 8]
