# 4. Check if a String is a Palindrome
is_palindrome = lambda s: s.lower() == s.lower()[::-1]


print(is_palindrome("steven"))
print(is_palindrome("madam"))
