def calculate_lps(self, pattern):
    lps = [0] * len(pattern)
    i, j = 1, 0

    while i < len(pattern):
        if pattern[i] == pattern[j]:
            j += 1
            lps[i] = j
            i += 1
        else:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    return lps


def kmp(text, pattern):
    M = len(pattern)
    N = len(text)
    lps = calculate_lps(pattern)

    i, j = 0, 0

    while (N - i) >= (M - j):
        if pattern[j] == text[i]:
            i += 1
            j += 1
            if j == M:
                print("Found pattern at index " + str(i - j))
                j = lps[j - 1]

        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1


print(kmp("ABABA", "ABA"))
