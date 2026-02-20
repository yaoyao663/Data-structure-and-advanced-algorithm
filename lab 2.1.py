def count_uppercase(s):
    return sum(1 for char in s if char.isalpha() and char.isupper())


def punctuation_count(s):
    return s.count('!') + s.count('?')


def caps_ratio(s):
    letters = [char for char in s if char.isalpha()]
    if len(letters) == 0:
        return 0
    return count_uppercase(s) / len(letters)


def repeated_character(s):
    count = 1
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            count += 1
            if count > 3:   
                return True
        else:
            count = 1
    return False


def detect_urgency(s):
    if not s:
        return "CALM"

    punc = punctuation_count(s)
    ratio = caps_ratio(s)

    if ratio >= 0.6 or punc >= 5:
        return "AGGRESSIVE"
    elif ratio >= 0.3 or punc >= 3:
        return "URGENT"
    else:
        return "CALM"


def detect_scam(s):
    if repeated_character(s):
        return "Potential Scam"
    else:
        return "Not a Scam"



s = input("Enter a message: ")

print(f"Number of uppercase letters: {count_uppercase(s)}")
print(f"Punctuation count: {punctuation_count(s)}")
print(f"Caps ratio: {caps_ratio(s):.2f}")

urgency = detect_urgency(s)
scam = detect_scam(s)

print(f"The message is classified as: {urgency}")
print(f"The message is classified as: {scam}")
