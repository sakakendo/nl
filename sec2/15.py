import sys
if len(sys.argv) <2 :
    print('arguments is not ehough')
    exit()
n=int(sys.argv[1])

with open('hightemp.txt') as f:
    text=f.readlines()
    for i in range(len(text)-n,len(text)):
        print(text[i],end='')
    

#!cat hightemp.txt |tail -n3
