def tokenizer (x, k):
    tok = ''
    i   = 0
    while i <= len(x)-k:
        for j in range (k):
            tok = tok + x[i+j]
        tok = tok + ' '
        i+=1
    return tok

def pre_processing (x, genome_dict):
    x = x.split()
    for i in range (len(x)):
        x[i] = genome_dict[x[i]]
        
    return x

def pre_pro (x, k):
    
    y = x.copy()
    
    x = x[:len(x)-k+1]
    
    for i in range (len(x)):
        
        x[i] = sum(y[i:i+k])/k
        
        if x[i]==0:
            x[i] = 1
            continue
        if x[i]>0 and x[i]<0.001:
            x[i] = 2  
            continue
        if x[i]>=0.001 and x[i]<0.01:
            x[i] = 3
            continue
        if x[i]>=0.01 and x[i]<0.1:
            x[i] = 4
            continue
        if x[i]>=0.1 and x[i]<0.125:
            x[i] = 5
            continue
        if x[i]>=0.125 and x[i]<0.15:
            x[i] = 6
            continue
        if x[i]>=0.15 and x[i]<0.2:
            x[i] = 7
            continue
        if x[i]>=0.2 and x[i]<0.3:
            x[i] = 8
            continue
        if x[i]>=0.3 and x[i]<0.4:
            x[i] = 9
            continue
        if x[i]>=0.4 and x[i]<0.5:
            x[i] = 10
            continue
        if x[i]>=0.5 and x[i]<0.6:
            x[i] = 11
            continue
        if x[i]>=0.6 and x[i]<0.7:
            x[i] = 12
            continue
        if x[i]>=0.7 and x[i]<0.8:
            x[i] = 13
            continue
        if x[i]>=0.8 and x[i]<0.9:
            x[i] = 14
            continue
        if x[i]>=0.9 and x[i]<1.0:
            x[i] = 15
            continue
        if x[i]>=1.0 and x[i]<2.0:
            x[i] = 16
            continue
        if x[i]>=2.0 and x[i]<3.0:
            x[i] = 17
            continue
        if x[i]>=3.0 and x[i]<4.0:
            x[i] = 18
            continue
        if x[i]>=4.0 and x[i]<5.0:
            x[i] = 19
            continue
        if x[i]>=5.0 and x[i]<6.0:
            x[i] = 20
            continue
        if x[i]>=6.0 and x[i]<7.0:
            x[i] = 21
            continue
        if x[i]>=7.0 and x[i]<8.0:
            x[i] = 22
            continue
        if x[i]>=8.0 and x[i]<9.0:
            x[i] = 23
            continue
        if x[i]>=9.0 and x[i]<10.0:
            x[i] = 24
            continue
        if x[i]>=10.0 and x[i]<11.0:
            x[i] = 25
            continue
        if x[i]>=11.0 and x[i]<12.0:
            x[i] = 26
            continue
        if x[i]>=12.0 and x[i]<13.0:
            x[i] = 27
            continue
        if x[i]>=13.0 and x[i]<14.0:
            x[i] = 28
            continue
        if x[i]>=14.0 and x[i]<15.0:
            x[i] = 29
            continue
        if x[i]>=15.0 and x[i]<20.0:
            x[i] = 30
            continue
        if x[i]>=20.0 and x[i]<25.0:
            x[i] = 31
            continue
        if x[i]>=25.0 and x[i]<35.0:
            x[i] = 32
            continue
        if x[i]>=35.0 and x[i]<55.0:
            x[i] = 33
            continue
        if x[i]>=55.0 and x[i]<100.0:
            x[i] = 34
            continue
        if x[i]>=100.0  and x[i]<200.0:
            x[i] = 35
            continue
        if x[i]>=200.0:
            x[i] = 36
            continue
    return x

def narrowPeak_Reader(path):
    f = open(path, encoding = "utf-8")
    E = f.read()
    E = E.split('\n')
    for i in range (len(E)):
        E[i] = E[i].split()
    
    return E

def value_fixer(CHR_value):
    
    for m in range (len(CHR_value)):
        if math.isnan(CHR_value[m]) == True:
            CHR_value[m]=0.0
            
    return CHR_value

def txt_Reader(path):
    f = open(path, encoding = "utf-8")
    E = f.read()
    E = E.split('\n')
    for i in range (len(E)):
        E[i] = E[i].split()[0]
    
    return E