import re

Emailpattern = r"^\w+[0-9]+\@\w+\.\w+$"
Namepattern = r"^[a-zA-Z]+$"
st = "_0kj_l_56125@897a.c"
st1 = "gjh,"
result = re.match(Emailpattern, st)
if result:
    print("Emailtrue")
else:
    print("Emailfale")
result = re.match(Namepattern, st1)
if result:
    print("Nametrue")
else:
    print("Namefale")
# hassan125@gg.com

