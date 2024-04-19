import aiofiles
import asyncio


async def read_file(file_name: str) -> list[str]:
    words = []
    async with aiofiles.open(file_name, 'r') as file:
        async for line in file:
            words.extend(line.strip().strip(",").strip(".").lower().split())
    return words


async def count_common_words_in_files(files: list[str]):
    word_counts = {}
    tasks = [read_file(file_name) for file_name in files]
    files_content = await asyncio.gather(*tasks)
    tasks = [count_words(content, files_content, word_counts) for content in files_content]
    await asyncio.gather(*tasks)
    return word_counts


async def count_words(content: list[str], files_content: tuple[list[str]], word_counts: dict[str, int]):
    for word in content:
        if word.isalpha() and all(word in file_words for file_words in files_content):
            if word in word_counts:
                word_counts[word] += 1
            else:
                word_counts[word] = 1


async def main():
    files_to_process = [
        "./static/1.txt",
        "./static/2.txt",
        "./static/3.txt",
    ]
    word_counts = await count_common_words_in_files(files_to_process)
    if word_counts:
        i = 1
        for word, count in word_counts.items():
            print(f"Слово: \"{word}\".{' '*(30 - len(f'Слово: {word}.'))}Количество: {count}", end=' '*(50 - len(f"Слово: \"{word}\".{' '*(30 - len(f'Слово: {word}.'))}Количество: {count}")))
            if i % 2 == 0:
                print()
            i += 1
    else:
        print("В файлах нет общих слов")

if __name__ == "__main__":
    asyncio.run(main())
