import sys
import MeCab
import pprint
pp=pprint.PrettyPrinter(indent=4)

'''
raw data format
表層形\t品詞,品詞細分類1,品詞細分類2,品詞細分類3,活用形,活用型,原形,読み,発音

'''


m=MeCab.Tagger()
def morphemeParser(word)->dict:
#    print("x",word.split('\t')[0],word.split('\t')[1].split(',')[0])
    surface=word.split('\t')[0]
    base=word.split('\t')[1].split(',')[6]
    pos=word.split('\t')[1].split(',')[0]
    pos1=word.split('\t')[1].split(',')[1]
    return {'surface':surface,'base':base,'pos':pos,'pos1':pos1}

def main():
    with open('neko.txt.mecab') as neko:
        while True:
            line=m.parse(neko.readline())
            morph=[]
            for word in line.split('\n'):
                if len(word.split('\t')) >=2: #ignore only enter line
                    morph.append(morphemeParser(word))
            pp.pprint(morph)
            next=input()
            if next=='q':
                exit()
if __name__ =='__main__':
    main()
