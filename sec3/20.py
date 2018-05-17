import json,gzip

fname='jawiki-country.json.gz'

with gzip.open(fname,'rt') as f:
    for line in f:
        x=json.loads(line)
        if x.get('title') == 'イギリス':
            print(x.get('text'))

