def find_anagrams(w, s):
    """Find starting indices of anagram of w in s."""
    indices = []
    anlength = len(w)
    sorted_word = sorted(w)
    for n, letter in enumerate(s):
        if letter in w:
            # Try anagram match
            attempt = s[n:n + anlength]
            if sorted(attempt) == sorted_word:
                indices.append(n)
    return indices

s = "abxaba"
w = "ab"
print(find_anagrams(w, s))
# Returns [0, 3, 4]
