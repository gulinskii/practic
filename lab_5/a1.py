text = input()

def string_function(text):
    while '(' in text and ')' in text:
        position1 = text.find('(')
        position2 = text.find(')')
        text = text.replace(text[position1:position2 + 1], '')
    return text

print(string_function(text))
