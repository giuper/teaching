from BF import bfPM
from KMP import kmpPM
from RK import prepareText, lookup
import time

f=open('DivinaCommedia.txt','r')
T=f.read()
f.close()

PP=["Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta.", "Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta.", "Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta.", "Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta.", "Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta.", "Allor fu la paura un poco queta,"+"\n"+"che nel lago del cor m’era durata"+"\n"+"la notte ch’i’ passai con tanta pieta."]
PP=['aba','abe','aca','ace','ada','ade','afa','afe','aga','age','ala','ale','ama','ame','ana','ane','apa','ape','ara','are','asa','ase','ata','ate','ava','ave','aza','aze']

PP=["aaab","aaac","caab","caaa","aaaa","abaa","aaba","baaa",]

for SIZE in [1_000,10_000,50_000,100_000,1_000_000,5_000_000,8_000_000]:
    print(f'{"Testo di lunghezza:":25s}{SIZE:10d}')
    print(f'{"Numero di pattern:":25s}{len(PP):10d}')
    T="a"*SIZE+"b"
    start=time.time()
    bfres=[]
    for P in PP:
        bfres.append(bfPM(T,P))
    print(f'{"Algoritmo di Forza Bruta":40s}{time.time()-start:10.6f}')
    
    
    kmpres=[]
    start=time.time()
    for P in PP:
        kmpres.append(kmpPM(T,P))
    print(f'{"Algoritmo Knuth-Morris-Pratt":40s}{time.time()-start:10.6f}')
    
    rkres=[]
    startp=time.time()
    TT=prepareText(T,len(PP[0]))
    finishp=time.time()
    startl=time.time()
    for P in PP:
        rkres.append(lookup(TT,P))
    finishl=time.time()
    print(f'{"Algoritmo Rabin-Karp":40s}')
    print(f'{"   Preparazione testo":40s}{finishp-startp:10.6f}')
    print(f'{"   Operazioni di lookup":40s}{finishl-startl:10.6f}')
    print(f'{"Totale":40s}{finishl-startp:10.6f}')

    print()

    for i in range(len(PP)):
        if(bfres[i]!=kmpres[i]):
            print("Errore per",PP[i])
        if(bfres[i]!=rkres[i]):
            print("Errore per",PP[i])
