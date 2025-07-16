import random

characters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "r", "s", "t", "w", "u", "x", "y", "z",
              "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "R", "S", "T", "W", "U", "X", "Y", "Z",
              "1", "2", "3", "4", "5", "6", "7", "8", "9", "0",
              "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ";", ":", "'", '"', "<", ">", ",", ".", "/", "?"]

zmienna = characters
zmienna2 = characters
zmienna3 = characters
zmienna4 = characters
zmienna5 = characters
zmienna6 = characters
zmienna7 = characters
zmienna8 = characters
zmienna9 = characters
zmienna10 = characters
zmienna11 = characters
zmienna12 = characters
zmienna13 = characters

print("Welcome to the 13-character password generator! Have fun!")
print("Press ENTER to generate")
print("Type 'esc' to exit")
while True:
    choose = input("by chlebek")
    if choose == "esc":
        break
    print("*")
    print(zmienna[int(random.randint(0, 78))] + zmienna2[int(random.randint(0, 78))] + 
          zmienna3[int(random.randint(0, 78))] + zmienna4[int(random.randint(0, 78))] + 
          zmienna5[int(random.randint(0, 78))] + zmienna6[int(random.randint(0, 78))] + 
          zmienna7[int(random.randint(0, 78))] + zmienna8[int(random.randint(0, 78))] + 
          zmienna9[int(random.randint(0, 78))] + zmienna10[int(random.randint(0, 78))] + 
          zmienna11[int(random.randint(0, 78))] + zmienna12[int(random.randint(0, 78))] + 
          zmienna13[int(random.randint(0, 78))])
    print("*")

print("See you!")