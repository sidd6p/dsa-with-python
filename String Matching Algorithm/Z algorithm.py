def calculate_z(s):
    left, right, idx = 0, 0, 1
    z = [0] * len(s)

    while idx < len(s):
        if idx > right:
            left, right = idx, idx
            while right < len(s) and s[right] == s[right - idx]:
                right += 1
            z[idx] = right - idx
            right -= 1
        else:
            if z[idx - left] >= right - idx + 1:
                left = idx
                while right < len(s) and s[right] == s[right - idx]:
                    right += 1
                z[idx] = right - idx
                right -= 1
            else:
                z[idx] = z[idx - left]
        idx += 1

    return z


def search_pattern(text, pattern):
    string = pattern + "$" + text
    z = calculate_z(string)
    print(z)

    for idx in range(len(string)):
        if z[idx] == len(pattern):
            print(f"Pattern found at index: {idx - len(pattern) - 1}")


search_pattern("GEEKS FOR GEEKS", "GEEK")
