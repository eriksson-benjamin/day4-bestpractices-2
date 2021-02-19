from mpi4py import MPI
import numpy as np

comm = MPI.COMM_WORLD
rank = comm.Get_rank()

# Get number of processes
n_procs = comm.Get_size()
random_number = np.zeros(1)

# Generate random numbers and send to rank 0
if rank != 0:
    for r in range(n_procs):     
        if rank == r:
            random_number = np.random.random_sample(1)[0]
            print(f'Rank {r} generated random number: {random_number:.2f}')
            comm.Send(random_number, dest = 0)

# Receive random numbers and sum them
if rank == 0:
    summed_numbers = 0
    for r in range(1, n_procs):
        comm.Recv(random_number, source = r)
        print(f'Rank 0: source = {r}, random number = {random_number[0]:.2f}')
        summed_numbers += random_number
    
    print(f'Summed random numbers: {summed_numbers[0]:.2f}')