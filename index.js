function read_file(filename) {
  const fs = require('fs');
  const lines = fs.readFileSync(filename, 'utf-8').split('\n');
  return lines.map(line => line.split(' ', 3));
}

function group_tuples(tuples) {
  const groups = {};
  tuples.forEach(tup => {
    if (groups[tup[2]]) {
      groups[tup[2]].push(tup);
    } else {
      groups[tup[2]] = [tup];
    }
  });
  return groups;
}

function extract_changes(group) {
  const names = new Set(group.map(tup => tup[1]));
  const activities = new Set(group.map(tup => tup[2]));
  return [names, activities];
}

function write_output(filename, groups) {
  const fs = require('fs');
  const stream = fs.createWriteStream(filename);

  Object.entries(groups).forEach(([activity, group]) => {
    group.sort((tup1, tup2) => {
      const datetime1 = new Date(`${tup1[0]} ${tup1[1]}`);
      const datetime2 = new Date(`${tup2[0]} ${tup2[1]}`);
      return datetime1 - datetime2;
    });

    const [names, activities] = extract_changes(group);

    group.forEach(tup => {
      const line = `${tup[0]} ${tup[1]} ${tup[2]} ${activity}\n`;
      stream.write(line);
    });

    const activityList = [...activities].join(', ');
    const namesList = [...names].join(', ');

    stream.write(`The changing word was: ${activityList}\n`);
    stream.write(`${namesList}\n\n`);
  });

  stream.end();
}

const input_file = 'input.txt';
const output_file = 'output.txt';
const tuples = read_file(input_file);
const groups = group_tuples(tuples);
write_output(output_file, groups);
