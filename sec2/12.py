
with open('hightemp.txt') as f:
    with open('col1.txt','w') as col1:
        with open('col2.txt','w') as col2:
            texts=f.readlines()
            for line in texts:
                col1.write(line.split('\t')[0]+'\n')
                col2.write(line.split('\t')[1]+'\n')

#!cat hightemp.txt |cut -f 1
#!cat hightemp.txt |cut -f 2
