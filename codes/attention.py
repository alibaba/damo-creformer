import torch
import torch.nn as nn
import numpy as np
import math
from einops.layers.torch import Rearrange
from einops import rearrange
import torch.nn.functional as F

## compute the attention score on each regulatory element ##

def compute_selfattention(transformer_encoder, x, i_layer, d_model, num_heads):

    h = F.linear(x, transformer_encoder.layers[i_layer].self_attn.in_proj_weight, bias=transformer_encoder.layers[i_layer].self_attn.in_proj_bias)
    qkv = h.reshape(x.shape[0], x.shape[1], num_heads, 3 * d_model//num_heads)
    qkv = qkv.permute(0, 2, 1, 3)
    q, k, v = qkv.chunk(3, dim=-1)
    attn_logits = torch.matmul(q, k.transpose(-2, -1))
    d_k = q.size()[-1]
    attn_probs = attn_logits / math.sqrt(d_k)

    return attn_probs

def extract_selfattention_maps(transformer_encoder, x):
    attn_logits_maps = []
    attn_probs_maps = []
    num_layers = transformer_encoder.num_layers
    d_model = transformer_encoder.layers[0].self_attn.embed_dim
    num_heads = transformer_encoder.layers[0].self_attn.num_heads
    norm_first = transformer_encoder.layers[0].norm_first
    i=0
    h = x.clone()
    if norm_first:
        h = transformer_encoder.layers[i].norm1(h)
    attn_probs = compute_selfattention(transformer_encoder, h, i, d_model, num_heads)
    x = transformer_encoder.layers[i](x)
    
    return attn_probs
