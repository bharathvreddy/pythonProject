#first code


def editorMiss(textInput):
    arr="qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890 "
    count=0
    for i in textInput:
        if i not in arr:
            count+=1
    return count