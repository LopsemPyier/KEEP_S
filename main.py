import pickle
import os

with open("besoin/dic1", "rb") as fichier:
    mfichier = pickle.Unpickler(fichier)
    numtocarac = mfichier.load()

with open("besoin/dic2", "rb") as fichier:
    mfichier = pickle.Unpickler(fichier)
    caractonum = mfichier.load()

with open("besoin/a", "rb") as fichier:
    mfichier = pickle.Unpickler(fichier)
    alphatonum = mfichier.load()

with open("besoin/n", "rb") as fichier:
    mfichier = pickle.Unpickler(fichier)
    numtoalpha = mfichier.load()
answer = ""

#programme pour crypter un message

while 1:
    choice = input("Type 1 to crypt a message.\nType 2 to decrypt a message.\nType 0 to close.\n")

    if choice == "1":
        out = ""
        decrypter = input("Type the decrypter :")
        encryptor = input("Type the encryptor :")
        f = input("Type de file : ")
        a = 0
        for i in encryptor:
            out += numtocarac.get(int(alphatonum.get(i)) + int(alphatonum.get(decrypter[a])))
            a += 1
        print("The text encrypted is {}".format(out))
        os.mkdir(f)
        fi = f + "/text"
        with open(fi, "wb") as fichier:
            mfichier = pickle.Pickler(fichier)
            mfichier.dump(out)
        fi = f + "/dico1"
        with open(fi, "wb") as fichier:
            mfichier = pickle.Pickler(fichier)
            mfichier.dump(caractonum)
        fi = f + "/dico2"
        with open(fi, "wb") as fichier:
            mfichier = pickle.Pickler(fichier)
            mfichier.dump(numtocarac)

        while 1:
            answer = input("Type 1 to continue.\nType 2 to close.\n")
            if answer == "1":
                break
            elif answer == "2":
                break
            else:
                print("Your answer isn't correct.\n\n")
                continue

#programme pour décrypter un message

    elif choice == "2":
        out = ""
        decrypter = input("Type the decrypter :")
        f = input("Type de file : ")
        fi = f + "/text"
        with open(fi, "rb") as fichier:
            mfichier = pickle.Unpickler(fichier)
            crypted = mfichier.load()
        fi = f + "/dico1"
        with open(fi, "rb") as fichier:
            mfichier = pickle.Unpickler(fichier)
            caractonum = mfichier.load()
        fi = f + "/dico2"
        with open(fi, "rb") as fichier:
            mfichier = pickle.Unpickler(fichier)
            numtocarac = mfichier.load()

        a = 0
        for i in crypted:
            out += numtoalpha.get(str(caractonum.get(i) - int(alphatonum.get(decrypter[a]))))

            a += 1

        print("\nThe crypted text is :", out, "\n")
        while 1:
            answer = input("Type 1 to continue.\nType 2 to close.\n")
            if answer == "1":
                break
            elif answer == "2":
                break
            else:
                print("Your answer isn't correct.\n\n")
                continue

    if answer == "2" or choice == "0":
    	print("program by e.vasse & n.frison")
    	break

    else:
        print("Your answer isn't correct.\n\n")
        continue


#program by e.vasse & n.frison
