#!/bin/bash
#SBATCH --account=bgmp                    # REQUIRED: which account to use
#SBATCH --partition=bgmp                  # REQUIRED: which partition to use
#SBATCH --cpus-per-task=8                 # optional: number of cpus, default is 1
#SBATCH --mem=16GB                        # optional: amount of memory, default is 4GB per cpu
#SBATCH --job-name=deduper                # optional: job name
#SBATCH --output=/projects/bgmp/aylee/bioinfo/Bi624/Deduper/20261101_deduper.%j.out

/usr/bin/time -v samtools sort /projects/bgmp/shared/deduper/C1_SE_uniqAlign.sam -o C1_SE_uniqAlign.sorted.sam 
/user/bin/time -v deduper.py -f C1_SE_uniqAlign.sorted.sam -u STL96.txt -o DEDUPED.C1_SE_uniqAlign.sorted.sam