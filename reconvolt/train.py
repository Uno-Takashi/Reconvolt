import torch

from conformer import *

pre_dim=2^10^10
block = ConformerBlock(
    dim =pre_dim,
    dim_head = 64,
    heads = 8,
    ff_mult = 4,
    conv_expansion_factor = 2,
    conv_kernel_size = 512-1,
    attn_dropout = 0.,
    ff_dropout = 0.,
    conv_dropout = 0.
)

print(block)