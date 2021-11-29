from typing import TextIO


def redFiles(file):
    f: TextIO = open("esy.docx", "r", encoding="utf8", errors='ignore')
    return f