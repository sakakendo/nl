from icecream import ic
text1=list("paraparaparadise")
text2=list("paragraph")

def makeBigram(word):
    bigram=[]
#    print(word,len(word))
    for i in range(1,len(word)):
        bigram.append(word[i-1]+word[i])
    return set(bigram)
set1,set2=makeBigram(text1),makeBigram(text2)

print('X:',''.join(text1),':',set1)
print('Y:',''.join(text2),':',set2)
print('union')
print(set1|set2)

print('intersection')
print(set1&set2)

print('differnce')
print('X-Y',set1-set2)
print('Y-X',set2-set1)

print('"se" in X?:','se' in set1)
print('"se" in Y?:','se' in set2)
