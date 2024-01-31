def brute_force(text, pattern):
    sols = []

    for i in range(len(text) - len(pattern) + 1):
        for j in range(len(pattern)):
            if text[i + j] != pattern[j]:
                break
            if j == len(pattern) - 1:
                sols.append((i, i + j))
    
    return sols