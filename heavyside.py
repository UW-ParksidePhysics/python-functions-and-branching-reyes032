def heaviside(x):
    if x < 0:
        return 0
    elif x >= 0:
        return 1

print (heaviside(-1))
print (heaviside(0))
print (heaviside(1))