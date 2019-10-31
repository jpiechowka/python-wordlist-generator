# Python wordlist generator
Python script to generate wordlists to crack passwords using utilities like hashcat. It will generate multiple wordlists using ProcessPoolExecutor with unique words and then merge them in one big list.

### Usage
Just run it with Python 3. No additional dependencies are required.
```
python3 wordlist_generator.py
```

### Configuration
Configuration can be changed using variables defined in the script. Numbers of letters (uppercase and lowercase), digits and symbols can be configured separately.
```python
WORDLIST_FILE_NAME = "wordlist.txt"
MERGED_WORDLIST_FILE_NAME = "merged_wordlist.txt"

HOW_MANY_WORDLISTS = 10
HOW_MANY_WORDS = 1000

HOW_MANY_LETTERS = 6
HOW_MANY_DIGITS = 1
HOW_MANY_SYMBOLS = 1
```

#### Examplary output of the script
```
[+] Generating wordlist #1. Words: 1000
[+] Generating wordlist #2. Words: 1000
[+] Generating wordlist #3. Words: 1000
[+] Generating wordlist #4. Words: 1000
[+] Generating wordlist #5. Words: 1000
[+] Generating wordlist #6. Words: 1000
[+] Generating wordlist #7. Words: 1000
[+] Generating wordlist #8. Words: 1000
[+] Finished generating wordlist #2, filename: 2_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #7, filename: 7_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Generating wordlist #9. Words: 1000
[+] Generating wordlist #10. Words: 1000
[+] Finished generating wordlist #5, filename: 5_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #8, filename: 8_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #6, filename: 6_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #1, filename: 1_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #3, filename: 3_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #4, filename: 4_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #9, filename: 9_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating wordlist #10, filename: 10_wordlist.txt, size: 0.007819175720214844 megabytes
[+] Finished generating separate wordlists. Time elapsed: 0.17534589767456055 seconds
[+] Merging everything into one wordlist: merged_wordlist.txt
[+] Deleting file: 1_wordlist.txt
[+] Deleting file: 6_wordlist.txt
[+] Deleting file: 7_wordlist.txt
[+] Deleting file: 2_wordlist.txt
[+] Deleting file: 5_wordlist.txt
[+] Deleting file: 10_wordlist.txt
[+] Deleting file: 4_wordlist.txt
[+] Deleting file: 3_wordlist.txt
[+] Deleting file: 9_wordlist.txt
[+] Deleting file: 8_wordlist.txt
[+] Finished merging wordlist, size: 0.0858306884765625 megabytes
```