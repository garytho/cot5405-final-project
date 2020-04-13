import math

def lemma_one(T, ell, p, m):
    number_iter =  math.ceil(1.0 * ell / m)

    our_string = T[max(0, p - ell + 1) : p + ell]
        
    i = 0
        
    string_batch = []
        
    while i + ell <= len(our_string):
        string_batch.append(our_string[i : i + ell])
        i += 1
        
        
    hash_batch = [pattern_hash(x, ell) for x in string_batch] 
        
    final_output = [rabin_karp_pm(T, ell, hash_batch[x], string_batch[x]) for x in range(len(string_batch))]


    if False in final_output:
        return True
    
    else:
        return False

        
def pattern_hash(P, ell):
    #compute the hash of a given pattern
    p = 0
    q = 7103 # our prime number
    d = 256
    for i in range(ell):
        p = (d * p + ord(P[i]))% q 
    return p


def rabin_karp_pm(T, ell, hashed, P):
    #perform rabin karp pattern matching given a hash of the current pattern P

    occ = 0

    t = 0
    q = 7103 # our prime number
    d = 256
    
    h = 1
    for i in range(ell - 1): 
        h = (h * d)% q 
    
    for i in range(ell):
        t = (d * t + ord(T[i]))% q
        
        
    for idx in range(len(T) - ell + 1):
        
        if i < len(T) - ell: 
            t = (d*(t-ord(T[i])*h) + ord(T[i +ell]))% q 
  
            if t < 0: 
                t = t + q 

    for i in range(len(T) - ell + 1):
        if T[i: i + ell] == P:
            occ += 1
            
    if occ > 1:
        return True
    
    else:
        return False



def exponential_search(Pattern, Text, p, m):
    ell = 1
    
    ell_low = 1
    
    ell_up = -1
    
    
    while True:
        
        if ell_low == ell_up:
            return ell_low
        
        lem1_output = lemma_one(Text, ell, p, m)
        
        if not lem1_output and ell_up == -1:
            new_ell = min(ell * 2, len(Text))
            ell_low = ell
            ell = new_ell
            
        elif not lem1_output and ell_up > 0:
            ell_low = ell
            new_ell = ell_low + (ell_up - ell_low) // 2
            ell = new_ell

        elif lem1_output:
            ell_up = ell
            new_ell = ell_low + (ell_up - ell_low ) // 2
            ell = new_ell


            

