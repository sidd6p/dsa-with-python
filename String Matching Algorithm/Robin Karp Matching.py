def compute_hash(string, base, prime_number):
    hash_value = 0

    for i in range(len(string)):
        char_value = ord(string[i])
        exp = len(string) - i - 1
        term = (char_value * pow(base, exp))
        hash_value += term
    
    return hash_value % prime_number

def rabin_karp(text,  pattern):
    base = 256
    prime_number = 101
    highest_term_scale = pow(base, len_pattern - 1)
    len_text = len(text)
    len_pattern = len(pattern)
    sols = []

    p_hash = compute_hash(pattern, base, prime_number)
    t_hash = compute_hash(text[:len_pattern], base, prime_number)

    for i in range(len_text - len_pattern + 1):
        if p_hash == t_hash:
            if all(text[i + j] == pattern[j] for j in range(len_pattern)):
                sols.append((i, i + len_pattern))
        if i + len_pattern < len_text:
            t_hash = (base * (t_hash - (ord(text[i]) * highest_term_scale) + ord(text[i + len_pattern]))) % prime_number
    
    return sols