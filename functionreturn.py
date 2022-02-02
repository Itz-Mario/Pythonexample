def reverseword(inword):
    lenword = len(inword)-1
    revword = ""
    for letter in range(lenword,-1,-1):
        revword = revword + inword[letter]
        return revword
    #print(revword)

def palindrometest(typedword,reversedword):
    if userinputvar == capturedword:
        return True
    else:
        return False


# Palindrome Finder
# User types in a word
# I find out if it is a palindrome

userinputvar = input("Insert word: ")
capturedword = reverseword(userinputvar)
ispalindrome = palindrometest(userinputvar,capturedword)
print(f"{userinputvar} tested: {ispalindrome}")