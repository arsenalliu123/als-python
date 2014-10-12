#!/usr/bin/env python
# encoding: utf-8
m = 1
u = 1
mdic = {}
udic = {}
fr2 = open('rvali')
fr3 = open('rvali_wi', 'w')
fr4 = open('rtrain')
fr5 = open('rtrain_wi', 'w')
fr6 = open('mindex', 'w')
fr7 = open('uindex', 'w')
for line in fr4:
    tmp = line.split()
    user = tmp[0]
    movie = tmp[1]
    rating = tmp[2]
    uid = udic.get(user)
    mid = mdic.get(movie)
    if uid is None:
        udic[user] = u
        u = u+1
    if mid is None:
        mdic[movie] = m
        m = m+1
    fr5.write(str(udic[user])+' '+str(mdic[movie])+' '+str(rating))
    fr5.write('\n')
fr4.close()
fr5.close()
for line in fr2:
    tmp = line.split()
    user = tmp[0]
    movie = tmp[1]
    rating = tmp[2]
    uid = udic.get(user)
    mid = mdic.get(movie)
    if uid is None:
        udic[user] = u
        u = u+1
    if mid is None:
        mdic[movie] = m
        m = m+1
    fr3.write(str(udic[user])+' '+str(mdic[movie])+' '+str(rating))
    fr3.write('\n')
fr2.close()
fr3.close()
for user in udic:
    fr7.write(str(user)+' '+str(udic[user]))
    fr7.write('\n')
for movie in mdic:
    fr6.write(str(movie)+' '+str(mdic[movie]))
    fr6.write('\n')
