#!/bin/bash
# Exercise 2 submission script - submit.sh
# Below, is the queue
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=2
#PBS -l walltime=06:00:00
#PBS -N mo
module load miniforge3
conda activate raglab
huggingface-cli login --token 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
#huggingface-cli download neuralmagic/Meta-Llama-3.1-8B-Instruct-quantized.w8a16 --local-dir RAGLAB/model/generator/Llama3-8B-baseline
#huggingface-cli download meta-llama/Llama-3.1-8B-Instruct --local-dir modellama/lama
huggingface-cli download colbert-ir/colbertv2.0 --local-dir RAGLAB/model/retriever/colbertv2.0
