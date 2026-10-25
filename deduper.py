

import argparse

def get_args():
    '''gets arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", default="part1TEST.txt.gz")
    parser.add_argument("-i","--input", default="testInput.sam")
    parser.add_argument("-o","--output", default="test.txt")
    parser.add_argument("-h", "--help")
    return parser.parse_args()

if __name__ == "__main__":
    do something