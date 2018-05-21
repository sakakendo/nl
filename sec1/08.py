sentence="Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."

for char in list(sentence):
    if ord('a')<ord(char)< ord('z'):
        print(ord(char),end='')
    else:
        print(char,end='')

