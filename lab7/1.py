import time


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {end_time - start_time} секунд")
        return result

    return wrapper


def fibonacci() -> str:
    fib = [0, 1]
    for i in range(2, 500):
        fib.append(fib[i - 1] + fib[i - 2])
    return "".join(map(str, fib))


def get_set_of_sub_s(data: str) -> set:
    res = []
    for idx in range(len(data) - 1):
        dig = data[idx] + data[idx + 1]
        if len(str(int(dig))) != 2:
            continue
        res.append(dig)
    return set(res)


def naive_alg(s: str, sub_s: str) -> int:
    """O(n)"""
    c = 0
    l, r = 0, len(sub_s)
    while r != len(s) + 1:
        if s[l:r] == sub_s:
            c += 1
        l += 1
        r += 1
    return c


def rabin_karp_hash(x, m, slv, sub_s):
    h = 0
    k = 0
    for i in sub_s:
        h += slv[i] * (x ** (m - k))
        k += 1
    return h


def rabin_karp_alg(s, sub_s):
    """O(n)"""
    alphabet = sorted(set(s))
    x = len(alphabet)
    m = len(sub_s) - 1
    slv = {}
    ind = 0
    for i in alphabet:
        slv[i] = ind
        ind += 1
    hash_sub_s = rabin_karp_hash(x, m, slv, sub_s)
    l, r = 0, len(sub_s)
    c = 0
    while r != len(s) + 1:
        if hash_sub_s == rabin_karp_hash(x, m, slv, s[l:r]):
            if sub_s == s[l:r]:
                c += 1
        l += 1
        r += 1
    return c


def preprocess_bad_character(sub_s):
    bad_char = {}
    for i in range(len(sub_s)):
        bad_char[sub_s[i]] = i
    return bad_char


def boyer_mur(s, sub_s):
    m = len(sub_s)
    n = len(s)
    c = 0
    bad_char = preprocess_bad_character(sub_s)
    s_idx = 0
    while s_idx <= n - m:
        sub_idx = m - 1
        while sub_idx >= 0 and sub_s[sub_idx] == s[s_idx + sub_idx]:
            sub_idx -= 1
        if sub_idx == -1:
            c += 1
            s_idx += m
        else:
            if s[s_idx + sub_idx] in bad_char:
                s_idx += max(1, sub_idx - bad_char[s[s_idx + sub_idx]])
            else:
                s_idx += sub_idx + 1
    return c

@timer
def print_res(s: str, set_of_sub_s: set, alg):
    c_max = -float("inf")
    for sub_s in set_of_sub_s:
        c = alg(s, sub_s)
        if c > c_max:
            val = sub_s
            c_max = c
    print(f"value - {val}\ncount - {c_max}\n")


def main():
    s = fibonacci()
    set_of_sub_s = get_set_of_sub_s(s)
    print_res(s, set_of_sub_s, naive_alg)
    print_res(s, set_of_sub_s, rabin_karp_alg)
    print_res(s, set_of_sub_s, boyer_mur)


if __name__ == "__main__":
    main()
