import json,gzip,re
fname='jawiki-country.json.gz'

'''
20. JSONデータの読み込み
Wikipedia記事のJSONファイルを読み込み，「イギリス」に関する記事本文を表示せよ．問題21-29では，ここで抽出した記事本文に対して実行せよ．

'''
def exercises20():
    british=''
    with gzip.open(fname,'rt') as f:
        for line in f:
            x=json.loads(line)
            if x.get('title') == 'イギリス':
                british=x.get('text')
#                print(x.get('text'))
    return british


'''
21. カテゴリ名を含む行を抽出
記事中でカテゴリ名を宣言している行を抽出せよ．

'''
def exercises21():
    with gzip.open(fname,'rt') as f:
        for line in f:
            x=json.loads(line)
            if x.get('title') == 'イギリス':
                for l in x.get('text').split('\n'):
                    if re.search('Category',l):
                        print(l)

'''
22. カテゴリ名の抽出
記事のカテゴリ名を（行単位ではなく名前で）抽出せよ．
'''
def exercises22():
    with gzip.open(fname,'rt') as f:
        for line in f:
            x=json.loads(line)
            if x.get('title') == 'イギリス':
                for l in x.get('text').split('\n'):
                    if re.search('Category',l):
                        print(re.split('[\[:\]]',l)[3])

'''
23. セクション構造
記事中に含まれるセクション名とそのレベル（例えば"== セクション名 =="なら1）を表示せよ．
'''
def exercises23():
    british=exercises20()
    p=re.compile(r'''^(={2,})\s*(.+?)\s*\1.*$''',re.MULTILINE+re.VERBOSE)
    for line in p.findall(british):
        print(len(line[0])-1,line[1])
exercises23()

