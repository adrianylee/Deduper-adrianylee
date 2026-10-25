import argparse

def deduplicate(input_sam, output_sam, umi_file):
    
    seen = set()
    current = None

    counts = 0
    duplicates = 0
    invalidUMI = 0

    validUMIs = set()

    with open(umi_file, "r") as umi_handle:
        for line in umi_handle:
            umi = line.strip()
            if umi:
                validUMIs.add(umi)
    return
    
def getUMI(qname):


def correctedPosition(pos, cigar, strand):

    

def get_args():
    '''gets arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", default="testInput.sam")
    parser.add_argument("-u","--umi", default="STL96.txt")
    parser.add_argument("-o","--output", default="test.txt")
    parser.add_argument("-h", "--help")
    return parser.parse_args()

if __name__ == "__main__":
    args = get_args()
    deduplicate(args.input, args.output, args.umi)