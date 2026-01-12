def is_palindrome(s):
    s_clean = s.replace(" ", "").lower()
    return s_clean == s_clean[::-1]

print(is_palindrome("My name is Manar"))  
print(is_palindrome("Hello world"))           
print(is_palindrome("Race car"))            


