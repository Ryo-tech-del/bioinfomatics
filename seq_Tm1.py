def DNA_Tm(seq):
        A=T=G=C=0
        for w in seq:   
                if w=="A":
                        A+=1
                if w=="T":
                        T+=1
                if w=="G":
                        G+=1
                if w=="C":
                        C+=1

        return print((A+T)*4+(C+G)*8)

