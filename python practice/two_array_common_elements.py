from collections import deque
import unittest
import doctest

# takes two sorted arrways and find the number of common elements
# assume all elements exist only once
def find_common(l1, l2):
    """
    >>> find_common([],[])
    0
    >>> find_common([1],[])
    0
    >>> find_common([4,7,9,10,11,16],[3,6,7,9,10])
    3
    >>> find_common([1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1])
    6
    >>> find_common([1],[1])
    1
    """
    if l1 and l2:       
        count = 0
        d1 = deque(l1)
        d2 = deque(l2)
        el1 = d1.popleft()
        el2 = d2.popleft()
        while d1 or d2:
            if el1 == el2:
                count+= 1
            # process nexts
            if el1 < el2:
                if d1:
                    el1 = d1.popleft()
                else:
                    return count
            elif el1 > el2:
                if d2:
                    el2 = d2.popleft()
                else:
                    return count
            else:
                if d1 and d2:
                    el2 = d2.popleft()
                    el1 = d1.popleft()
                else:
                    return count
        # catch last elements
        if el1 == el2:
            count+=1
        return count
    else:
        return 0

class MyTest(unittest.TestCase):
    def test_usual_1(self):
        self.assertEqual(find_common([4,7,9,10,11,16],[3,6,7,9,10]), 3)

    def test_same_el(self):
        self.assertEqual(find_common([1,1,1,1,1,1,1,1,1,1],[1,1,1,1,1,1]), 6)

    def test_both_empty(self):
        self.assertEqual(find_common([],[]),0)

    def test_one_empty_1(self):
        self.assertEqual(find_common([1],[]),0)

    def test_one_empty_2(self):
        self.assertEqual(find_common([],[2]),0)

    def test_both_one_el(self):
        self.assertEqual(find_common([2],[2]),1)

    def test_one_el_1(self):
        self.assertEqual(find_common([2],[1,2,3]),1)

    def test_one_el_2(self):
        self.assertEqual(find_common([1,3,5,6],[5]),1)




doctest.testmod()
unittest.main()