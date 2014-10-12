#!/bin/bash
rcounts1=`wc -l $1|awk '{print $1}'`
rcounts2=`wc -l $2|awk '{print $1}'`
ucounts=`cat $1 $2|awk '{print $1}'|sort -u|wc -l`
mcounts=`cat $1 $2|awk '{print $2}'|sort -u|wc -l`
(echo -e "%%MatrixMarket matrix coordinate real general\n% Generated 4-Apr-2014\n$ucounts $mcounts $rcounts1" | cat - $1 > file1)  &&  mv file1 $1
(echo -e "%%MatrixMarket matrix coordinate real general\n% Generated 4-Apr-2014\n$ucounts $mcounts $rcounts2" | cat - $2 > file1)  &&  mv file1 $2
