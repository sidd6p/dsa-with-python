def calculate_z(string):
    left, right, idx = 0, 0, 1
    z = [0] * len(string)

    while idx < len(z):
        if idx > right:
            left, right = idx, idx
            while right < len(z) and string[right] == string[right - left]:
                right += 1
            z[idx] = right - left
            right -= 1
        else:
            if z[idx - left] >= right - idx + 1:
                left = idx
                while right < len(string) and string[right] == string[right - left]:
                    right += 1
                z[idx] = right - left
                right -= 1
            else:
                z[idx] = z[idx - left]
        idx += 1

    return z


def search_pattern(text, pattern):
    string = pattern + "$" + text
    z = calculate_z(string)

    for idx in range(len(string)):
        if z[idx] == len(pattern):
            print(f"Pattern found at index: {idx - len(pattern) - 1}")


search_pattern("GEEKS FOR GEEKS", "GEEK")
