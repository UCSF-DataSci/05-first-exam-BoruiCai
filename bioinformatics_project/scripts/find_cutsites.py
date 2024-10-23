import argparse

def read_file(name):
    with open(name,'r') as f:
        text= f.read()
        text.replace(' ','')
    return text

def find_cut(seq,cutsite):
    cut = cutsite.index('|')
    cutsite = cutsite.replace('|','')
    cutposition = []
    for i in range(len(seq)):
        if seq[i:i+len(cutsite)] == cutsite:
            cutposition.append(i + cut)
    return  cutposition

def find_pair(cutposition):
    final = []
    for i in range(len(cutposition)):
        for k in range(i+1,len(cutposition)):
            distance = cutposition[k] - cutposition[i]
            if 80000 <= distance <= 120000:
                final.append((cutposition[i], cutposition[k]))
    return final

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("filename", type=str, help="filename")
    parser.add_argument("cutsite", type=str, help="cutsite")
    
    args = parser.parse_args()
    
    with open(args.filename, 'r') as f:
        text = f.read().replace(' ', '').replace('\n', '')

    cut = find_cut(text,args.cutsite)
    pair = find_pair(cut)

    print(f'Analyzing cut site: {args.cutsite} \n')
    print(f'Total cut sites found: {len(cut)} \n')
    print(f'Cut site pairs 80-120 kbp apart: {len(pair)} \n')
    print('First 5 pairs: \n')
    count = min(5, len(pair))  
    for i in range(count): 
        p1 = pair[i][0]  
        p2 = pair[i][1]  
        print(f'{i + 1}. {p1} - {p2}') 
    

    output_file = "bioinformatics_project/results/cutsite_summary.txt"
    with open(output_file, 'w') as f:
        f.write(f'Analyzing cut site: {args.cutsite} \n')
        f.write(f'Total cut sites found: {len(cut)} \n')
        f.write(f'Cut site pairs 80-120 kbp apart: {len(pair)} \n')
        for ii in range(len(pair)): 
            p1 = pair[ii][0]  
            p2 = pair[ii][1]  
            f.write(f'{ii + 1}. {p1} - {p2} \n') 

    print('Results saved to bioinformatics_project/results/distant_cutsite_summary.txt')
    


