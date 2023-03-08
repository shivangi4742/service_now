def parse_input_file(file_path):
    sentences = []
    with open(file_path, "r") as f:
        for line in f:
            date , timestamp, sentence = line.strip().split(" ", 2)
            name, actions = sentence.split(" is ")
            action, actioner = actions.split(" into the ")
            sentences.append({"timestamp": date + timestamp, "name": name, "action": action, "actioner": actioner})
    return sentences

def group_sentences_by_name(sentences):
    name = {}
    for sentence in sentences:
        if sentence["name"] in name:
            name[sentence["name"]].append({"action": sentence["action"], "timestamp": sentence["timestamp"]})
        else:
            name[sentence["name"]] = [{"action": sentence["action"], "timestamp": sentence["timestamp"]}]
    return name

def group_sentences_by_values(sentences):
    v = {}
    for sentence in sentences:
        if sentence["actioner"] in v:
            v[sentence["actioner"]].append({'name' : sentence["name"],"action": sentence["action"], "timestamp": sentence["timestamp"]})
        else:
            v[sentence["actioner"]] = [{'name' : sentence["name"],"action": sentence["action"], "timestamp": sentence["timestamp"]}]
    return v


def group_sentences_by_action(sentences):
    actions = {}
    for sentence in sentences:
        if sentence["action"] in actions:
            actions[sentence["action"]].append({"name": sentence["name"], "timestamp": sentence["timestamp"]})
        else:
            actions[sentence["action"]] = [{"name": sentence["name"], "timestamp": sentence["timestamp"]}]
    return actions


sentences = parse_input_file("input.txt")
name = group_sentences_by_name(sentences)
actions = group_sentences_by_action(sentences)
actioners  = group_sentences_by_values(sentences)

with open("output.txt", "w") as f:
    for sentence in sentences:
        f.write(sentence["timestamp"] + " " + sentence["name"]  + " " + sentence["action"] + " " +sentence["actioner"]+ "\n")
    if (len(name.keys())> 1):
        f.write(f"The changing words was: {', '.join(sorted(name))}\n")
    elif (len(actions.keys())>1):
        f.write(f"The changing words was: {', '.join(sorted(actions))}\n")
    elif (len(actioners.keys())>1):
        f.write(f"The changing words was: {', '.join(sorted(actioners))}\n")
        
