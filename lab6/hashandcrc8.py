M = int(input("Введите длину массива для значений: "))
hash_map = {}


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


def div_hash(s_to_hash: str):
    res = 0
    for char in s_to_hash:
        res += ord(char)
    return int(res) % M


try:
    while True:
        s = input("Введите значение: ")
        hash_map[s] = div_hash(s)
except KeyboardInterrupt:
    print()
    print(hash_map)
    print(crc8(bytes(s, encoding="utf-8")))
    exit()
