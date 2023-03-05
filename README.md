# service_now
Private Investigator
You have a file describing the notes of a private investigator following his target.
The file has many sentences, ordered by time, one in a row.
To write his report, the private investigator uses consistent phrasing to describe what is
going on. Only one word can change in a specific phrase/pattern.
The input may look like:
01-01-2012 19:45:00 Naomi is getting into the car
01-01-2012 20:12:39 Naomi is eating at a restaurant
02-01-2012 09:13:15 George is getting into the car
02-01-2012 10:14:00 George is eating at a diner
03-01-2012 10:15:00 Naomi is eating at a diner
03-01-2012 11:22:40 Mike is getting into the car
03-01-2012 12:52:23 Mike is getting into the office
04-01-2012 21:55:05 Naomi is running into the car
Your task is to write code that groups together similar sentences (sentences where only
a single word differ between them) and extracts the changes, then outputs them to a file
in the following format:
01-01-2012 19:45:00 Naomi is getting into the car
02-01-2012 09:13:15 George is getting into the car
03-01-2012 11:22:40 Mike is getting into the car
The changing word was: Naomi, George, Mike
02-01-2012 10:14:00 George is eating at a diner
03-01-2012 10:15:00 Naomi is eating at a diner
The changing word was: Naomi, George
01-01-2012 20:12:39 Naomi is eating at a restaurant
03-01-2012 10:15:00 Naomi is eating at a diner
The changing word was: restaurant, diner
03-01-2012 11:22:40 Mike is getting into the car
03-01-2012 12:52:23 Mike is getting into the office
The changing word was: car, office
01-01-2012 19:45:00 Naomi is getting into the car
04-01-2012 21:55:05 Naomi is running into the car
The changing word was: getting, running
When done, please answer the following questions in your README file:
1. What can you say about the complexity of your code?
2. How will your algorithm scale?
3. If you had two weeks to do this task, what would you have done differently? What
would be better?
Q&A:
- Q: Can I assume the timestamp is unique?
A: Yes
- Q: Can I assume 2 identical sentences with 1 extra word in one of them are not
similar?
03-01-2012 11:22:40 Mike is getting into the car
04-01-2012 09:12:30 Mike is getting into the blue car
A: Yes
- Q: One sentence can be similar to multiple sentences?
A: Yes, and all of them need to show in the final output
- Q: Can I assume that all the file structure can be loaded into the memory?
A: Yes
- Q: Do I need to create a simple UI with input parameters
A: No
- Q: Can I use case insensitive comparison?
A: Yes
- Q: Can I assume there are no special characters, or can I ignore special
characters
A: Yes
What’s important to us:
- Good code structure – the way you modularize the application should make good
sense.
- Good Algorithm – your algorithm should be performant and readable.
What’s not important:
- Unit tests.
- Using Spring Framework, Dependency Injection or anything that adds unneeded
complication. Focus on the task, write a focused, minimal solution.
Please upload your code to GitHub and attach a README file that includes instructions
on how to run your program and the answers to the open questions.
A suggested format for the README file:
Overview of the solution:
…
How to run?
…
1. What can you say about the complexity of your code?
…
2. How will your algorithm scale?
…
3. If you had two weeks to do this task, what would you have done differently? What would be
better?
…
Send us the link to your git repository when you’re ready,
Good luck!!!
