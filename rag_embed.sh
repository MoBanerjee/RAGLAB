#!/bin/bash
#PBS -N ColbertEmbedding
#PBS -l select=1:ncpus=16:mem=256GB:ngpus=1
#PBS -l walltime=6:00:00
#PBS -j oe
#PBS -o A.log
#PBS -P personal-mohor001
#PBS -q normal

# Load modules and activate environment
module load miniforge3
module load cuda/11.8.0
module load git
conda activate /home/users/ntu/mohor001/.conda/envs/raglab


python RAGLAB_Project/RAGLAB/preprocess/colbert-wiki2023-preprocess/wiki2023_tsv-2-colbert_embedding.py
