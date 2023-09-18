def translate(phrase):
    translated_phrase = ""
    for char in phrase:
        if char.lower() in "aeiou":
            translated_phrase+="g"
        else:
            translated_phrase+=char
    return translated_phrase

user_input = input("Enter a phrase to translate: ")

print(translate(user_input))
