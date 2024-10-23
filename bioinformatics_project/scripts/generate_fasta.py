import random
import textwrap 

def generate_random_dna(pairs):
    seq = []
    while pairs != 0:
        seq.append(random.choice('ACGT')) 
        pairs -= 1
    return ''.join(seq)

def write_file(seq,name):
    with open(name,'w') as f:
        newseq= textwrap.fill(seq, width=80)
        f.write(newseq)


if __name__ == "__main__":
    seq = generate_random_dna(1000000)
    write_file(seq,'bioinformatics_project/data/random_sequence.fasta')
    print('Random DNA sequence generated and saved to bioinformatics_project/data/random_sequence.fasta')
