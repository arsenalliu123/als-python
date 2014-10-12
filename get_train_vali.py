#!/usr/bin/env python
# encoding: utf-8
import random

fr = open("r60000")
fr2 = open("rtrain", "w")
fr3 = open("rvali", "w")
ran = random.random()
mlist = {}
ulist = {}
for line in fr:
    tmp = line.split()
    u = tmp[0]
    m = tmp[1]
    ucount = ulist.get(u)
    mcount = mlist.get(m)
    if ucount is None:
        ulist[u] = 1
    else:
        ulist[u] = ulist[u]+1
    if mcount is None:
        mlist[m] = 1
    else:
        mlist[m] = mlist[m]+1
fr.close()
fr4 = open("r60000")
for line in fr4:
    tmp = line.split()
    u = tmp[0]
    m = tmp[1]
    if mlist[m] >= 100 and ulist[u] >= 10:
        if ran < 0.85:
            fr2.write(line)
        else:
            fr3.write(line)
        ran = random.random()
fr4.close()
fr2.close()
fr3.close()
