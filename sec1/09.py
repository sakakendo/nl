import random

words="I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

def randomList(n):
    l=[0]
    while len(l) <len(word)-1:
        rnd=random.randrange(1,n-1)
        if rnd not in l: l.append(rnd)
        else: continue
    l.append(n-1)
    return l

def sortWord(word):
    for i in randomList(len(word)):
        print(word[i],end='')
    print(' ',end='')

for word in words.split(' '):
    if 4 > len(word):
        print(word,end=' ')
    else:
        sortWord(word)
"""
#result
I cnd'uolt blveeie that I cuold alualtcy utnansrded what I was ranideg : the peonenmahl pweor of the hmuan mnid . 

"""
