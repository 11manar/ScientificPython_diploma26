def max_char(s):
    char = max(s, key=s.count)
    return (char, s.count(char))
print(max_char("hello world"))
