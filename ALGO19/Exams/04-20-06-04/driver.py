from SBST import SBST

print("Primo test su albero vuoto")
Albero=SBST()
ListaOrdinata=Albero.sorting()
print(ListaOrdinata)

print("Inseriamo i dati dall'esempio della traccia")
Albero.insert(3,"pluto")
Albero.insert(8,"pippo")
Albero.insert(7,"minnie")
ListaOrdinata=Albero.sorting()
print(ListaOrdinata)

print("Un nuovo esempio")
NuovoAlbero=SBST()
citta=[["Roma",2856133],["Milano",1378689],["Napoli",959188],["Torino",875698],["Palermo",663401], ["Genova",578000],["Bologna",390636], ["Firenze",378839],["Bari",320862], ["Catania", 311584]]

for ct in citta:
    [nome,pop]=ct
    NuovoAlbero.insert(nome,pop)

ListaOrdinataCitta=NuovoAlbero.sorting()
print(ListaOrdinataCitta)

