import mysql.connector as mysql
import database

class SalleCinema:
    def __init__(self, nom_salle, capacite):
        self.nom_salle = nom_salle
        self.capacite = capacite
        self.connexion = mysql.connector.connect(
            
        )
        self.curseur = self.connexion.cursor()
        self.creer_table_reservations()

    def creer_table_reservations(self):
        self.curseur.execute("""
            """)
        self.connexion.commit()

    def reserver_place(self, nom, place):
        if self.verifier_place_disponible(place):
            self.curseur.execute("""
                INSERT INTO Reservations (nom, place) VALUES (%s, %s)
            """, (nom, place))
            self.connexion.commit()
            print(f"Place {place} reservee pour {nom}.")
        else:
            print("La place specifiee est deja reservee ou invalide.")

    def verifier_place_disponible(self, place):
        self.curseur.execute("""
            SELECT COUNT(*) FROM Reservations WHERE place = %s
        """, (place,))
        count = self.curseur.fetchone()[0]
        return count == 0 and 1 <= place <= self.capacite

    def afficher_places_reservees(self):
        self.curseur.execute("""
            SELECT nom, place FROM Reservations
        """)
        reservations = self.curseur.fetchall()
        if reservations:
            print("Places reservees :")
            for nom, place in reservations:
                print(f"{nom} a reserve la place {place}.")
        else:
            print("Aucune place n'a ete reservee.")

    def __del__(self):
        self.curseur.close()
        self.connexion.close()