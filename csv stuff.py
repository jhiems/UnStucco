"""
Testing CSV stuff
"""

import csv

def find_dye(y):
    err = input("What is the degree of error you'd like?\n")
    ls_d = []
    ls_w = []
    ls_s = []
    with open("dye_1.csv", 'rb') as dye:
        r_d = csv.reader(dye)
        for c_d in r_d:
            for e_d in c_d:
                ls_d.append(float(e_d))
    with open("White.csv", 'rb') as white:
        r_w = csv.reader(white)
        for c_w in r_w:
            for e_w in c_w:
                ls_w.append(float(e_w))
    with open("Sample.csv", 'rb') as sample:
        r_s = csv.reader(sample)
        for c_s in r_s:
            for e_s in c_s:
                ls_s.append(float(e_s))
                
    print ls_s, "Sample", "\n", ls_w, "White", "\n", ls_d, "Dye"

    for i in range(10000):
        r = i*0.0001
        for i in range(3):
            if(ls_w[i]-ls_s[i]-err)/(ls_w[i]-ls_d[i]) < r and r < (ls_w[i]-ls_s[i]+ err)/(ls_w[i]-ls_d[i]):
                print r
            #print (ls_w[i]-ls_s[i]-err)/(ls_d[i]-ls_s[i])
            #print ls_w[i]
            #print r,  (ls_w[i]-ls_s[i]+err)/(ls_w[i]-ls_d[i]) , (ls_w[i]-ls_s[i]-err)/(ls_w[i]-ls_d[i])
            #print (ls_w[i]-ls_s[i]+err)/(ls_w[i]-ls_d[i])
    
            















"""
    for i in range(int(1/float(err))):
        r = i*err
        with open("dye_1.csv", 'rb') as dye:
            reader_dye = csv.reader(dye)
            
            with open(y, 'rb') as sample:
                reader_sample = csv.reader(sample)
                
                with open("White.csv", 'rb') as white:
                    reader_white = csv.reader(white)

                    

                    for i in reader_white, reader_dye, reader_sample:
                        for z in i:
                            for p in z:
                                print p
                                
"""
                 

find_dye("Sample_1.csv")

"""
            r = i*(err)
            for i in range(3):
                if (white[1] - x[1]) == x:
                    print "foo"
"""
