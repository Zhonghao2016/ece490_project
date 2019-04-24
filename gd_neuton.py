from matrix import matrix
import numpy as np 
from numpy.linalg import inv
import pdb
# Make the score matrix. M[i][j] = number of matches team i wins -  number of matches team j wins
# run "python crawl.py" to print out the url for finding the match result between two teams and fill out the above matrix
def make_input_matrix():
    inM = np.array(matrix)
    for i in range(30):
        for j in range(i):
            inM[i][j] = -inM[j][i]
    return inM

# mean square differential w.r.t S (each team's strenth score)
def df(M, S):
    df_s = np.zeros(30)
    for i in range(30):
        df_s[i] = 2*np.sum(M[:,i]) - 2*np.sum(M[i,:]) + 4*30*S[i] - 4*np.sum(S)
    return df_s

def H_inverse():
    H_i = np.zeros((30,30))
    for i in range(30):
        for j in range(30):
            if i == j:
                H_i[i][j] = 4*30 - 4
            else:
                H_i[i][j] = -4
    pdb.set_trace()
    H_i = np.matmul(inv(np.matmul(np.transpose(H_i), H_i)), np.transpose(H_i))
    return H_i

# loss is a mean square loss. Sigma_i Sigma_j (M_ij - (S_i - S_j)) ** 2
def loss(M, S):
    l = 0
    for i in range(30):
        for j in range(30):
            l += (M[i][j] - (S[i]-S[j])) ** 2
    return l

# gradient descent
def gd_newton(lr=0.0001):
    M = make_input_matrix()
    S = np.zeros(30)
    H_i = H_inverse()
    pdb.set_trace()
    for i in range(100):
        print(loss(M,S))
        S = S - lr*V
        print(S)

gd_newton()