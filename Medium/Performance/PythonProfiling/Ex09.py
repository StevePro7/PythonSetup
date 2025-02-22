def compute_big_sum(tensor: torch.Tensor):
    a = tensor.sum()
    b = tensor.pow(2).sum()
    c = tensor.sqrt().sum()

    sum_all = a + b + c
    torch.cuda.synchronize()  # add this after all your GPU operations
    # to ensure correct time measurements
    sum_all_cpu = sum_all.cpu()

    return sum_all_cpu