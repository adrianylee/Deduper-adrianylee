#!/bin/bash
#SBATCH --account=bgmp                    # REQUIRED: which account to use
#SBATCH --partition=bgmp                  # REQUIRED: which partition to use
#SBATCH --cpus-per-task=8                 # optional: number of cpus, default is 1
#SBATCH --mem=16GB                        # optional: amount of memory, default is 4GB per cpu
#SBATCH --job-name=deduper                # optional: job name
#SBATCH --output=/projects/bgmp/aylee/bioinfo/Bi624/Deduper/20261101_deduper.%j.out

cd /projects/bgmp/aylee/bioinfo/Bi624/Deduper

/usr/bin/time -v samtools sort /projects/bgmp/shared/deduper/C1_SE_uniqAlign.sam \
    -o /projects/bgmp/aylee/bioinfo/Bi624/Deduper/C1_SE_uniqAlign.sorted.sam 

/usr/bin/time -v python /projects/bgmp/aylee/bioinfo/Bi624/Deduper/deduper.py \
    -u /projects/bgmp/aylee/bioinfo/Bi624/Deduper/STL96.txt \
    -f /projects/bgmp/aylee/bioinfo/Bi624/Deduper/C1_SE_uniqAlign.sorted.sam \
    -o /projects/bgmp/aylee/bioinfo/Bi624/Deduper/DEDUPED.C1_SE_uniqAlign.sorted.sam