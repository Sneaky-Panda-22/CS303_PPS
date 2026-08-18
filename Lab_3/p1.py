temp = input("Enter string: ")
text = temp.lower()
text1 = ""

for c in text:
    if((c>='a'and c<='z') or c==' '):
        text1 += c

words = text1.split()
#print(words)

alpha_sort = sorted(words)
print(f"alphabetically sorted : {alpha_sort}")

for i in range(len(words)):
    for j in range(len(words)-1):
        if len(words[j])>len(words[j+1]):
            words[j],words[j+1] = words[j+1],words[j]
        elif len(words[j])==len(words[j+1]) and words[j]>words[j+1]:
            words[j],words[j+1] = words[j+1],words[j]

print(f"length wise sorted: {words}")