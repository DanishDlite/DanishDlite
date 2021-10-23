def stringreplacer(phrase,object1,replace,count):
    p = len(phrase)
    o = len(object1)
    start=0
    phrase_new = ""
    c = 0
    for i in range(0,p+1):
        i_new = i+o
        if phrase[i:i_new] == object1 and count != c:
            c+=1
            index = i
            phrase_new += (phrase[start:index]+replace)
            start = i+o
    if start != p:
        phrase_new += (phrase[start:p])
    return phrase_new 