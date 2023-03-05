from collections import defaultdict

# Read the input file and group the sentences by their prefix
_sentencesByPrfix = defaultdict(list)
with open("input.txt", "r") as input_file:
    for _line in input_file:
        _prefix, _sentence = _line.strip().split(" ", 1)
        _sentencesByPrfix[_prefix].append(_sentence)

# Find groups of similar sentences and extract the changing word

groups = []
for _prefix, _sentences in _sentencesByPrfix.items():
    groups_by_sentence = defaultdict(list)
    # print(sentences)
    for sentence in _sentences:
        _prefix, _pattern = sentence.split(" ", 1)
        groups_by_sentence[_pattern].append(_prefix)

    for _pattern, _prefixes in groups_by_sentence.items():
        if len(_prefixes) >=1:
            _changing_word = _pattern.split()
            groups.append((_prefixes, _pattern, _changing_word))


# Output the results to a file
with open("output.txt", "w") as output_file:
    ouptut = []
    for group in groups:
        prefixes, pattern, changing_word = group
        for prefix in prefixes:
            output_file.write(prefix + " " + str(pattern) + "\n")
            ouptut.append(prefix)
    output_file.write("The changing word was: " + ",".join(ouptut) + "\n")
