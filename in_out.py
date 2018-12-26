from tree import *
from graphviz import Graph
import os

def main():
    P = Parser()
    S = P.scan

    S.read_lines('input.txt')
    S.out_lines('output.txt')

    print(P.program())

if __name__ == "__main__":
    # dirpath = os.getcwd()
    # os.environ["PATH"] += os.pathsep + dirpath + os.pathsep + 'release\\bin'
    main()
