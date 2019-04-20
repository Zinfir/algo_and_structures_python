"""
2*. Определение количества различных подстрок с использованием хэш-функции.
Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
Требуется найти количество различных подстрок в этой строке.
"""
import random
import hashlib


alphabet = 'abcdefghijklmnopqrstuvwxyz'
s = ''
N = 10000

for _ in range(N):
    s += alphabet[random.randint(0, len(alphabet)-1)]

print(s)

def rabin_karp(s, t):
    count = 0
    len_sub = len(t)
    h_subs = hashlib.sha1(t.encode('utf-8')).hexdigest()
    for i in range(len(s) - len_sub + 1):
        if h_subs == hashlib.sha1(s[i:i+len_sub].encode('utf-8')).hexdigest():
            count += 1
    return count

t = s[3:6]
print('Подстрока \'{}\' встречается {} - раз'.format(t, rabin_karp(s, t)))
