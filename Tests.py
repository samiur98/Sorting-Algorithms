from SortingAlgorithms import*
import unittest
class TestCases(unittest.TestCase):
    def test_insertion(self):
        #Tests for the insertion-sort algorithm.
        test_1=[1,2,3,4,5]
        test_2=[2,1,5,7,8,4]
        test_3=[9,7,1,2,3,11]
        self.assertEqual(insertion_sort(test_1),[1,2,3,4,5])
        self.assertEqual(insertion_sort(test_2),[1,2,4,5,7,8])
        self.assertEqual(insertion_sort(test_3),[1,2,3,7,9,11])
    def test_selection(self):
        #Tests for the selection-sort algorithm.
        test_1=[1,2,3,4]
        test_2=[4,12,8,1,3,9]
        test_3=[12,9,2]
        self.assertEqual(selection_sort(test_1),[1,2,3,4])
        self.assertEqual(selection_sort(test_2),[1,3,4,8,9,12])
        self.assertEqual(selection_sort(test_3),[2,9,12])
    def test_bubble(self):
        #Tests for the bubble-sort algorithm.
        test_1=[3,5,7,9]
        test_2=[5,1,4,7,12,8,17]
        test_3=[24,11,36,15,80,21,10]
        self.assertEqual(bubble_sort(test_1),[3,5,7,9])
        self.assertEqual(bubble_sort(test_2),[1,4,5,7,8,12,17])
        self.assertEqual(bubble_sort(test_3),[10,11,15,21,24,36,80])
    def test_merge(self):
        #Tests for the merge-sort algorithm.
        test_1=[2,4,6,8]
        test_2=[34,12,14,9,8,2,6]
        test_3=[11,7,9,1,3,5,7,7]
        self.assertEqual(merge_sort(test_1),[2,4,6,8])
        self.assertEqual(merge_sort(test_2),[2,6,8,9,12,14,34])
        self.assertEqual(merge_sort(test_3),[1,3,5,7,7,7,9,11])
    def test_quick(self):
        #Tests for the quick-sort algorithm.
        test_1=[3,4,5,6,7]
        test_2=[12,4,6,9,1,3,6,8,15]
        test_3=[33,31,4,56,11,24,97,65,79,29,14]
        self.assertEqual(quick_sort(test_1),[3,4,5,6,7])
        self.assertEqual(quick_sort(test_2),[1,3,4,6,6,8,9,12,15])
        self.assertEqual(quick_sort(test_3),[4,11,14,24,29,31,33,56,65,79,97])
if __name__ == '__main__':
    unittest.main()