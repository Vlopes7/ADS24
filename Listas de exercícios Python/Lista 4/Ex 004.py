l1 = list()
d = '''The Python Software Foundation and the global Python
community welcome and encourage participation by everyone. Our community is based on
mutual respect, tolerance, and encouragement, and we are working to help each other live up
to these principles. We want our community to be more diverse: whoever you are, and
whatever your background, we welcome you'''.lower().split()

for palavra in d:
    if palavra[0] in "python" or palavra[-1] in "python":
        l1.append(palavra)

print(l1)
