#!/usr/bin/env python
# encoding: utf-8
import time
import sys
from scipy import *
from scipy.sparse import *
from numpy.linalg import *
from scipy.io import *

ui={}
mi={}
fui=open("uindex")
fmi=open("mindex")
for line in fui:
    tmp=line.split()
    ui[tmp[1]]=tmp[0]
fui.close()
for line in fmi:
    tmp=line.split()
    mi[tmp[1]]=tmp[0]
fmi.close()

M=mmread("0.08_best/0.08_10_M.mtx")
U=mmread("0.08_best/0.08_10_U.mtx")
R=mmread("rtogether")
Rr=R.tocsr()
frr=open("rcm","w")
frnr=open("nrcm","w")
nlist = {}
for i in range(U.shape[1]):
    print i
    Ri=U[ : ,i].dot(M)
    ri=Rr.getrow(i).nonzero()[1]
    rex={}
    for k in range(len(ri)):
        rex[ri[k]]=1
    mlist = []
    recommend = ""
    notre = ""
    for j in range(Ri.shape[0]):
        mlist.append([j+1,Ri[j]])
        if Ri[j]<=1.3 and j not in rex:
            print >>frnr, "%s %s %.2f" %(ui[str(i+1)], mi[str(j+1)], Ri[j])
    num = 0
    mlist.sort(key=lambda x:x[1], reverse=True)
    for item in mlist:
        if num > 49:
            break
        print >> frr, "%s %s %.2f" %(ui[str(i+1)], mi[str(item[0])], item[1])
        num += 1
frr.close()
frnr.close()
"""
index = int(ui[str(sys.argv[1])])
Ri = U[ : ,index].dot(M)
ri = Rr.getrow(index).nonzero()[1]
rex = {}
for k in range(len(ri)):
    rex[ri[k]] = 1
for j in range(Ri.shape[0]):
    if Ri[j]>=4.5 and j not in rex:
        print mi[str(j+1)]
"""
