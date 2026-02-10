alphabets = 'abcdefghijklmnopqrstuvwxyz'
word = input()
result = [str(word.count(a)) for a in alphabets]
print(' '.join(result))