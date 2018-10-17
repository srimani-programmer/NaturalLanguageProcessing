from nltk.util import bigrams
from nltk.tokenize import word_tokenize,sent_tokenize
python_data = '''Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation'''

data_wordtokens = word_tokenize(python_data)
data_senttokens = sent_tokenize(python_data)

data_wordbigram = bigrams(data_wordtokens)
data_sentbigram = bigrams(data_senttokens)

for data in data_wordbigram:
    print(data)
#print(data_bigram)
print('\n\n')
for data in data_sentbigram:
    print(data)
    print('\n')