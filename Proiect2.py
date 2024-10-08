from sqlalchemy import create_engine, Column, Integer, String, Float, ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

Base = declarative_base()

factura_produs = Table('factura_produs', Base.metadata,
                       Column('factura_id', Integer, ForeignKey('factura.id')),
                       Column('produs_id', Integer, ForeignKey('produs.id'))
                       )


class Client(Base):
    __tablename__ = 'client'
    id = Column(Integer, primary_key=True)
    nume = Column(String)
    cif_cui = Column(String)
    adresa = Column(String)
    facturi = relationship('Factura', back_populates='client', foreign_keys='Factura.client_id')
    furnizori = relationship('Factura', back_populates='furnizor', foreign_keys='Factura.furnizor_id')


class Produs(Base):
    __tablename__ = 'produs'
    id = Column(Integer, primary_key=True)
    denumire = Column(String)
    cantitate = Column(Float)
    pret_unitar = Column(Float)
    pret_total = Column(Float)

    facturi = relationship("Factura", secondary=factura_produs, back_populates="produse")


class Factura(Base):
    __tablename__ = 'factura'
    id = Column(Integer, primary_key=True)
    numar = Column(String)
    total = Column(Float)
    client_id = Column(Integer, ForeignKey('client.id'))
    furnizor_id = Column(Integer, ForeignKey('client.id'))
    client = relationship('Client', foreign_keys=[client_id], back_populates='facturi')
    furnizor = relationship('Client', foreign_keys=[furnizor_id], back_populates='furnizori')
    produse = relationship('Produs', secondary='factura_produs', back_populates='facturi')


def create_engine_and_session(db_url):
    engine = create_engine(db_url)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    return engine, Session()


# Pentru SQLite
sqlite_engine, sqlite_session = create_engine_and_session('sqlite:///facturi.db')


# Pentru MySQL
# mysql_engine, mysql_session = create_engine_and_session('mysql+pymysql://user:password@localhost/facturi')

def adauga_client(session, nume, cif_cui, adresa):
    client = Client(nume=nume, cif_cui=cif_cui, adresa=adresa)
    session.add(client)
    session.commit()


def adauga_produs(session, denumire, cantitate, pret_unitar):
    pret_total = cantitate * pret_unitar
    produs = Produs(denumire=denumire, cantitate=cantitate, pret_unitar=pret_unitar, pret_total=pret_total)
    session.add(produs)
    session.commit()


def adauga_factura(session, client_id, furnizor_id, produse):
    total = sum([produs.pret_total for produs in produse])
    numar_factura = f"JD {str(session.query(Factura).count() + 1).zfill(4)}"
    factura = Factura(client_id=client_id, furnizor_id=furnizor_id, numar=numar_factura, total=total, produse=produse)
    session.add(factura)
    session.commit()


def lista_clienti(session):
    for client in session.query(Client).all():
        print(f"{client.id}: {client.nume} - {client.cif_cui} - {client.adresa}")


def lista_produse(session):
    for produs in session.query(Produs).all():
        print(f"{produs.id}: {produs.denumire} - {produs.cantitate} - {produs.pret_unitar} - {produs.pret_total}")


def lista_facturi(session):
    for factura in session.query(Factura).all():
        print(f"{factura.id}: {factura.numar} - {factura.total}")


def genereaza_factura_txt(session, factura_id, filename):
    factura = session.query(Factura).filter_by(id=factura_id).one()
    with open(filename, 'w') as f:
        f.write(f"Factura Nr: {factura.numar}\n")
        f.write(f"Client: {factura.client.nume}, CIF: {factura.client.cif_cui}, Adresa: {factura.client.adresa}\n")
        f.write(
            f"Furnizor: {factura.furnizor.nume}, CIF: {factura.furnizor.cif_cui}, Adresa: {factura.furnizor.adresa}\n")
        f.write("Produse:\n")
        for produs in factura.produse:
            f.write(
                f"{produs.denumire} - Cantitate: {produs.cantitate}, Pret Unitar: {produs.pret_unitar}, Pret Total: {produs.pret_total}\n")
        f.write(f"Total Factura: {factura.total}\n")


def main():
    while True:
        print("1. Adauga client")
        print("2. Adauga produs")
        print("3. Adauga factura")
        print("4. Listeaza clienti")
        print("5. Listeaza produse")
        print("6. Listeaza facturi")
        print("7. Genereaza factura .txt")
        print("0. Iesi")
        optiune = input("Alege o optiune: ")

        if optiune == '1':

            nume = input("Nume client: ")
            cif_cui = input("CIF/CUI: ")
            adresa = input("Adresa: ")
            adauga_client(sqlite_session, nume, cif_cui, adresa)
        elif optiune == '2':
            denumire = input("Denumire produs: ")
            cantitate = float(input("Cantitate: "))
            pret_unitar = float(input("Pret unitar: "))
            adauga_produs(sqlite_session, denumire, cantitate, pret_unitar)
        elif optiune == '3':
            lista_clienti(sqlite_session)
            client_id = int(input("ID Client: "))
            furnizor_id = int(input("ID Furnizor: "))
            lista_produse(sqlite_session)
            produse_ids = input("ID-uri Produse (separate prin virgula): ").split(',')
            produse = [sqlite_session.query(Produs).filter_by(id=int(id)).one() for id in produse_ids]
            adauga_factura(sqlite_session, client_id, furnizor_id, produse)
        elif optiune == '4':
            lista_clienti(sqlite_session)
        elif optiune == '5':
            lista_produse(sqlite_session)
        elif optiune == '6':
            lista_facturi(sqlite_session)
        elif optiune == '7':
            factura_id = int(input("ID Factura: "))
            filename = input("Nume fisier: ")
            genereaza_factura_txt(sqlite_session, factura_id, filename)
        elif optiune == '0':
            break


if __name__ == "__main__":
    main()
