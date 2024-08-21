# Factura electronica


## Introducere

Folosind cunostiintele de baze de date si programare in Python dobandite pana acum, vom scrie o aplicatie de management al facturilor. 
Aplicatia trebuie scrisa in Python si trebuie sa integreze atat o baza de date de tip SQLite, cat si o baza de date MySQL. 
Aplicatia trebuie sa citeasca de la tastatura informatii despre: Clienti Facturi Produse (ale facturilor)
sa le stocheze in baza de date si sa genereze facturi de tip .txt 

O factura are 3 componente: 
- Client
- Furnizor
- Produs

Cele 3 categorii de informatii enumerate mai sus pot fi reprezentate ca tabele intr-o baza de date:
### Client 
- Id 
- Nume 
- CIF/CUI 
- Adresa 

### Produs 
- Id
- Denumire 
- Cantitate 
- Pret unitar 
- Pret total 

### Factura
- Id 
- Client (Referinta catre o inregistrare de la punctul 1. Client) 
- Furnizor (Referinta catre o inregistrare de la punctul 1. Client) 
- Produse (Mai multe referinte catre inregistrari de la Punctul 2. Produs) 
- Numar (Numar factura, diferit de id. Exemplu: “JD 0001”) 
- Total (Calculat pe baza produselor)

## Instalare

Cloneaza repozitory-ul:

```bash
git clone https://github.com/Cata341/Proiect-2.git
```

Navigheaza in folderul proiectului, creaza un virtual environment si instaleaza dependintele:
```bash
cd proiect2-curs
python -m venv venv
pip install -r requirements.txt
```

## Requirements
- SQLAlchemy

## Utilizare

Pentru a usura, atat intretinerea, cat si interactiunea cu baza de date, putem folosi ORM-ul SQLAlchemy. 
Cu ajutorul aplicatiei trebuie sa putem adauga, sterge, lista facturi, clienti si produse. 
Se pot imbina concepte de citire de la tastatura cu concepte de citire a argumentelor din linia de comanda. 
Scopul final este sa putem emite facturi pentru diferiti client cu diferite produse.

### Configurarea mediului: 
- Instalează SQLAlchemy
- (sau daca vrem sa folosim MySQL) PyMySQL

## Definirea modelelor ORM: 
Creează clasele pentru Client, Produs și Factura. 
- Interacțiunea cu baza de date: Funcții pentru adăugarea, ștergerea, listarea și generarea facturilor. 
- Interfață utilizator: Funcții pentru citirea datelor de la tastatură sau din linia de comandă. 
- Generarea facturilor în format .txt: Funcție pentru crearea fișierelor de factură.

