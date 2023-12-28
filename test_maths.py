import unittest
import numpy as np
import maths


class TestMaths(unittest.TestCase):

    # corelation function
    
    def test_euclidean_2d(self):
        self.assertEqual(maths.euclidean_distance([1, 2], [4, 6]), 5)
        
    def test_euclidean_3d(self):
        self.assertEqual(maths.euclidean_distance([1, 6, 2], [5, 1, 5]), np.sqrt(50))
        
    def test_euclidean_5d(self):
        self.assertEqual(maths.euclidean_distance([1, 6, 2, 4, 2], [5, 6, 1, 3, 5]), np.sqrt(27))
    
    # means function

    def test_means1(self):
        self.assertEqual(maths.means([1, 2, 3, 4, 5]), 3)
        
    def test_means2(self):
        self.assertEqual(maths.means([0,0,0,0,0,0,0,0,0]), 0)
        
    def test_means3(self):
        self.assertEqual(maths.means([0,0,0,0,2,2,2,2]), 1)
    
    # min max
        
    def test_x_y_min(self):
        data = [[0, 1], [-2, 5], [-3, 2], [5, 12]]
        self.assertEqual(maths.getmin(data), [-3, 1])

    def test_x_y_max(self):
        data = [[0, 1], [-2, 5], [-3, 2], [-2, 12], [5, -3]]
        self.assertEqual(maths.getmax(data), [5, 12])

    # --------------------------------------------------
    
    # ReLU
    
    def test_relu_pos(self):
        data = 5
        self.assertEqual(maths.relu(data), 5)
        
    def test_relu_neg(self):
        data = -21
        self.assertEqual(maths.relu(data), 0)
        
    def test_relu_zero(self):
        data = 0
        self.assertEqual(maths.relu(data), 0)
    
if __name__ == '__main__':
    unittest.main()
