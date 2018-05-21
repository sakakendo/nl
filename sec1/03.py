import re

text="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
l=[]

for s in re.split('\W',text):
    if s =='': continue
    print(s)
    l.append(len(s))
print(l)
