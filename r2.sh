#!/bin/bash
# Exercise 2 submission script - submit.sh
# Below, is the queue
#PBS -q normal
#PBS -j oe
#PBS -l select=1:ncpus=16:ngpus=2
#PBS -l walltime=06:00:00
#PBS -N a
module load miniforge3
#conda activate raglab
#python RAGLAB_Project/RAGLAB/alltgt.py
