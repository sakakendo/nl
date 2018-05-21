import sys
if len(sys.argv) <2 :
    print('arguments is not ehough')
    exit()
n=int(sys.argv[1])

with open('hightemp.txt') as f:
    while True:
        for i in range(n):
            line=f.readline()
            if not line :exit()
            print(line[:-1:])
        print('')
        

#!split -l 10 hightemp.txt
