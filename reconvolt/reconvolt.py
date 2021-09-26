import torch
from torch import nn

class Reconvolt(nn.Module):

    def __init__(self,*,dim,dim_head = 64,heads = 8,ff_mult = 4,conv_expansion_factor = 2,conv_kernel_size = 31,attn_dropout = 0.,ff_dropout = 0.,conv_dropout = 0.):
        super(Reconvolt, self).__init__()

    def forward(self, x):
        nn.Embended(x)


        x = nn.Sigmoid(x)
        return x