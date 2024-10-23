import argparse

def complement(sequence):
    seq = []
    sequence = sequence.upper()
    dic_com ={'A' :'T','C':'G','G':'C','T':'A'} 
    for i in sequence:
        seq.append(dic_com[i])
    return ''.join(seq)

def reverse(sequence):
    sequence = sequence.upper()
    return sequence [::-1]

def reverse_complement(sequence):
    new = reverse(sequence)
    return complement(new)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("sequence", type=str, help="sequence")
    args = parser.parse_args()
    seq = args.sequence
    try:
        print(f"Original sequence: {seq}")
        print(f'Complement: {complement(seq)}')
        print(f'Reverse: {reverse(seq)}')
        print(f'Reverse complement: {reverse_complement(seq)}')
    except IOError:
        print('wrong!')
