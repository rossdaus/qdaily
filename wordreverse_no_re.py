def solve(text, delimiters):
    """Reverse order of words in text, keeping delims in place."""

    def is_word(chars):
        """Return True if chars countains no delimiters."""
        return not any((c in delimiters for c in chars))

    tokens = []  # a token is either a word or delimiter(s)
    cur_token = ""

    for char in text:
        # add character to cur_token if we havent encountered a new token
        if not cur_token or is_word(char) == is_word(cur_token):
            cur_token += char

        else: # start collecting next token
            tokens.append(cur_token)
            cur_token = char

    tokens.append(cur_token)  # append the last token

    # Get all words and their positions
    wordpos = [(n, w) for n, w in enumerate(tokens) if is_word(w)]
    word_positions, words = zip(*wordpos)  # unbind to two lists

    words = reversed(words)  # reverse word list

    for p in word_positions:  # substitute words using the reverse wordlist
        tokens[p] = next(words)

    return "".join(tokens)

for i in ("hello/world:here", "hello/world:here/", "hello//world:here"):
    answer = solve(i, delimiters = {"/", ":"})
    print(i, " --> ", answer)
