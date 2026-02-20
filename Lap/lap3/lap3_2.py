gmail = " Student_01@TU.AC.TH "
gmail = gmail.strip()
gmailfind = gmail.find('@')
parts = gmail.split("@")[0]
parts2 = gmail.split('@')[1]

print('clear gmail:' ,gmail.lower())
print("Username:", parts.lower())
print("Domain:",parts2.lower())
print("At position:",gmailfind)