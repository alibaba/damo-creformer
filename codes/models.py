import pandas as pd
import torch
from torch import nn
from einops.layers.torch import Rearrange
from einops import rearrange
import math

class AttentionPool(nn.Module):
    def __init__(self, dim, pool_size = 8):
        super().__init__()
        self.pool_size = pool_size
        self.pool_fn = Rearrange('b d (n p) -> b d n p', p = pool_size)

        self.to_attn_logits = nn.Conv2d(dim, dim, 1, bias = False)

        nn.init.dirac_(self.to_attn_logits.weight)

        with torch.no_grad():
            self.to_attn_logits.weight.mul_(2)

    def forward(self, x):
        b, _, n = x.shape
        remainder = n % self.pool_size
        needs_padding = remainder > 0

        if needs_padding:
            x = F.pad(x, (0, remainder), value = 0)
            mask = torch.zeros((b, 1, n), dtype = torch.bool, device = x.device)
            mask = F.pad(mask, (0, remainder), value = True)

        x = self.pool_fn(x)
        logits = self.to_attn_logits(x)

        if needs_padding:
            mask_value = -torch.finfo(logits.dtype).max
            logits = logits.masked_fill(self.pool_fn(mask), mask_value)

        attn = logits.softmax(dim = -1)

        return (x * attn).sum(dim = -1)
    
class DNA_Embedding(nn.Module):
    
    def __init__(self):
        super(DNA_Embedding, self).__init__()
        dim = 2048
        self.dna_embed = nn.Embedding(4100, dim)
        
    def forward(self, DNA):
        
        Genome_embed   = self.dna_embed(DNA)
        
        return Genome_embed
    
class Sig_Embedding(nn.Module):
    
    def __init__(self):
        super(Sig_Embedding, self).__init__()
        dim = 2048
        self.sig_embed   = nn.Embedding(38, dim)
        
    def forward(self, signal):

        signal_embed  = self.sig_embed(signal)
        
        return signal_embed
    
class Encoder(nn.Module):
    def __init__(self, d_model=2048, batch_first=True, nhead=32, dim_ffn=2048*4, num_layer=20, drop=0, LNM=1e-05):
        super(Encoder, self).__init__()
        self.norm = nn.LayerNorm(d_model)
        self.encoder_layer = nn.TransformerEncoderLayer(
                         d_model=d_model, nhead=nhead,
                         dim_feedforward=dim_ffn,
                         batch_first=True,dropout=drop, layer_norm_eps=LNM)
        self.encoder = nn.TransformerEncoder(
                         self.encoder_layer,
                         num_layers=num_layer)

    def forward(self, x):
        output = self.encoder(self.norm(x))
        return output
    
class Encoder1(nn.Module):
    def __init__(self, d_model=2048, batch_first=True, nhead=32, dim_ffn=2048*4, num_layer=20, drop=0, LNM=1e-05):
        super(Encoder1, self).__init__()
        self.norm = nn.LayerNorm(d_model)
        self.encoder_layer = nn.TransformerEncoderLayer(
                         d_model=d_model, nhead=nhead,
                         dim_feedforward=dim_ffn,
                         batch_first=True,dropout=drop, layer_norm_eps=LNM)
        self.encoder = nn.TransformerEncoder(
                         self.encoder_layer,
                         num_layers=num_layer)

    def forward(self, x):
        output = self.encoder(self.norm(x))
        return output
    
class Pos_L1_Embed(nn.Module):
    
    def __init__(self):
        super(Pos_L1_Embed, self).__init__()
        dim = 2048
        self.pos_embed   = nn.Embedding(130, dim)
    
    def forward(self, Position):
        
        position_embed = self.pos_embed(Position)
        
        return position_embed
    
class Pos_L2_Embed(nn.Module):
    
    def __init__(self):
        super(Pos_L2_Embed, self).__init__()
        dim = 2048
        self.pos_embed   = nn.Embedding(129, dim)
    
    def forward(self, Position):
        
        position_embed = self.pos_embed(Position)
        
        return position_embed
    
class Pos_L3_Embed(nn.Module):

    def __init__(self, max_len):
        super(Pos_L3_Embed, self).__init__()
        dim = 2048
        self.pos_embed   = nn.Embedding(max_len, dim)

    def forward(self, Position):

        position_embed = self.pos_embed(Position)

        return position_embed
    
class ANN(nn.Module):
    def __init__(self):
        super(ANN, self).__init__()
        self.l1 = nn.Linear(1 * 150 * 2048 , 32)
        self.l2 = nn.Linear(32 , 1)
        self.act= nn.ReLU()

    def forward(self, x1):
        x1 = x1.view(-1, 1 * 150 * 2048)
        x1 = self.act(self.l1(x1))
        x2 = self.l2(x1)

        return x2