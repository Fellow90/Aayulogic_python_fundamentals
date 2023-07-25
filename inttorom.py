
'''#### python program to print the star pattern -- nepal flag
for i in range(12):
    if i < 6:
        print('*'*((2*i) + 1))
    else:
        print('*' * ((2 * i)-8))
'''

intRom = {
    1: "I",
    5: "V",
    10: "X",
    50: "L",
    100: "C",
    500: "D",
    1000: "M",
    5000: "G",
    10000: "H"
}
def convertinttoRom(num):
    for key,value in intRom.items():
        if key not in intRom:

            pass
        else:
            return intRom[key]







