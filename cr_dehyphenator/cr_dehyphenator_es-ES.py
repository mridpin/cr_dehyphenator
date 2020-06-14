# This script removes the hyphenation that splits words at the end of the lines,
# in order to remove noise for NLP work. También funciona en español.
# For example, the lines:
# "este script me ha sal-
# vado la vida"
# -->
# "este script me ha 
# salvado la vida"

# ----------------------------------------------------------------------------
# "CR_DEHYPHENATOR" (Revision 1.0):
# mridpin wrote this file. You can do whatever you want with this stuff. Including but not limited to:
# writing a GATE plugin, using it as NLP preprocessing, printing it and shoving it up your rectum, etc
# ----------------------------------------------------------------------------

import os

from nltk.tokenize import word_tokenize
from nltk.tokenize.treebank import TreebankWordDetokenizer

# path vars, modify accordingly
input_docs = str(os.getcwd()) + '/input_docs'
output_dir = str(os.getcwd()) + '/output_docs'

print(os.getcwd())

files = [i for i in os.listdir(input_docs) if i.endswith("txt")]

for input_file in files:

    input_lines = open(os.path.join(input_docs, input_file)).readlines()

    output_lines = ''
    hyphenated_word = ''

    # iterate the text looking for applicable cases. 
    for line in input_lines:

        # check if prev line had applicable word
        if (hyphenated_word):
            line = hyphenated_word + line
            hyphenated_word = '' 

        line = line.strip()
        if len(line) > 2:
            last_char = line[-1]
            # if last char is hyphen
            if (last_char == '-'):
                # if prev char to hyphen is alpha
                prev_char = line[-2]
                if (prev_char.isalpha()):
                    # store last token to join with next line
                    tokens = word_tokenize(line)
                    hyphenated_word = tokens[-1].rstrip('-')
                    tokens.pop()
                    line = TreebankWordDetokenizer().detokenize(tokens)
        output_lines += line + "\n"

    # write output file
    output_file = open(output_dir + '/dehyphenated_' + input_file, 'w')
    output_file.write(output_lines)
    output_file.close()