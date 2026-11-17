from engine import code_generator

inputh = [1,2,3]#input czlowieka
code = code_generator()
for i in inputh:
    for x in range(6):
        if code[x] == i:
            break