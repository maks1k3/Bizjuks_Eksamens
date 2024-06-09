a=(input("Ievadi vārdu: "))


jautajumi=(("Kā izveidot ciklu, kas izdrukā skaitļus no 1 līdz 10"),
           ("Kā pareizi tiek rakstīts cikls ar priekšnosacījumu programmā"),
           ("Kā 'break' komanda darbojas ciklā"))

izveles=(("A. while x < 10: print(x)","B. while x < 11: print(x)", "C. for x in range(11)","D. while x <= 10: print(x)"),
         ("A. while","B. WHILE","C. While","D. while"),
         ("A. Aptur ciklu","B. turpina ciklu","C. pabeidz ciklu ","D. palaiž ciklu"))

atbildes=(("C","D"),
          ("A","D"),
          ("A","C"))

izveletas=[]
punkti=0
jautNr=0

while jautNr<10:
    print("--------")
    print(jautajumi[jautNr])
    for opcija in izveles[jautNr]:
        print(opcija)
        
    izvelesIevade=(input("Ievadi savu atbildi  (A, B, C, D):")).upper()
    if izvelesIevade =='q':
        break
    
    if izvelesIevade in atbildes[jautNr]:
      punkti+=1
      print("Pareizi!")
    else:
        print("Nepareizi!")  
        jautNr+=1
         
  