key = [" into the ", " at a " ]

original_sentence= []
def parse_input_file(file_path):
    sentences = []
    with open(file_path, "r") as f:
        for line in f:
            original_sentence.append(line)
            date , timestamp, sentence = line.strip().split(" ", 2)
            name, actions = sentence.split(" is ")
            half_prefix = actions.split(key[0])
            if(len(half_prefix) > 1):
                action, actioner = actions.split(key[0])
            else:
                action, actioner = actions.split(key[1])
            
            sentences.append({"timestamp": date + timestamp, "name": name, "action": action, "actioner": actioner})
    return sentences



def group_sentences_by_action(sentences, k):
    actions = {}
    for sentence in sentences:
        if sentence[k] in actions:
            actions[sentence[k]].append({ "timestamp": sentence["timestamp"]})
        else:
            actions[sentence[k]] = [{ "timestamp": sentence["timestamp"]}]
    return actions


sentences = parse_input_file("input.txt")
name = group_sentences_by_action(sentences, 'name')
actions = group_sentences_by_action(sentences, 'action')
actioners  = group_sentences_by_action(sentences, 'actioner')



with open("output.txt", "w") as f:
    for sentence in original_sentence:
        f.write(f"{sentence}  \n")
    if (len(name.keys())> 1):
        f.write(f"The changing words was: {', '.join(sorted(name))}\n")
    elif (len(actions.keys())>1):
        f.write(f"The changing words was: {', '.join(sorted(actions))}\n")
    elif (len(actioners.keys())>1):
        f.write(f"The changing words was: {', '.join(sorted(actioners))}\n")
        
