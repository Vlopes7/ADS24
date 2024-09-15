v = 0

for c in range(18644, 33087 + 1):
    z = str(c)

    if ("2" in z) and not ("7" in z):
        v = v + 1
    
print(f"Há {v} números com o número '2' e não com o número '7'")




