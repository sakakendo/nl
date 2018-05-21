
with open('col1.txt') as col1:
    with open('col2.txt') as col2:
        with open('merge.txt','w') as merge:
            while True:
                text1,text2=col1.readline()[:-1:],col2.readline()[:-1:]
                if not text1 or not text2:
                    break
                merge.write(text1+'\t'+text2+'\n')

paste col1.txt col2.txt 
