import mysql.connector as mysql

# Fonction pour établir une connexion à la base de données MySQL
def connexion_db():
    connexion = mysql.connect(
        user='root',
        password='',
        host='localhost',
        database='listepersonne'
    )
    return connexion

# Fonction pour créer un nouvel utilisateur
def create_user(email, password, nom):
    connexion = connexion_db()
    curseur = connexion.cursor()

    sql = "INSERT INTO utilisateurs(email, mot_de_passe, nom) VALUES(%s,%s,%s)"
    curseur.execute(sql, (email, password, nom))
    connexion.commit()

    curseur.close()
    connexion.close()

    return (nom, email)

# Fonction pour lister tous les utilisateurs
def read_users():
    connexion = connexion_db()
    curseur = connexion.cursor()

    sql = "SELECT * FROM utilisateurs"
    curseur.execute(sql)
    utilisateurs = curseur.fetchall()
    for utilisateur in utilisateurs:
        print(utilisateur)

    curseur.close()
    connexion.close()

# Fonction pour mettre à jour les informations d'un utilisateur
def update_user(ID, email, password, nom):
    connexion = connexion_db()
    curseur = connexion.cursor()

    sql = "UPDATE utilisateurs SET email=%s, mot_de_passe=%s, nom=%s WHERE id=%s"
    curseur.execute(sql, (email, password, nom, ID))
    connexion.commit()

    curseur.close()
    connexion.close()

# Fonction pour supprimer un utilisateur
def delete_user(ID):
    connexion = connexion_db()
    curseur = connexion.cursor()

    sql = "DELETE FROM utilisateurs WHERE id=%s"
    curseur.execute(sql, (ID,))
    connexion.commit()

    curseur.close()
    connexion.close()

# Fonction principale pour afficher le menu et interagir avec les utilisateurs
def main():
    while True:
        print("\nMenu :")
        print("1. Ajouter un utilisateur")
        print("2. Mettre à jour un utilisateur")
        print("3. Supprimer un utilisateur")
        print("4. Lister les utilisateurs")
        print("5. Ajouter un âge")
        print("6. Quitter")

        choix = input("Entrez votre choix : ")

        if choix == "1":
            email = input("Entrez l'adresse email : ")
            mot_de_passe = input("Entrez le mot de passe : ")
            nom = input("Entrez le nom complet : ")
            create_user(email, mot_de_passe, nom)
            print("Utilisateur ajouté avec succès.")

        elif choix == "2":
            ID = input("Entrez l'ID de l'utilisateur à mettre à jour : ")
            email = input("Entrez la nouvelle adresse email : ")
            mot_de_passe = input("Entrez le nouveau mot de passe : ")
            nom = input("Entrez le nouveau nom complet : ")
            update_user(ID, email, mot_de_passe, nom)
            print("Utilisateur mis à jour avec succès.")

        elif choix == "3":
            ID = input("Entrez l'ID de l'utilisateur à supprimer : ")
            delete_user(ID)
            print("Utilisateur supprimé avec succès.")

        elif choix == "4":
            print("\nListe des utilisateurs :")
            read_users()

        elif choix == "5":
             age= input("Entrer un age")
             update_user(ID)
             print("mis a jour avec succes.")    

        elif choix == "6":
         print("Au revoir !")
         break

        else:
            print("Choix invalide. Veuillez saisir à nouveau.")

if __name__ == "__main__":
    main()