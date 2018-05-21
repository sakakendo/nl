import sys
if len(sys.argv) <2 :
    print('arguments is not ehough')
    exit()
n=int(sys.argv[1])



with open('hightemp.txt') as f:
    for i in range(n):
        print(f.readline()[:-1:])
#!cat hightemp.txt |head -n3
