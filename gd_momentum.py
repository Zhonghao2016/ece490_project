from matrix import make_input_matrix
import numpy as np 


# mean square differential w.r.t S (each team's strenth score)
def df(M, S):
    df_s = np.zeros(30)
    for i in range(30):
        df_s[i] = 2*np.sum(M[:,i]) - 2*np.sum(M[i,:]) + 4*30*S[i] - 4*np.sum(S)
    return df_s

# loss is a mean square loss. Sigma_i Sigma_j (M_ij - (S_i - S_j)) ** 2
def loss(M, S):
    l = 0
    for i in range(30):
        for j in range(30):
            l += (M[i][j] - (S[i]-S[j])) ** 2
    return l

# gradient descent
def gd_momentum(lr=0.0001, beta=0.2):
    M = make_input_matrix()
    S = np.zeros(30)
    V = np.zeros(30)
    for i in range(500):
        print(loss(M,S))
        V = beta*V + (1-beta)*df(M, S)
        S = S - lr*V
        print(S)

gd_momentum()