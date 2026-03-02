import numpy as np
import time

N = 10000
A = np.random.rand(N, N)

def row_sums(A):
    N = A.shape[0]
    s = 0.0
    for i in range(N):
        s += np.sum(A[i, :])
    return s


def col_sums(A):
    N = A.shape[1]
    s = 0.0
    for j in range(N):
        s += np.sum(A[:, j])
    return s

def time_func(f, *args):
    t0 = time.perf_counter()
    result = f(*args)
    return time.perf_counter() - t0, result

t_row, _ = time_func(row_sums, A)
t_col, _ = time_func(col_sums, A)


print(f"Row sums time: {t_row:.3f} s")
print(f"Col sums time: {t_col:.3f} s")

A_f = np.asfortranarray(A)

t_row_f, _ = time_func(row_sums, A_f)
t_col_f, _ = time_func(col_sums, A_f)

print("\nWith Fortran order:")
print(f"Row sums time: {t_row_f:.3f} s")
print(f"Col sums time: {t_col_f:.3f} s")



"""
the results are 

Row sums time: 0.227 s
Col sums time: 1.060 s

With Fortran order:
Row sums time: 1.122 s
Col sums time: 0.228 s

even though both loops perform the same number of operations, row wise traversal is faster for C-order (python)
because it accesses memory with stride-1 which uses all 8 doubles per cache line, meaning each cache line is 
fully utilized, achieving b_effective = b_peak.
column wise traversal uses tride-N which uses 1 out of 8 doubles almost increasing b by a factor of 8.
For Fortran order, the situation is reversed.

"""