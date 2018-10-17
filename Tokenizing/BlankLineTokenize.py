from nltk.tokenize import blankline_tokenize

python_data = '''Python is an interpreted high-level programming language for general-purpose programming. Created by Guido van Rossum and first released in 1991, Python has a design philosophy that emphasizes code readability, notably using significant whitespace. It provides constructs that enable clear programming on both small and large scales.[27] In July 2018, Van Rossum stepped down as the leader in the language community after 30 years.[28][29]

Python features a dynamic type system and automatic memory management. It supports multiple programming paradigms, including object-oriented, imperative, functional and procedural, and has a large and comprehensive standard library.[30]

Python interpreters are available for many operating systems. CPython, the reference implementation of Python, is open source software[31] and has a community-based development model, as do nearly all of Python's other implementations. Python and CPython are managed by the non-profit Python Software Foundation'''

python_tokens = blankline_tokenize(python_data)

# Length of the blank line tokenize

print(len(python_tokens))

# printing the data of the blank line tokenize

for item in python_tokens:
    print(item)
