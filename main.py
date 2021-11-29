import Nord_ouest as no
import readfiles as rf
import Vogel
import tkinter as tk
t = [3, 3, [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [150, 300, 350], [150, 400, 250]]
l = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

from docx import Document

doc = Document('esy.docx')
L =[]
def pp():
    x = 0
    c=0
    for i in doc.paragraphs:
        if x <= 1 :
            while c<7:
                L.append(i.text[c])
                c=c+2
            return L
        else:
            break
        x = x + 1
t[2][0]=pp()

print(t)