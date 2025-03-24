txt = input()
txt = txt[:1]+"a"+txt[2:]
txt = txt[:len(txt)-2]+"a"+txt[-1]
print(txt)