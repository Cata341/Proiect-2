# Factura electronica


## Introducere

Folosind cunostiintele de baze de date si programare in Python dobandite pana acum, vom scrie o aplicatie de management al facturilor. 
Aplicatia trebuie scrisa in Python si trebuie sa integreze atat o baza de date de tip SQLite, cat si o baza de date MySQL. 
Aplicatia trebuie sa citeasca de la tastatura informatii despre: Clienti Facturi Produse (ale facturilor)
sa le stocheze in baza de date si sa genereze facturi de tip .txt 
O factura are 2 componente: Client si furnizor (2 intrari de tip Client) Produse (1 sau mai multe intrari de tip Produs). 
Cele 3 categorii de informatii enumerate mai sus pot fi reprezentate ca tabele intr-o baza de date: 
1. Client 
2. Id 
3. Nume 
4. CIF/CUI 
5. Adresa 
6. Produs 
7. id 
8. Denumire 
9. Cantitate 
10. Pret unitar 
11. Pret total 
12. Factura 
13. id 
14. Client (Referinta catre o inregistrare de la punctul 1. Client) 
15. 15 Furnizor (Referinta catre o inregistrare de la punctul 1. Client) 
16. 16 Produse (Mai multe referinte catre inregistrari de la Punctul 2. Produs) 
17. 17 Numar (Numar factura, diferit de id. Exemplu: “JD 0001”) 
18. 18 Total (Calculat pe baza produselor)

## Instalare

Cloneaza repozitory-ul:
https://github.com/Cata341/Proiect-2.git
Navigheaza in folderul proiectului.
Creaza un virtual environment si instaleaza dependintele
cd proiect2-curs
python -m venv venv
pip install -r requirements.txt


## Requirements
SQLAlchemy

## Utilizare

Pentru a usura, atat intretinerea, cat si interactiunea cu baza de date, putem folosi ORM-ul SQLAlchemy. 
Cu ajutorul aplicatiei trebuie sa putem adauga, sterge, lista facturi, clienti si produse. 
Se pot imbina concepte de citire de la tastatura cu concepte de citire a argumentelor din linia de comanda. 
Scopul final este sa putem emite facturi pentru diferiti client cu diferite produse.

• Configurarea mediului: 
- Instalează SQLAlchemy, 
- PyMySQL. 
• Definirea modelelor ORM: 
Creează clasele pentru Client, Produs și Factura. 
• Interacțiunea cu baza de date: Funcții pentru adăugarea, ștergerea, listarea și generarea facturilor. 
• Interfață utilizator: Funcții pentru citirea datelor de la tastatură sau din linia de comandă. 
• Generarea facturilor în format .txt: Funcție pentru crearea fișierelor de factură.

