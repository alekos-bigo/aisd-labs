from hashandcrc8 import crc8

if __name__ == "__main__":
    s = input("Введите строку: ")
    print(f"Контрольная сумма: {crc8(bytes(s, encoding="utf-8"))}")
