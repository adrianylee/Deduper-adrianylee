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

    with open(input_sam, "r") as fi:
        with open(output_sam, "w") as fo:
            for line in fi:

                if line.startswith("@"):
                    fo.write(line)
                    continue

                record = line.rstrip("\n").split("\t")

                origQNAME = record[0]
                QNAME = record[0]
                FLAG = int(record[1])
                RNAME = record[2]
                POS = int(record[3])
                CIGAR = record[5]

                if FLAG & 4:
                    fo.write(line)
                    counts += 1
                    continue

                if RNAME != current:
                    current = RNAME
                    seen.clear()

                umi = getUMI(QNAME)

                if umi not in validUMIs:
                    invalidUMI += 1
                    continue

                if FLAG & 16:
                    strand = "reverse"
                else:
                    strand = "forward"

                corrected_position = correctedPosition(POS, CIGAR, strand)    

                isItDuplicate = [RNAME, strand, umi, corrected_position]

                if isItDuplicate in seen:
                    duplicates += 1
                    continue

                seen.add([RNAME, strand, umi, corrected_position])
                output_sam.write(origQNAME, current, strand, umi, corrected_position)
                counts += 1

        fo.close()
    fi.close()

    return
    
def getUMI(qname):
    fields = qname.split(":")
    return fields[-1]

def correctedPosition(pos, cigar, strand):
    CIGARsets = []
    current = ""

    print(f"POS: {pos}, CIGAR: {cigar}, Strand: {strand}")

    for character in cigar:
        if character.isdigit():

            current += character
        else:
            CIGARsets.append([int(current), character])
            current = ""

    leading = 0
    trailing = 0

    referenceLength = 0

    for length, operation in CIGARsets:

        if operation == "H":
            continue
        if operation == "S":
            leading = length
        break

    for length, operation in reversed(CIGARsets):
        if operation == "H":

            continue
        if operation == "S":
            trailing = length
        break

    for length, operation in CIGARsets:
        if operation in "MDN=X":
            referenceLength += length

    if strand == "forward":
        corrected = pos - leading
        print(f"forward: {pos} - {leading} = {corrected}")
    else:
        corrected = pos + referenceLength - 1 + trailing
        print(f"rev: {pos} + {referenceLength} - 1 + {trailing} = {corrected}")

    return pos + referenceLength - 1 + trailing    
    

def get_args():
    '''gets arguments'''
    parser = argparse.ArgumentParser()
    parser.add_argument("-f","--file", default="testInput.sam")
    parser.add_argument("-u","--umi", default="STL96.txt")
    parser.add_argument("-o","--output", default="test.txt")
    parser.add_argument("-h", "--help")
    return parser.parse_args()

if __name__ == "__main__":

    #correctedPosition(100, "50M", "forward")
    #correctedPosition(100, "50M", "reverse")
    #correctedPosition(100, "5S45M", "forward")
    #correctedPosition(100, "45M5S", "reverse")
    #correctedPosition(100, "5S20M2I10M3D15M4S", "forward")
    #correctedPosition(100, "5S20M2I10M3D15M4S", "reverse")
    #correctedPosition(100, "5H5S45M", "forward")
    #correctedPosition(100, "45M5S5H", "reverse")

    args = get_args()
    deduplicate(args.input, args.output, args.umi)