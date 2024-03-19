M = int(input("Введите длину массива для значений: "))
HASH_LEN = 20
hash_map = {}
p = 2 ** 64
m = 11


def crc8(data):
    crc = 0
    for byte in data:
        crc ^= byte
        for _ in range(8):
            if crc & 0x80:
                crc = (crc << 1) ^ 0x07
            else:
                crc <<= 1
            crc &= 0xFF
    return crc


def additive_hash(str_pwd):
    if len(str_pwd) < m:
        str_pwd += '*'
    while len(str_pwd) < m:
        str_pwd += '0'

    int_pwd = 0
    # k = 31
    # l = 0
    for i in str_pwd:
        # int_pwd += ord(i) * (k ** l)
        # l += 1
        int_pwd += ord(i)
    return int_pwd % p


def div_hash(s_to_hash: str):
    res = ''
    for char in s_to_hash:
        res += str(ord(char) % M)
    res += "0" * (HASH_LEN - len(res))
    return int(res)


try:
    while True:
        s = input("Введите значение: ")
        hash_map[s] = additive_hash(s)
except KeyboardInterrupt:
    print()
    print(hash_map)
    print(crc8(bytes("1", encoding="utf-8")))
    exit()
