from mpi4py import MPI

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
print(f'Hello World from process {rank}')
