import numpy
import threading


class MatrixMult(threading.Thread):
    def __init__(self, A, B, i):
        super(MatrixMult, self).__init__()
        self.A = A
        self.B = B
        self.i = i

    def run(self):
        print(self.i, self.i)
        x = 0
        result = []
        for k in range(self.A.shape[0]):
            x += self.A[self.i, k] * self.B[k, self.i]
        self.result = x
        print(self.i, self.j)


def mult():
    n = 5
    m = 6
    A = []
    B = []
    C = []
    for i in range(n):
        for j in range(m):
            A[i, j] = i + j
            B[i, j] = i - j
    # Create and start the threads
    threads = []
    for i in range(n):
        for j in range(m):
            t = MatrixMult(A, B, i)
            threads.append(t)
            t.start()
    for t in threads: t.join()

    for t in threads:
        C[t.i] = t.result
    return C


print(mult())
