#BY ASVIN JAIN
data=(("HEAD1","HEAD2","HEAD3","HEAD4","HEAD5","HEAD6"),  #SAMPLE DATA
      ('E001', 'Sameer Gupta',  'VP', 'SALES', 85000, 10000),
      ('E002', 'Ajay Sharma',  'MGR', 'MKT', 56000, 6720),
      ('E003', 'Anita Sood',  'AST-MGR', 'ACCOUNTS', 75000, 7500),
      ('E004', 'Raghav Gupta',  'AVP', 'SALES', 90000, 10000),
      ('E005', 'Rashi Sharma',  'GM', 'MKT', 89000, 10680),
      ('E006', 'Aditya Suri',  'CLERK', 'HRD', 35000, 10000),
      ('E007', 'Samiksha',  'MGR', 'ACCOUNTS', 65000, 6500),
      ('E008', 'Neeta Jain',  'MGR', 'SALES', 57000, 10000))

def tablemaker(data):     #OPTIMIZED VARIANT
    l=len(data[0])
    lf=[]
    for p in range(l):
        li=[]
        mx=0
        for i in data:
            aa=len(str(i[p]))
            li.append(aa)
            mx=max(li)
        else:
            lf.append(mx)
    print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="")
    for p in data:
        for i in range(l):
            print("|"," ",p[i]," "," "*(lf[i]-len(str(p[i]))),"|",end="",sep="")
        if data[0]==p:
            print()
            print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="",end="")            
        print()
    print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="")# table making end

tablemaker(data)


def tablemaker(data):   #ORIGINAL
    l=len(data[0])
    lf=[]
    for p in range(l):
        li=[]
        mx=0
        for i in data:
            try:
                aa=len(str(i[p]))
                li.append(aa)
                mx=max(li)
            except:
                continue
        else:
            if mx==0:
                mx=10
            lf.append(mx)
    #print(lf)
    #print(sum(lf))
    print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="")
    for p in data:
        for i in range(l):            
            try:
                print("|"," ",p[i]," "*(lf[i]-len(str(p[i])))," ","|",end="",sep="")
            except:
                print("|"," ",p[i]," ","|",end="",sep="")
        if data[0]==p:
            print()
            print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="",end="")
        print()
    print("+","-"*((len(lf)*4)+sum(lf)-2),"+",sep="")

tablemaker(data)
