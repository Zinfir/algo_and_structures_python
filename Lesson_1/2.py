# 2. Выполнить логические побитовые операции "И", "ИЛИ" и др.
# над числами 5 и 6. Выполнить
# над числом 5 побитовый сдвиг вправо и влево на два знака.

a = 5
b = 6

a_bin = bin(a)
b_bin = bin(b)

bit_or = a | b
bit_and = a & b
bit_xor = a ^ b

print("bit_a:  {}".format(a_bin))
print("b_bin:  {}".format(b_bin))
print("bit_or: {}".format(bin(bit_or)))
print("bit_or: {}".format(bin(bit_and)))
print("bit_or: {}".format(bin(bit_xor)))

a_bit_shift_left = a << 2
a_bit_shift_right = a >> 2
b_bit_shift_left = b << 2
b_bit_shift_right = b >> 2

print("a_bit_shift_left:  {}".format(bin(a_bit_shift_left)))
print("a_bit_shift_right: {}".format(bin(a_bit_shift_right)))
print("b_bit_shift_left:  {}".format(bin(b_bit_shift_left)))
print("b_bit_shift_right: {}".format(bin(b_bit_shift_right)))