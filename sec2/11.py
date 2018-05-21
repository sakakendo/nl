import re

with open('hightemp.txt') as fin:
    with open('result.txt','w') as fout:
        fout.write(re.sub('\t',' ',fin.read()))

#!cat hightemp.txt |tr t  >>result.txt
