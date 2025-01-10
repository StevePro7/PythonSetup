# 4. Check if a String is a Palindrome
def is_palindrome(s):
    s = s.lower()
    return s == s[::-1]


print(is_palindrome("steven"))
print(is_palindrome("madam"))
