import numpy as np
import scipy.linalg as lg

my_sqr_matrix = np.array([[1, 2, 3], [4, 15, 6], [7, 8, 9]])
print(lg.det(my_sqr_matrix))
