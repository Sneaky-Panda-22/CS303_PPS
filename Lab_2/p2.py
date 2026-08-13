def censor_string(s,badWord):
    result = ""
    censor = "*" * len(badWord)
    i = 0
    while i < len(s):
        temp = s[i:i+len(badWord)]
        if(temp.lower()==badWord.lower()):
            result += censor
            i += len(badWord)
        else:
            result += s[i]
            i+=1

    return result



st = input("Enter string: ")
bdwd = input("Input badword: ")
censored_string = censor_string(st,bdwd)

print(censored_string)