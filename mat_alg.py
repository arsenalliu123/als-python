#! /usr/local/bin/python
import time
import sys
from scipy import *
from scipy.sparse import *
from numpy.linalg import *
from scipy.io import *

# read training dataset & validation dataset into matrixs
# get variables like lambda from input 
R = mmread('rtrain_wi')
RM = R.tocsc()
RU = R.tocsr()
D = int(sys.argv[2])
lam = float(sys.argv[1])
u = RU.shape[0]
m = RM.shape[1]
T = mmread('rvali_wi')
logname = str(lam)+'_'+str(D)+'.log'
frlog = open(logname, 'w')
TU = T.tocsc()
RN = TU.nonzero()
RN_inarray = TU[RN]

# initialize M (movie matrix), U (user matrix)
#Fix M&U with random small numbers, D=10
M = matrix(random.normal(0.0, 0.01, (D, m)),'f64')
U = matrix(random.normal(0.0, 0.01, (D, u)),'f64')
frlog.write('lambda = %f D = %d' %(lam, D))
frlog.write('\n')
frlog.write('Initialization Finished! u = %d m = %d' %(u, m))

#definition of U's update function
def updateU(i):
    tmp = RU.getrow(i)
    if tmp.size:
        tmp2 = tmp[tmp.nonzero()]
        tmp1 = array(tmp.nonzero()[1]).reshape(tmp2.shape[1])
        RiIi = tmp2.reshape((1,tmp2.shape[1]))
        nui = RiIi.shape[1]
        MIi = M[:, array(tmp1)]
        Ai = MIi.dot(MIi.T)+lam*nui*E
        Vi = MIi.dot(RiIi.T)
        U[:, i:i+1] = inv(Ai).dot(Vi)

#definition of M's update function
def updateM(j):
    tmp = RM.getcol(j)
    if tmp.size:
        tmp2 = tmp[tmp.nonzero()]
        tmp1 = array(tmp.nonzero()[0]).reshape(tmp2.shape[1])
        RjIj = tmp2.reshape((1, tmp2.shape[1]))
        nmj = RjIj.shape[1]
        UIj = U[:, array(tmp1)]
        Aj = UIj.dot(UIj.T)+lam*nmj*E
        Vj = UIj.dot(RjIj.T)
        M[:, j:j+1] = inv(Aj).dot(Vj)

#definition of calculating RMSE function
def cRMSE():
    ERROR = 0
    for k in range(0, RN[0].size):
        i = RN[0][k]
        j = RN[1][k]
        ERROR += (RN_inarray[0, k]-U[:, i].T.dot(M[:, j]))**2
    return sqrt(ERROR/RN[0].size)

#filtering iterations
RMSE = 7
for incre in range(1, 10):
    frlog.write('\n')
    frlog.write('loop: %d' %(incre))
    E = identity(D)
    for i in range(u):
        updateU(i)
    for j in range(m):
        updateM(j)
    nRMSE = cRMSE()
    frlog.write('\n')
    frlog.write('validation RMSE:%f' %(nRMSE))
    if RMSE - nRMSE < 0.001:
        break
    RMSE = nRMSE


#save M and U into files
uname = str(lam)+'_'+str(D)+'_U'
mmwrite(uname, U)
mname = str(lam)+'_'+str(D)+'_M'
mmwrite(mname, M)
frlog.close()
