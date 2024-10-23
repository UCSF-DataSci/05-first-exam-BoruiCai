#!/bin/bash
mkdir -p bioinformatics_project/data bioinformatics_project/scripts bioinformatics_project/results
touch bioinformatics_project/scripts/generate_fasta.py bioinformatics_project/scripts/dna_operations.py bioinformatics_project/scripts/find_cutsites.py
touch bioinformatics_project/results/cutsite_summary.txt
touch bioinformatics_project/data/random_sequence.fasta
echo 'Bioinformatics Project: data, scripts, results' > bioinformatics_project/README.md
echo "Project directory structure created successfully:"
ls -R bioinformatics_project