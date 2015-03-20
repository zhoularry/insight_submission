# Insight Data Engineering Fellows Program - Coding Challenge
## Word Counter
One of the first problems you'll encounter in data engineering is Word Count, which takes in 
a text file or set of text files from a directory and outputs the number of occurrences for each word.  
For example, Word Count on a file containing the following passage:


So call a big meeting,
Get everyone out out,
Make every Who holler,
Make every Who shout shout.

would return:

  * a			1
  * big		1
  * call		1
  * every	2
..* everyone1
..* get		1
..* holler  1
..* make	 	2
..* meeting	1
..* out		2
..* shout   2
..* so		1
..* who		2

The first part of the coding challenge is to implement your own version of Word Count that counts all
the words from the text files contained in a directory named wc_input and outputs the counts 
(in alphabetical order) to a file named wc_result.txt,which is placed in a directory named wc_output.
