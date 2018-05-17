import json,gzip,re

fname='jawiki-country.json.gz'

with gzip.open(fname,'rt') as f:
    for line in f:
        x=json.loads(line)
        if x.get('title') == 'イギリス':
            for l in x.get('text').split('\n'):
                if re.search('Category',l):
                    print(re.split('[\[:\]]',l)[3])

