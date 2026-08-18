
#PART:1 USING LISTS->

temp = input("Enter string: ")
text = temp.lower()
text1 = ""

# text1.join(char for char in text if char not in punctuation)

for c in text:
    if((c>='a'and c<='z') or c==' ' or (c>='0' and c<='9')):
        text1 += c

words = list(text1.split())

alpha_sort = sorted(words)
print(f"alphabetically sorted : {alpha_sort}")

for i in range(len(words)):
    for j in range(len(words)-1):
        if len(words[j])>len(words[j+1]):
            words[j],words[j+1] = words[j+1],words[j]
        elif len(words[j])==len(words[j+1]) and words[j]>words[j+1]:
            words[j],words[j+1] = words[j+1],words[j]

print(f"length wise sorted: {words}")

#BONUS: USING TUPLE->
