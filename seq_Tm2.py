import math
def DNA_Tm(seq,Na):
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

        A=float(A)
        T=float(T)
        G=float(G)
        C=float(C)

        return print(81.5-16.6*(math.log10(Na))+0.41*((C+G)/(A+T+G+C)))
