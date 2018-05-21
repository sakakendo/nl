
cnt=0
with open('hightemp.txt') as f:
    while f.readline():
        cnt+=1
print('counter:',cnt)

#!wc -l hightemp.txt 

