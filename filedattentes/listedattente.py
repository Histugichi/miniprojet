import database as db
from filedattentes import filedattente

class Fileattente:
    def __init__(self):
        
        self.curseur = self.connexion.cursor()
        self.creer_table_file_attente()

    def creer_table_file_attente(self):
        self.curseur.execute("""
            
        """)
        self.connexion.commit()

    def ajouter_personne_en_attente(self, nom):
        self.curseur.execute("""
            (nom, prioritaire) VALUES (%s, FALSE)
        """, (nom,))
        self.connexion.commit()
        print(f"{nom} a ete ajoute a la file d'attente.")

    def ajouter_personne_prioritaire(self, nom):
        self.curseur.execute("""
            INSERT INTO FileAttente (nom, prioritaire) VALUES (%s, TRUE)
        """, (nom,))
        self.connexion.commit()
        print(f"{nom} a ete ajoute en tant que personne prioritaire a la file d'attente.")

    def supprimer_personne_de_attente(self):
        self.curseur.execute("""
            SELECT nom FROM FileAttente WHERE prioritaire = TRUE ORDER BY id LIMIT 1
        """)
        personne_prioritaire = self.curseur.fetchone()
        if personne_prioritaire:
            nom = personne_prioritaire[0]
            self.curseur.execute("""
                DELETE FROM FileAttente WHERE nom = %s
            """, (nom,))
            self.connexion.commit()
            print(f"{nom} a ete retire en tant que personne prioritaire de la file d'attente.")
        else:
            self.curseur.execute("""
                
            """)
            personne = self.curseur.fetchone()
            if personne:
                nom = personne[0]
                self.curseur.execute("""
                    DELETE FROM FileAttente WHERE nom = %s
                """, (nom,))
                self.connexion.commit()
                print(f"{nom} a ete retire de la file d'attente.")
            else:
                print("La file d'attente est vide.")

    def __del__(self):
        self.curseur.close()
        self.connexion.close()