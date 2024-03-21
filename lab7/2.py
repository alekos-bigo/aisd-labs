def read_file(filename: str):
    res = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.strip(",").strip(".").strip(":").strip(";").strip("-").strip("?").strip("!")
                if word.isalpha():
                    res.append(word)
    return res


def hash_text(words: list, alphabet: list):
    hashed_words = []
    alphabet_len = len(alphabet)
    for idx in range(0, len(words) - 2):
        hashed_words.append(alphabet.index(words[idx]) * alphabet_len ** 2 +
                            alphabet.index(words[idx + 1]) * alphabet_len +
                            alphabet.index(words[idx + 2]))
    return hashed_words


def check_plagiarism(original_hashed_words: list, plagiarism_hashed_words: list):
    if all(word in original_hashed_words for word in plagiarism_hashed_words):
        return 3 * len(plagiarism_hashed_words)
    words_c = 0
    for word in set(original_hashed_words):
        if word in plagiarism_hashed_words:
            words_c += 3 * plagiarism_hashed_words.count(word)
    return words_c


def main():
    original_words = read_file("orig.txt")
    plagiarism_words = read_file("plagiarism.txt")
    alphabet = sorted(set(original_words) | set(plagiarism_words))
    original_hashed_words = hash_text(original_words, alphabet)
    plagiarism_hashed_words = hash_text(plagiarism_words, alphabet)
    print(check_plagiarism(original_hashed_words, plagiarism_hashed_words) / len(plagiarism_words) * 100)


if __name__ == "__main__":
    main()
