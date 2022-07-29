print(int('f3', 16))


def hex_to_dec(val):
    n1 = int(val[1:3], 16)
    n2 = int(val[3:5], 16)
    n3 = int(val[5:], 16)
    return ','.join([str(n1), str(n2), str(n3)])


print(hex_to_dec('#23eeaa'))