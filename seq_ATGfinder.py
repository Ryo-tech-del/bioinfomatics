def DNA_ATG(seq):
     import re
     pattern=r"ATG"
     ite=re.finditer(pattern,seq)
     for match in ite:
             print(match.group(),match.start())
