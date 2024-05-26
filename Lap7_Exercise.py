def reverse_string(s):
    if len(s)== 1:
        return s

    else:
        last_word = s[(len(s)-1):]
        remaining_word = s[:(len(s)-1)]
        return  last_word + reverse_string(remaining_word)

print(reverse_string("hello"))
print(reverse_string("python"))