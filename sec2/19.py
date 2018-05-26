from icecream import ic

prefectures={}
rank=[]
with open('hightemp.txt') as f:

    while True:
        line=f.readline()
        if not line :break
        pref=line.split('\t')[0]
        if prefectures.get(pref):
            prefectures[pref]+=1
        else:
            prefectures[pref]=1
    rank=sorted(prefectures.items(),key=lambda x:x[1],reverse=True)

ic(rank)

#cat hightemp.txt |cut -f1 |sort|uniq -c |sort --reverse
