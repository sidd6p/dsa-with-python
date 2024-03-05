def calculate_lps(pattern):
    lps = list()
    lps.append(0)
    current_match = 0
    i, j = 1, 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            current_match += 1
            j += 1
        else:
            current_match = 0
            j = 0
            if pattern[i] == pattern[j]:
                current_match += 1
                j += 1
        lps.append(current_match)
        i += 1
    return lps


def kmp(text, pattern):
    lps = calculate_lps(pattern)
    sols = list()
    i, j = 0, 0

    while i < len(text):
        if text[i] == pattern[j]:
            i += 1
            j += 1
            if j == len(pattern):
                sols.append(i - j)
                j = lps[j - 1]
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return sols


print(kmp("ABABA", "ABA"))
