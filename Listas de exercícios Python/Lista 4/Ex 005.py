d = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''.lower().split()

c = 0

for palavra in d:
    if len(palavra) > 4:
        for letra in palavra:
            if letra in "python":
                c = c + 1
                break
    
print(c)

