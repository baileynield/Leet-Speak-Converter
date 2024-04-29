leet = {
    "a" : "@",
    "A" : 4,
    "B" : 8,
    "b" : 8,
    "E" : 3,
    "e" : 3,
    "I" : "!",
    "i" : "!",
    "L" : 1,
    "l" : 1,
    "O" : 0,
    "o" : 0,
    "S" : 5,
    "s" : 5
}

def convert(text: str) -> str:
    new_str = []
    for letter in text:
        if letter in leet:
            new_str.append(leet[letter])
        if letter not in leet.keys():
            new_str.append(letter)
    return new_str


text = "testthiswholethingcuzwecan"
print(convert(text))
