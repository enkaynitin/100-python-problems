import re
emailAddress = raw_input()
pattern2 = "(\w+)@(\w+)+(\.com)"
r2 = re.match(pattern2, emailAddress)
print r2.group(2)
