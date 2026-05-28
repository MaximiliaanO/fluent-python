import re
import collections

WORD_RE = re.compile(r'\w+') #\w+ matches one or more word characters

index = collections.defaultdict(list)

with open('Chapter_3/zen.txt', encoding='utf-8') as fp:
    for line_no, line in enumerate(fp, 1):              #Iterate through the lines of the file starting index at 1 returns (index, lineitem)
        for match in WORD_RE.finditer(line):            #Goes through every match (word) in the line
            word = match.group()                        #Returns only the fully matched word because there is no caputre group.
            column_no = match.start() + 1               #Match.start() = the starting index of the match added + 1 because indexing starts at 0.
            location = (line_no, column_no)             #Stores location in a tuple
            index[word].append(location)                #Default dict creates a new list when a key is missing, key[[list]]


#display in alphabeticl order:
for word in sorted(index, key=str.upper):
    print(word, index[word])