orig_str = input("Enter a string: ")
ans_str = ""

for c in orig_str:
    if(c=='a' or c=='e' or c=='i' or c=='o' or c=='u' or c=='A' or c=='E' or c=='I' or c=='O' or c=='U'):

        ans_str = ans_str + "*"

    else:
        ans_str = ans_str + c

print(ans_str)