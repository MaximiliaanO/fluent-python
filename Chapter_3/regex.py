import re

WORD_RE = re.compile(r'\w+') #\w+ matches one or more word characters

with open('Chapter_3/zen.txt', encoding='utf-8') as fp:
        for line_no, line in enumerate(fp, 1):              #Iterate through the lines of the file starting index at 1 returns (index, lineitem)
            for match in WORD_RE.finditer(line):            #Returns iterator of regex matches being words on the line
                print(match)
                word = match.group()
                print(word)