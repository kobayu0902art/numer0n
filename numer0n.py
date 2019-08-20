#!/usr/bin/env python
# coding: utf-8

# In[11]:


#重複チェック用フラグ
replayflag =1
#重複チェック通るまでループ
while replayflag==1:
    #数字input
    q=input("any 3-digit number\n")
    #桁で分解
    a=q[0]#百の位
    b=q[1]#十の位
    c=q[2]#一の位
    #重複チェック
    if a!=b and b!=c and c!=a:
        replayflag=0

        
while eat!=3:
    import random
    #重複チェック用フラグ
    replayflag =1
    #重複チェック通るまでループ
    while replayflag==1:
        #コール用数字生成
        call=random.randint(12,987)
        call=str(call)
        #0パディング、しないとstrがout of range
        call=call.zfill(3)
        #桁で分解
        calla=call[0]#百の位
        callb=call[1]#十の位
        callc=call[2]#一の位
        #重複チェック
        if calla!=callb and callb!=callc and callc!=calla:
            replayflag=0

    print(call)
    print("をコールします")

    #eatチェック
    eat=0
    if a==calla:
        eat+=1
    if b==callb:
        eat+=1
    if c==callc:
        eat+=1

    #biteチェック
    bite=0
    if a==callb or a==callc:
        bite+=1
    if b==calla or b==callc:
        bite+=1
    if c==calla or c==callb:
        bite+=1

    print(eat)
    print("Eat")
    print(bite)
    print("Biteです。\n")


# In[10]:


eat=0


# In[ ]:




