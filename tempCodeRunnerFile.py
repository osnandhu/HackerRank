s = input("Enter a string")
# To evaluate whether any character of the string contains an uppercase/lowercase/etc- Note: any character of the string:
for test in ("isalnum","isalpha","isdigit","isupper","islower"):
    print(any(eval("c." + test + "()") for c in s ))