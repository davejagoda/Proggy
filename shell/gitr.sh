#!/bin/sh

for d in `ls`
do
    cd $d
    pwd
    git branch -a
    git status
    git branch -a
    cd ..
    echo
done
