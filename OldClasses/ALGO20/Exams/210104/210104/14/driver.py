from Sol import maxK

prevN=None
endR=1500

for N in range(10,endR+1):
    kk=maxK(N)
    if prevN is None:
        prevN=N
        prevKK=kk
        continue

    if kk != prevKK:
        print("da N=",prevN,"\ta N=",N-1,"\tmassimo ottenuto per k=",prevKK)
        prevN=N
        prevKK=kk

print("da N=",prevN,"\ta N=",endR,"\tmassimo ottenuto per k=",prevKK)



