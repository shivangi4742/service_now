from collections import defaultdict

# Read the input file and group the sentences by their prefix
sentences_by_prefix = defaultdict(list)
with open("input.txt", "r") as input_file:
    for line in input_file:
        prefix, sentence = line.strip().split(" ", 1)
        sentences_by_prefix[prefix].append(sentence)

# Find groups of similar sentences and extract the changing word

groups = []
for prefix, sentences in sentences_by_prefix.items():
    groups_by_sentence = defaultdict(list)
    # print(sentences)
    for sentence in sentences:
        prefix, pattern = sentence.split(" ", 1)
        groups_by_sentence[pattern].append(prefix)

    for pattern, prefixes in groups_by_sentence.items():
        if len(prefixes) >=1:
            changing_word = pattern.split()
            groups.append((prefixes, pattern, changing_word))


# Output the results to a file
with open("output.txt", "w") as output_file:
    ouptut = []
    for group in groups:
        prefixes, pattern, changing_word = group
        for prefix in prefixes:
            output_file.write(prefix + " " + str(pattern) + "\n")
            ouptut.append(prefix)
    output_file.write("The changing word was: " + ",".join(ouptut) + "\n")