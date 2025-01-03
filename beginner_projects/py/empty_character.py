def empty_character(text,ch):
    result=''
    for i in text:
        if i==' ':
            i=ch
        result+=i
    return result

text='D t C mpBl ckFrid yS le'
ch='a'
print(empty_character(text,ch))        

