#!/usr/bin/env python
# encoding: utf-8

fr = open("rcm")
fnr = open("nrcm")
r = {}
n = {}
rcount = {}
rsum = {}
ncount = {}
nsum = {}

for line in fr:
    tmp = line.split()
    if r.get(tmp[0]) is None:
        r[tmp[0]]=tmp[1]
        rcount[tmp[0]] = 1
        rsum[tmp[0]]=float(tmp[2])
    else:
        r[tmp[0]]+=("|"+tmp[1])
        rcount[tmp[0]]+=1
        rsum[tmp[0]]+=float(tmp[2])
for line in fnr:
    tmp = line.split()
    if n.get(tmp[0]) is None:
        n[tmp[0]]=tmp[1]
        ncount[tmp[0]] = 1
        nsum[tmp[0]]=float(tmp[2])
    else:
        n[tmp[0]]+=("|"+tmp[1])
        ncount[tmp[0]]+=1
        nsum[tmp[0]]+=float(tmp[2])

wr = open("recommend", "w")
wn = open("notrecommend", "w")
a=1
for item in r:
    wr.write(str(a)+","+item+","+r[item]+","+str(rsum[item]/rcount[item]))
    a+=1
    wr.write("\n")
b=1
for item in n:
    wn.write(str(b)+","+item+","+n[item]+","+str(nsum[item]/ncount[item]))
    b+=1
    wn.write("\n")
fr.close()
fnr.close()
wr.close()
wn.close()
