import torch
from profilehooks import profile


@profile(filename='gpu_test.prof', stdout=False)
def compute_big_sum(tensor: torch.Tensor):
    # do a bunch of expensive computations, that all output a single number
    a = tensor.sum()
    b = tensor.pow(2).sum()
    c = tensor.sqrt().sum()

    sum_all = a + b + c
    sum_all_cpu = sum_all.cpu()  # move the value to CPU memory

    # return a sum of all the operations (scalar)
    return sum_all_cpu


if __name__ == '__main__':
    # Create a big matrix of random number, already in GPU memory
    X = torch.rand((10000, 10000), dtype=torch.float64, device='cuda:0')
    res = compute_big_sum(X)

    print(float(res))