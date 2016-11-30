import itertools

_word_points_dict = {
    'a': 1,
    'e': 1,
    'i': 1,
    'o': 1,
    'u': 1,
    'l': 1,
    'n': 1,
    's': 1,
    't': 1,
    'r': 1,
    'd': 2,
    'g': 2,
    'b': 3,
    'c': 3,
    'm': 3,
    'p': 3,
    'f': 4,
    'h': 4,
    'v': 4,
    'w': 4,
    'y': 4,
    'k': 5,
    'j': 8,
    'x': 8,
    'q': 10,
    'z': 10
}

def word_points(w):
    return sum([_word_points_dict[c] for c in w])

def combine_dicts(f1, f2, out_f):
    with open(f1, 'r') as f1:
        with open(f2, 'r') as f2:
            words = list(set([l.strip().lower() for l in f1] + [l.strip().lower() for l in f2]))
            words.sort()

            with open(out_f, 'w') as out_f:
                for w in words:
                    out_f.write(w)
                    out_f.write('\n')

def get_dictionary(filename):
    with open(filename, 'r') as f:
        words = [l.strip().lower() for l in f]
        return set(words)

def find_words(letters, dictionary):
    valid_words = set(["".join(perm)
                       for i in range(1, len(letters) + 1)
                       for comb in itertools.combinations(letters, i)
                       for perm in itertools.permutations(comb) if "".join(perm) in dictionary])

    sorted_words = sorted(list(valid_words), key=word_points)

    return sorted_words
