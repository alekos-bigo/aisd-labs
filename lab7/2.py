def read_file(filename: str):
    res = []
    with open(filename, encoding="utf-8") as f:
        for line in f:
            for word in line.split():
                word = word.strip(",").strip(".").strip(":").strip(";").strip("-").strip("?").strip("!")
                if word.isalpha():
                    res.append(word)
    return res


def threes(words: list):
    res = []
    for idx in range(len(words) - 2):
        res.append(words[idx] + words[idx + 1] + words[idx + 2])
    return res


def check_plagiarism_naive(original_words: list, plagiarism_words: list):
    set_of_original_threes = set(threes(original_words))
    list_of_plagiarism_threes = threes(plagiarism_words)
    c = 0
    for word in list_of_plagiarism_threes:
        if word in set_of_original_threes:
            c += 1
    res = c / len(list_of_plagiarism_threes) * 100
    return round(res, 2)


def main():
    original_words = read_file("orig.txt")
    plagiarism_words = read_file("plagiarism.txt")
    print(check_plagiarism_naive(original_words, plagiarism_words))


if __name__ == "__main__":
    main()
