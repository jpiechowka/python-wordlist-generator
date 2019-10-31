import glob
import multiprocessing
import os
import shutil
import string
import time
from concurrent.futures.process import ProcessPoolExecutor
from random import SystemRandom

WORDLIST_FILE_NAME = "wordlist.txt"
MERGED_WORDLIST_FILE_NAME = "merged_wordlist.txt"

HOW_MANY_WORDLISTS = 10
HOW_MANY_WORDS = 1000

HOW_MANY_LETTERS = 6
HOW_MANY_DIGITS = 1
HOW_MANY_SYMBOLS = 1


def generate_wordlist(num_words, num_letters, num_digits, num_symbols):
    rng = SystemRandom()
    wordlist_set = set()

    for _ in range(num_words):
        letters = ''.join(rng.choice(string.ascii_letters) for _ in range(num_letters))
        digits = ''.join(rng.choice(string.digits) for _ in range(num_digits))
        symbols = ''.join(rng.choice(string.punctuation) for _ in range(num_symbols))
        word = letters + digits + symbols

        word_l = list(word)
        rng.shuffle(word_l)
        wordlist_set.add(''.join(word_l))

    return wordlist_set


def generate_and_save_wordlist_to_file(num_words, num_letters, num_digits, num_symbols, wordlist_file_path, wordlist_ctr):
    wordlist_complete_file_path = f"{wordlist_ctr}_{wordlist_file_path}"
    with open(wordlist_complete_file_path, 'w') as f:
        print(f"[+] Generating wordlist #{wordlist_ctr}. Words: {num_words}")
        for word in generate_wordlist(num_words, num_letters, num_digits, num_symbols):
            f.write(word + '\n')
        print(
            f"[+] Finished generating wordlist #{wordlist_ctr}, filename: {wordlist_complete_file_path}, size: {os.path.getsize(wordlist_complete_file_path) / (1024 * 1024.0)} megabytes")


if __name__ == '__main__':
    start_time = time.time()

    proc_pool_exec = ProcessPoolExecutor(max_workers=multiprocessing.cpu_count(), )

    for i in range(HOW_MANY_WORDLISTS):
        proc_pool_exec.submit(generate_and_save_wordlist_to_file, HOW_MANY_WORDS, HOW_MANY_LETTERS, HOW_MANY_DIGITS, HOW_MANY_SYMBOLS, WORDLIST_FILE_NAME, i + 1)

    proc_pool_exec.shutdown(wait=True)
    print(f"[+] Finished generating separate wordlists. Time elapsed: {time.time() - start_time} seconds")

    print(f"[+] Merging everything into one wordlist: {MERGED_WORDLIST_FILE_NAME}")
    with open(MERGED_WORDLIST_FILE_NAME, "w") as merged_output_file:
        for separate_wordlist_file_path in glob.glob(f"*{WORDLIST_FILE_NAME}"):
            if separate_wordlist_file_path == MERGED_WORDLIST_FILE_NAME:
                # don't want to copy the output into the output
                continue
            with open(separate_wordlist_file_path, "r") as file_to_be_merged:
                shutil.copyfileobj(file_to_be_merged, merged_output_file)

            print(f"[+] Deleting file: {separate_wordlist_file_path}")
            os.remove(separate_wordlist_file_path)

    print(f"[+] Finished merging wordlist, size: {os.path.getsize(MERGED_WORDLIST_FILE_NAME) / (1024 * 1024.0)} megabytes")
