temp = input("Enter string: ")
text = temp.lower()
text1 = ""

for c in text:
    if((c>='a'and c<='z') or c==' ' or (c>='0' and c<='9')):
        text1 += c

words = list(text1.split())
alpha_sort = sorted(words)

freq = {}

for word in alpha_sort:
    if word in freq:
        freq[word] += 1
    else:
        freq[word] = 1
print(f"alphabetically sorted dictionary:")

#we use .items() to decrease the load over RAM. if we dont use .items() then it wont know that after we access word, we will access freq[word] too!!

# def get_freq(item):
#     return item[1]

# freq_sorted = sorted(freq.items(),key = get_freq,reverse = True)



for word, word_f in freq.items():
    print(f"{word} : {word_f}")

sorted_dict = {}
print("Freq sorted:")
while freq:
    highest_key,highest_val = -1,-1

    for key in freq:
        if freq[key] > highest_val:
            highest_val = freq[key]
            highest_key = key

    sorted_dict[highest_key] = highest_val

    del freq[highest_key]

for word,word_f in sorted_dict.items():
    print(f"{word} : {word_f}")