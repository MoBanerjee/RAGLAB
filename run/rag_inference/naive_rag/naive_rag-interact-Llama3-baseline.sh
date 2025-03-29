#!/bin/bash
#PBS -N ColbertEmbedding
#PBS -l select=1:ncpus=16:mem=256GB:ngpus=1
#PBS -l walltime=6:00:00
#PBS -j oe
#PBS -o aaa.log
#PBS -P personal-mohor001
#PBS -q normal

# Load modules and activate environment
module load miniforge3
module load cuda/11.8.0
export CUDA_VISIBLE_DEVICES=0

#pip install flash-attn --no-build-isolation --extra-index-url
module load git
conda activate /home/users/ntu/mohor001/.conda/envs/raglab

cd RAGLAB_Project/RAGLAB
python ./main-interact.py\
 --config ./config/naive_rag/naive_rag-interact-Llama3-baseline.yaml
