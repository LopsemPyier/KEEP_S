import pickle
import os

os.mkdir("besoin")
alphatonum = {
    "a" : '1', "b" : '2', "c" : '3', "d" : '4', "e" : '5', "f" : '6', "g" : '7', "h" : '8', "i" : '9', "j" : '10', "k" : '11', "l" : '12', "m" : '13', "n" : '14', "o" : '15', "p" : '16', "q" : '17', "r" : '18', "s" : '19', "t" : '20', "u" : '21', "v" : '22', "w" : '23', "x" : '24', "y" : '25', "z" : '26', " " : '27'
}
numtoalpha = {
    "1" : 'a', "2" : 'b', "3" : 'c', "4" : 'd', "5" : 'e', "6" : 'f', "7" : 'g', "8" : 'h', "9" : 'i', "10" : 'j', "11" : 'k', "12" : 'l', "13" : 'm', "14" : 'n', "15" : 'o', "16" : 'p', "17" : 'q', "18" : 'r', "19" : 's', "20" : 't', "21" : 'u', "22" : 'v', "23" : 'w', "24" : 'x', "25" : 'y', "26" : 'z', "27" : ' '
}
with open("besoin/a", "wb") as fichier:
    mfichier = pickle.Pickler(fichier)
    mfichier.dump(alphatonum)
with open("besoin/n", "wb") as fichier:
    mfichier = pickle.Pickler(fichier)
    mfichier.dump(numtoalpha)

from random import *

dico2 = {}
cara = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJQLMNOPQRSTUVWXYZ&é~"#\'{([-|è`_\ç^à@)]°+=}*.;,?ù£¨µ%§!:<>²'
tmpCara = ''
tmp = 'abcdefghijklmnopqrstuvwxyz ABCDEFGHIJQLMNOPQRSTUVWXYZ&é~"#\'{([-|è`_\ç^à@)]°+=}*.;,?ù£¨µ%§!:<>²'
dico = {}
i = range(1, len(cara))
for a in i:
    tmpCara = choice(tmp)
    dico[a] = tmpCara
    tmp = tmp.replace(tmpCara, '')
for a in i:
    dico2[dico.get(a)] = a

'''print(dico)
print('\n\n\n\n\n\n\n\n\n\n\n\n')
print(dico2)'''



with open("besoin/dic1", "wb") as fichier:
    mfichier = pickle.Pickler(fichier)
    mfichier.dump(dico)

with open("besoin/dic2", "wb") as fichier:
    mfichier = pickle.Pickler(fichier)
    mfichier.dump(dico2)
