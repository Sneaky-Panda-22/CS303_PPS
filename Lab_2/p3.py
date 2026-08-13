def are_anagrams(s1,s2):
    temp1,temp2 = "",""
    for c in s1.lower():
        if c>='a' and c<='z':
            temp1 += c

    for c in s2.lower():
        if c>='a' and c<='z':
            temp2 += c

    if len(temp1) != len(temp2):
        return False
    for c in temp1:
        if temp1.count(c) != temp2.count(c):
            return False
    return True


s1 = input("Enter string1: ")
s2 = input("Enter string2: ")

if are_anagrams(s1,s2):
    print(f"yes")
else:
    print(f"no")