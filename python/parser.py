import glob
import os
import numpy
from MESAreader import getSrcCol


def check_final_R(R_threshold = 3):
    # load history file
    try:
        src, col = getSrcCol("../work/LOGS/history.data", True, False)
    except FileNotFoundError:
        print("No history output file found!")
        return
    try:
        r = 10.**(src[-1, col.index("log_R")]) # Rsun
    except ValueError:
        print("logR not in the history file, check `history_columns.list`")
        return
    return r

if __name__== "__main__":
    print(check_final_R())
