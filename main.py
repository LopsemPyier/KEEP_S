#la valeur alphatonum permet de transformer les lettres en valeurs équivalentes à leur placement dans l'alphabet.

alphatonum = {
    "a" : '1', "b" : '2', "c" : '3', "d" : '4', "e" : '5', "f" : '6', "g" : '7', "h" : '8', "i" : '9', "j" : '10', "k" : '11', "l" : '12', "m" : '13', "n" : '14', "o" : '15', "p" : '16', "q" : '17', "r" : '18', "s" : '19', "t" : '20', "u" : '21', "v" : '22', "w" : '23', "x" : '24', "y" : '25', "z" : '26', " " : '27'
}

#la valeur numtocarac permet de transformer les valeurs en lettres et caractères spéciaux aléatoires.

numtocarac = {
    0: 'M', 1: 'l', 2: 'V', 3: '¨', 4: '.', 5: '£', 6: ',', 7: 's', 8: ')', 9: "'", 10: 'H', 11: '|', 12: 'j', 13: 'f', 14: '~', 15: 'o', 16: 'd', 17: '!', 18: 'µ', 19: 'Z', 20: '?', 21: '_', 22: 'Q', 23: '=', 24: 'q', 25: '-', 26: 'C', 27: 'x', 28: 'k', 29: 'W', 30: 'y', 31: '²', 32: '%', 33: 'i', 34: '#', 35: 'T', 36: 'E', 37: 'B', 38: 'w', 39: '}', 40: 'p', 41: 'J', 42: ']', 43: ':', 44: '`', 45: 'S', 46: 'P', 47: '*', 48: 'I', 49: 'b', 50: 'u', 51: 'é', 52: '§', 53: 'N', 54: 'r', 55: ';', 56: 'X', 57: 'D', 58: '+', 59: 'è', 60: 'g', 61: '<', 62: 'R', 63: 'F', 64: '°', 65: '>', 66: 'O', 67: '&', 68: 'e', 69: '"', 70: '\\', 71: 'G', 72: 'A', 73: 'z', 74: 'ç', 75: 'a', 76: '@', 77: '^', 78: 't', 79: '[', 80: 'L', 81: 'm', 82: 'h', 83: 'Y', 84: '(', 85: 'à', 86: 'ù', 87: '{', 88: 'v', 89: ' ', 90: 'c', 91: 'U', 92: 'n'
}

#la valeur numtoalpha permet de transformer les valeurs en lettres équivalentes à leur placement dans l'alphabet.

numtoalpha = {
    "1" : 'a', "2" : 'b', "3" : 'c', "4" : 'd', "5" : 'e', "6" : 'f', "7" : 'g', "8" : 'h', "9" : 'i', "10" : 'j', "11" : 'k', "12" : 'l', "13" : 'm', "14" : 'n', "15" : 'o', "16" : 'p', "17" : 'q', "18" : 'r', "19" : 's', "20" : 't', "21" : 'u', "22" : 'v', "23" : 'w', "24" : 'x', "25" : 'y', "26" : 'z', "27" : ' '
}

#la valeur caractonum permet de transformer les lettres et caractères spéciaux aléatoires en lettres.

caractonum = {
    'M': 0, 'l': 1, 'V': 2, '¨': 3, '.': 4, '£': 5, ',': 6, 's': 7, ')': 8, "'": 9, 'H': 10, '|': 11, 'j': 12, 'f': 13, '~': 14, 'o': 15, 'd': 16, '!': 17, 'µ': 18, 'Z': 19, '?': 20, '_': 21, 'Q': 22, '=': 23, 'q': 24, '-': 25, 'C': 26, 'x': 27, 'k': 28, 'W': 29, 'y': 30, '²': 31, '%': 32, 'i': 33, '#': 34, 'T': 35, 'E': 36, 'B': 37, 'w': 38, '}': 39, 'p': 40, 'J': 41, ']': 42, ':': 43, '`': 44, 'S': 45, 'P': 46, '*': 47, 'I': 48, 'b': 49, 'u': 50, 'é': 51, '§': 52, 'N': 53, 'r': 54, ';': 55, 'X': 56, 'D': 57, '+': 58, 'è': 59, 'g': 60, '<': 61, 'R': 62, 'F': 63, '°': 64, '>': 65, 'O': 66, '&': 67, 'e': 68, '"': 69, '\\': 70, 'G': 71, 'A': 72, 'z': 73, 'ç': 74, 'a': 75, '@': 76, '^': 77, 't': 78, '[': 79, 'L': 80, 'm': 81, 'h': 82, 'Y': 83, '(': 84, 'à': 85, 'ù': 86, '{': 87, 'v': 88, ' ': 89, 'c': 90, 'U': 91, 'n': 92
}

#programme pour crypter un message

x = 0
while x == 0:
    choice = input("Type 1 to crypt a message.\nType 2 to decrypt a message.\n")

    if choice == "1":
        out = ""
        decrypter = input("Type the decrypter :\n")
        encryptor = input("Type the encryptor :\n")
        a = 0
        b = 0
        c = ""
        d = ""
        for i in encryptor:
            out += numtocarac.get(int(alphatonum.get(i)) + int(alphatonum.get(decrypter[a])))
            a += 1

        print("The crypted text to send is :", out, "\n")
        y = 0
        while y == 0:
            answer = input("Type 1 to continue.\nType 2 to close.\n")
            if answer == "1":
                break
            elif answer == "2":
                y = 666
                continue
            else:
                print("Your answer isn't correct.\n\n")
                continue

#programme pour décrypter un message

    elif choice == "2":
        out = ""
        decrypter = input("Type the decrypter : ")
        crypted = input("Type the crypted message : ")
        print("\n")
        a = 0
        b = 0
        c = ""
        d = ""
        for i in crypted:
            out += numtoalpha.get(str(caractonum.get(i) - int(alphatonum.get(decrypter[a]))))
            
            a += 1

        print("The crypted text to send is :", out, "\n")
        y = 0
        while y == 0:
            answer = input("Type 1 to continue.\nType 2 to close.\n")
            if answer == "1":
                break
            elif answer == "2":
                x = 666
                break
            else:
                print("Your answer isn't correct.\n\n")
                continue

    else:
        print("Your answer isn't correct.\n\n")
        y = 0
        while y == 0:
            answer = input("Type 1 to continue.\nType 2 to close.\n")
            if answer == "1":
                break
            elif answer == "2":
                y = 666
                x = 666
                break
            else:
                print("Your answer isn't correct.\n\n")
                continue
        continue
      
#program by e.vasse
