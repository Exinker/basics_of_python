

def int_func(word):
    word = ''.join([letter.upper() if i == 0 else letter for i, letter in enumerate(word)])
    
    return word


def transform_text(text):
    text = ' '.join([int_func(word) for word in text.split(' ')])

    return text


print(int_func('text'))
print(transform_text('text text text text'))
