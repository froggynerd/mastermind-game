import random

# generator ukrytego kodu
def code_generator():
    code = []
    for num in range(0, 4):
        # losowane jednej z 6 cyfr
        a = random.randint(0, 5)
        code.append(a)
    return code
