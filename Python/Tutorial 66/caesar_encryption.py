import string

original_text = "hello world"
shift = 26
alphabet = string.ascii_letters
shifted = alphabet[shift:] + alphabet[:shift]
table = str.maketrans(alphabet,shifted)
encrypted = original_text.translate(table)
print(encrypted)