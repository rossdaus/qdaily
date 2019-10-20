def find_anagrams(w, s):
    """Find starting indices of anagram of w in s."""
    indices = []
    for n, letter in enumerate(s):
        if letter in w:
            # Try anagram match
            if sorted(s[n:n + len(w)]) == sorted(w):
                indices.append(n)
    return indices

s = "abxaba"
w = "ab"
print(find_anagrams(w, s))
# Returns [0, 3, 4]
