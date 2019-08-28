#!/usr/bin/env python
# coding: utf-8

import random


def not_duplicate_generator():
    #重複チェック用フラグ
    flag =1
    #重複チェック通るまでループ
    while flag==1:
        #数字生成
        num=random.randint(12,987)
        num=str(num)
        #0パディング、しないとstrがout of range
        num=num.zfill(3)
        #桁で分解
        numa=num[0]#百の位
        numb=num[1]#十の位
        numc=num[2]#一の位
        #重複チェック
        if numa!=numb and numb!=numc and numc!=numa:
            flag=0
    return num,numa,numb,numc

def same_number(prev,next):
    prev=prev.zfill(3)
    next=next.zfill(3)
    #桁で分解
    nexta=next[0]#百の位
    nextb=next[1]#十の位
    nextc=next[2]#一の位
    #桁で分解
    preva=prev[0]#百の位
    prevb=prev[1]#十の位
    prevc=prev[2]#一の位
    same=0
    if preva==nexta or preva==nextb or preva==nextc:
        same+=1
    if prevb==nexta or prevb==nextb or prevb==nextc:
        same+=1
    if prevc==nexta or prevc==nextb or prevc==nextc:
        same+=1
    return same

def bite_count(prev,next):
    prev=prev.zfill(3)
    next=next.zfill(3)
    #桁で分解
    nexta=next[0]#百の位
    nextb=next[1]#十の位
    nextc=next[2]#一の位
    #桁で分解
    preva=prev[0]#百の位
    prevb=prev[1]#十の位
    prevc=prev[2]#一の位
    bite=0
    if preva==nextb or preva==nextc:
        bite+=1
    if prevb==nexta or prevb==nextc:
        bite+=1
    if prevc==nexta or prevc==nextb:
        bite+=1

#eat_count==same_place
def eat_count(prev,next):
    prev=prev.zfill(3)
    next=next.zfill(3)
    #桁で分解
    nexta=next[0]#百の位
    nextb=next[1]#十の位
    nextc=next[2]#一の位
    #桁で分解
    preva=prev[0]#百の位
    prevb=prev[1]#十の位
    prevc=prev[2]#一の位
    eat=0
    if preva==nexta:
        eat+=1
    if prevb==nextb:
        eat+=1
    if prevc==nextc:
        eat+=1
    return eat

#上3つ統合できるかもしれない
#わけたほういいならけす
def judge(prev,next):
    prev=prev.zfill(3)
    next=next.zfill(3)
    #桁で分解
    nexta=next[0]#百の位
    nextb=next[1]#十の位
    nextc=next[2]#一の位
    #桁で分解
    preva=prev[0]#百の位
    prevb=prev[1]#十の位
    prevc=prev[2]#一の位
    eat=0
    if preva==nexta:
        eat+=1
    if prevb==nextb:
        eat+=1
    if prevc==nextc:
        eat+=1
    bite=0
    if preva==nextb or preva==nextc:
        bite+=1
    if prevb==nexta or prevb==nextc:
        bite+=1
    if prevc==nexta or prevc==nextb:
        bite+=1
    same=0
    if preva==nexta or preva==nextb or preva==nextc:
        same+=1
    if prevb==nexta or prevb==nextb or prevb==nextc:
        same+=1
    if prevc==nexta or prevc==nextb or prevc==nextc:
        same+=1
    return eat,bite,same

player,playera,playerb,playerc=not_duplicate_generator()

#test用
print(player)
print("\n")
i=0

eat=0
redoflag=0
while 1:
    if eat == 3:
        break
    while redoflag==0:
        redoflag=0
        com,coma,comb,comc=not_duplicate_generator()
        eat,bite,same=judge(player,com) 
        if eat == 3:
            break
        if eat+bite==1 and same > 2:
            pass
        elif eat+bite==1 and same == 0:
            pass
        elif eat+bite==2 and same == 3:
            pass
        elif eat+bite==2 and same < 2:
            pass
        elif eat+bite==3 and same == 0:
            pass
        elif bite==0 and eat == 0:
            pass
        elif eat==0 and eat > 0:
            pass
        elif eat==1 and eat > 1:
            pass
        else:
            redoflag=1
    #test用
    print(com)
    print("をコールします")
    print(eat)
    print("eat")
    print(bite)
    print("biteです\n")
    i+=1
    
#test用
print(i)
print("回かかりました")
input("enter")