import re
burti=re.compile('^[A-Za-z]+$')
a=""
while not burti.match(a):
    a=(input("Ievadi vārdu: ")).strip().upper()


jautajumi=(("1. Kā izveidot ciklu, kas izdrukā skaitļus no 1 līdz 10?"),
           ("2. Kā pareizi tiek rakstīts cikls ar priekšnosacījumu programmā?"),
           ("3. Kā 'break' komanda darbojas ciklā"),
           ("4. Vai cikls while varētu būt bezgalīgs?"),
           ("5. Cik reizes izpildīsies while cikls , ja viņam ir nosacījums TRUE?"),
           ("6. Kurās programmēšanmas valodās neizmanto while ciklu?"),
           ("7. Kurus ciklus neizmanto Python?") ,
           ("8. Kurš nosacījums While ciklam ir nepareizs?"),
           ("9. Ko ir jāliek while nosacījuma?"),
           ("10. Kads ir Python while cikla pamata sintakse?"))

izveles=(("A. while x < 10: print(x)","B. while x < 11: print(x)", "C. for x in range(11)","D. while x <= 10: print(x)"),
         ("A. while","B. WHILE","C. While","D. while"),
         ("A. Aptur ciklu","B. turpina ciklu","C. pabeidz ciklu ","D. palaiž ciklu"),
         ("A. Jā","B. Pēc lietotāja izvēles","C. Nē ","D. Nekādīgi"),
         ("A. Kāmēr nebūs kļūda","B. Bezgalīgi daudz","C. bezgalīgi ","D. vienu reizi"),
         ("A. PostScript","B. Java","C. Python ","D. Erlang"),
         ("A. map","B. if","C. filter ","D. for"),
         ("A. ==","B. <<","C. -- ","D. <"),
         ("A. ;", "B. :","C. ;","D. :"),
         ("A. nosacījums", "B. nosacījums ","C. Kāmēr","D. Kāmēr"))

atbildes=(("C","D"),
          ("A","D"),
          ("A","C"),
          ("A","B"),
          ("B","C"),
          ("A","D"),
          ("A","C"),
          ("B","C"),
          ("B","D"),
          ("C","D"))

izveletas=[]
punkti=0
jautNr=0
nepareizieJ=[]

while jautNr<10:
    print("--------")
    print(jautajumi[jautNr])
    for opcija in izveles[jautNr]:
        print(opcija)
        
    izvelesIevade=input("Ievadi savu atbildi  (A, B, C, D):").upper()
    
    
    if izvelesIevade in atbildes[jautNr]:
      punkti+=1
      print("Pareizi!")
      jautNr+=1
    else:
      print("Nepareizi!")  
      
      nepareizieJ.append((jautajumi[jautNr],izvelesIevade,atbildes[jautNr]))
      jautNr+=1
print("----------")    
print("Rezulāts: ")
print(" Lietotājam ",a," ir ",punkti,"pareizās atbildes no 10")   

if nepareizieJ:
    print("Nepareizie jautājumi: ")
    for jautajums,atbilde,pareizas in nepareizieJ:
        print(jautajums)
        print("Tava atbilde: ", atbilde) 
        print("Pareizās atbildes: ",pareizas)
elif nepareizieJ==0:
        print("Visas atbildes ir pareizas")
else:
    print("Visas atbildes ir pareizas")