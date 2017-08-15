# SoloLearn Python Tutorial - RegEx

"""
Our regex contains three groups:
1 - first part of the email address.
2 - domain name without the suffix.
3 - the domain suffix.
"""

pattern = r"([\w\.-]+)@([\w\.-]+)(\.[\w]+)"

str = "Favor de contactarse con tuvieja@elpirata.com"

match = re.search(pattern, str)
if match:
   print(match.group())
