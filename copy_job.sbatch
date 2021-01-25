#!/bin/bash

#SBATCH --nodes=1
#SBATCH --account=ucb164_summit1
#SBATCH --time=10:00:00
#SBATCH --qos=normal
#SBATCH --partition=shas
#SBATCH --ntasks=1

#SBATCH --job-name=MERRA2
#SBATCH --output=./sbatch_out_files/%x.%j.out
#SBATCH --mail-type=ALL
#SBATCH --mail-user=eric.keenan@colorado.edu

bash copy.sh

