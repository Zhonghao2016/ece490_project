import numpy as np
from matrix import make_input_matrix
import matplotlib.pyplot as plt
import pdb


# Plot the bar chart
def plot_score(score):
    team_name = ['atl', 'bos', 'bkn', 'cha', 'chi', 'cle', 'dal', 'den', 'det', 'gsw', 'hou', 'ind', 
                 'lac', 'lal', 'mem', 'mia', 'mil', 'min', 'nor', 'nyk', 'okc', 'orl', 'phi', 'pho',
                 'por', 'sac', 'sas', 'tor', 'uth', 'was']
    score = 2**score
    max_score = np.max(score)
    score = score / max_score
    score_sort = np.sort(score)[::-1]
    arg = np.argsort(score)[::-1]
    team_name_sort = []
    for i in arg:
        team_name_sort.append(team_name[i])

    y_pos = np.arange(len(team_name_sort))
    plt.bar(y_pos, score_sort, align='center', alpha=0.5)
    plt.xticks(y_pos, team_name_sort, rotation=90)
    plt.ylabel('score')
    plt.title('NBA team strength')

    plt.savefig('./strength.png')


def plot_loss(L):
    plt.plot(np.arange(len(L)), L)
    plt.savefig('./loss.png')

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
def gd(lr=0.0001):
    M = make_input_matrix()
    S = np.zeros(30)
    L = []
    for i in range(500):
        L.append(loss(M,S))
        S = S - lr*df(M, S)
    return S, L

score, loss_value = gd()
plot_score(score)
plot_loss(loss_value)
