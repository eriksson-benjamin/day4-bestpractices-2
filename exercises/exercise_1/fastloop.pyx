cimport numpy as np
from scipy.interpolate import Rbf
def rbf_network_cython(np.ndarray[np.float64_t, ndim = 2] X, np.ndarray[np.float64_t, ndim = 1] beta):
    cdef int D
    D = 5    
    rbf = Rbf(X[:,0], X[:,1], X[:,2], X[:,3], X[:, 4], beta)
    Xtuple = tuple([X[:, i] for i in range(D)])
    return rbf(*Xtuple)