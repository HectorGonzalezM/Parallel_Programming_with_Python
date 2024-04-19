# Pi Computation Project

This project includes three Python scripts designed to compute the value of π using numerical integration. Each script employs a different method: a single-threaded approach, a multi-processing approach, and a distributed computing approach using MPI.

## Scripts Description

1. **pure.py**: Computes π using a single-threaded numerical integration method.
2. **multi.py**: Utilizes Python's multiprocessing module to parallelize the computation of π.
3. **mpi_script.py**: Uses the mpi4py library to distribute the computation of π across multiple nodes in a cluster.

## Installation

To run these scripts, you need to have Python installed on your system. Python 3.6 or higher is recommended. You also need to install the necessary Python packages.

1. Clone this repository to your local machine.
   git clone git@github.com:HectorGonzalezM/Parallel_Programming_with_Python.git
   cd pi-computation-project

2. Install the required Python packages.
   pip install -r requirements.txt

## Usage

### Running the Single-threaded Script
python pure.py

### Running the Multi-processing Script
Ensure you are on a system that supports multiprocessing.
python multi.py

### Running the MPI-based Script
This script requires an MPI installation and is intended to be run on a cluster or a machine with MPI configured.
mpirun -n <number_of_processes> python3 mpi_script.py
Replace <number_of_processes> with the number of processes you want to use.

## Requirements

- Python 3.6+
- NumPy
- mpi4py (for mpi_script.py)
- A system with MPI installed (for mpi_script.py)
