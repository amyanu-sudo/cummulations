#splits the string 1 time at pattern matching.

import re
string = 'Twelve:12 Eighty nine:89 Nine:9.'
pattern = '\d+'
# split only at the first occurrence
result = re.split(pattern, string, 1) 
print(result)

# Output: ['Twelve:', ' Eighty nine:89 Nine:9.']
