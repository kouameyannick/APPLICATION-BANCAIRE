
import hashlib

import os

import sqlite3

from multiprocessing import connection

from getpass import getpass

from hashlib import *

from colorama import Cursor


def RECHERCHE_TRANS() :

    NUMERO_TELEPHONE=int(input("") )

    os.system("clear")

    if os.path.exists("donnee.db") :
            
            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()

            requette = f"SELECT * FROM clients WHERE telephone = ? "

            curseur.execute(requette,(NUMERO_TELEPHONE,))

            resultat_affichage = curseur.fetchone()

            print("\n--------------------------------------Bénéficiaire--------------------------------------------\n")
            
            print("\nN°compte client : ",resultat_affichage[1])

            print("\nNom client : ",resultat_affichage[2])

            print("\nPrenom client : ",resultat_affichage[3])

            print("\nTelephone : ",resultat_affichage[12])

            print("\n---------------------------------------------------------------------------------------")

            compte_transferant = int(input('\t\t\n\nEntrer le N°telephone du transferant :\t'))

            somme = float(input("\t\t\n\nEntrer le montant du Transfert :\t"))

            precedent = int(input("\n\n\t  0.Retour \n\n\t 9.Quitter \n"))

            if (precedent == 0) :

                main()

            elif (precedent == 9) :

                os.system("clear")

                quit()


    else :
            
        print ("Cette fonctionnalité n'exist pas \n\n")
        

            # FONCTION POUR RECHERCHER UN COMPTE POUR LE VERSEMENT!

def RECHERCHE_VERS( ) :

    NUMERO_TELEPHONE=int(input(""))

    os.system("clear")

    if os.path.exists("donnee.db") :
            
            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()

            requette = f"SELECT * FROM clients WHERE telephone = ? "

            curseur.execute(requette,(NUMERO_TELEPHONE,))

            resultat_affichage = curseur.fetchone()

            print("--------------------------------------Abonnée--------------------------------------------\n")
            
            print("\nN°compte client : ",resultat_affichage[1])

            print("\nNom client : ",resultat_affichage[2])

            print("\nPrenom client : ",resultat_affichage[3])

            print("\nTelephone : ",resultat_affichage[12])

            print("\n---------------------------------------------------------------------------------------")

            depot = float(input("\n\t\t Combien voulez vous déposer \t"))

            confirmation = input("\n\t\t Entrez le code de confirmation \t")
            
            connection.close()

            precedent = int(input("\n\n\t  0.Retour \n\n\t 9.Quitter \n"))

            if (precedent == 0) :

                main()

            elif (precedent == 9) :

                os.system("clear")

                quit()

    else :
            
        print ("Cette fonctionnalité n'est pas disponible \n\n") 

        # FONCTION POUR VOIR LES INFOS SUR MON COMPTE
        
def information_compte () :

    NUMERO_TELEPHONE=int(input(""))

    os.system("clear")

    if os.path.exists("donnee.db") :
            
            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()

            requette = f"SELECT * FROM clients WHERE telephone = ? "

            curseur.execute(requette,(NUMERO_TELEPHONE,))

            resultat_affichage = curseur.fetchone()

            print("-------------------------------------------------------------INFORMATION SUR VOTR COMPTE --------------------------------------------------------------\n")
            
            print("\nN°compte client : ",resultat_affichage[1])

            print("\nNom client : ",resultat_affichage[2])

            print("\nPrenom client : ",resultat_affichage[3])

            print("\nEmail : ",resultat_affichage[4])

            print("\nLieux de naissance : ",resultat_affichage[6])
            
            print("\nDate de naissance : ",resultat_affichage[5])

            print("\nSituation Matrimonial : ",resultat_affichage[9])

            print("\nProfession : ",resultat_affichage[11])

            print("\nAdress : ",resultat_affichage[8])

            print("\nTelephone : ",resultat_affichage[12])

            print("\nNombre d'enfant : ",resultat_affichage[10])

            print("\nNationnalite : ",resultat_affichage[7])

            #print("Solde : ")

            print("\n---------------------------------------------------------------------------------------------------------------------------------------------------------")

            precedent = int(input("\n\n\t  0.Retour \n\n\t 9.Quitter \n"))

            if (precedent == 0) :

                mon_compte()

            elif (precedent == 9) :

                quit()

            else :

                print("\n Cette option n'existe pas ")

                quit()

    else :

        print("\n Une erreur est survenir lors du traitement ! \n\n")


        #FONCTION POUR SUPPRIMER UN COMPTE
         
def supprimer () :

    autorisation=2108

    NUMERO_TELEPHONE=int(input(""))

    os.system("clear")

    autorisation = float(input("\t\tEntrez le code d'autorisation\t"))

    if (autorisation == 2108) :

        if os.path.exists("donnee.db") :

            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()

            requette = f"DELETE FROM clients WHERE telephone = ? "

            curseur.execute(requette,(NUMERO_TELEPHONE,))

            connection.commit()

            connection.close()

            print('\n\n-----------------------------------------Votre compte a été supprimer avec success----------------------------------------------------------\n\n')

            precedent = int(input("\n\n\t  0.Retour \n\n\t00.Acceuil \n\n\t9.Quitter \n"))

            if (precedent == 0) :

                mon_compte()

            elif(precedent ==00) :

                main()

            elif (precedent == 9) :

                os.system("clear")

                quit()

            else :

                print("\n Cette option n'existe pas ")

                quit()

        else :

            print("\n Une erreur est survenir lors du traitement ! \n\n")

    else :

        print('\t\n\nLe code est incorrect')

            # FONCTION CREER UN COMPTE NOUVEAU  

def creer_compte() :

    os.system("clear")

    nombre_de_compte=int(input("\nEntrez le nombre de personnes dont vous voulez creer les comptes\t"))
    
    for i in range(nombre_de_compte) :
        
        print("\n---------------------------------------------client  {}-------------------------------------------------------\n".format(i+1))
        
        nom =input("\n Entrez le nom :\t")
        
        prenoms=input("\n Entrez le Prenoms :\t")

        email =input("\n Entrez votre email :\t")
        
        date_de_naissance=input("\n DATE DE NAISSANCE :\t")
        
        lieux_de_naissance=input("\n LIEUX DE NAISSANCE : \t")
        
        nationnalite=input("\n NATIONNALITE : \t")
        
        address=input("\n ADRESS (residence) : ")
        
        situation_matrimonail=input("\n SITUATION MATRIMONIAL : \t")
        
        nombre_enfant=int(input("\n NOMBRE ENFANT : \t"))
        
        profession =input("\n PROFESSION : \t")
        
        telephone=int(input("\n Telephone +225: \t"))
        
        code=getpass("\n ENTREZ UN CODE (a ne pas communiquer) : \t" )
        
        numero_compte=int(input("\n ENTREZ LE NUMERO DE COMPTE RECU PAR SMS AU  :{}\t".format(telephone)))
        
        if os.path.exists("donnee.db") :
            
            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()
            
            ecrire = f"INSERT INTO clients  (numero_compte,nom,prenoms,email,date_de_naissance,lieux_de_naissance,nationnalite,address,situation_matrimonial,nombre_enfant,profession,telephone,code) VALUES ( '{numero_compte}','{nom}','{prenoms}','{email}','{date_de_naissance}','{lieux_de_naissance}','{nationnalite}','{address}','{situation_matrimonail}','{nombre_enfant}','{profession}','{telephone}','{hashlib.sha256(code.encode()).hexdigest()}')"

            curseur.execute(ecrire)
            
            connection.commit()

            connection.close()

             # COMMENT JE CONNECT LA TABLE CLIENT  A LA TABLE COMPTE

            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()

            requette = f"SELECT * FROM clients WHERE numero_compte = ? "

            curseur.execute(requette,(numero_compte,))

            resultat_affichage = curseur.fetchone()

            identifiant = resultat_affichage[0]

            nom_compte = resultat_affichage[2]

            prenoms_compte = resultat_affichage[3]

            telephone_compte = resultat_affichage[12]

            ecrire_compte = f"INSERT INTO compte  (solde,client_id,nom,prenoms,telephone) VALUES ('{00}','{identifiant}','{nom_compte}','{prenoms_compte}','{telephone_compte}')"

            curseur.execute(ecrire_compte)

            connection.commit()

            connection.close() 

            print("\n\n-----------------------------------------------------FELICITATION Mr/Mm {} VOTRE COMPTE A ETE CREER AVEC SUCCESS ---------------------------------------------------------------------\n".format(nom))
            
            print("\n\t\tVEUILLEZ VOUS RENDRE A LA BANQUE POUR FINALISER LA PROCCEDURE DE CREATION DE COMPTE !\n")

            precedent = int(input("\n\n\t  0.Retour \n\n\t 1.Voir mon compte  \n\n\t9.Quitter \n"))

            if (precedent == 0) :

                main()
            
            elif(precedent == 1) :

                os.system("clear")

                print("\n\t\tEntrez votre N° de telephone \t")

                information_compte()


            elif (precedent == 9) :

                os.system("clear")

                quit()

        else :
            
            

            print ("le document n'exist pas \n\n")

                    # FONCTION VERSEMENT
                     
def versement () :
    
    os.system("clear")
    
    print("*************************************************** BIENVENUE DANS LE MENU VERSEMENT***************************************************************** \n\n")
    
    print("\t\t\tEntrez le numero de telephone du client \t")
    
    RECHERCHE_VERS()

                    # FONCTION TRANSFERT D'ARGENT 
def transfert () :
    
    os.system("clear")

    print("\t\t\t*******************************************BIENVENUE DANS LE MENU TRANSFERT D ARGENT**************************************************************** \n\n")
    
    print("\t\t\t[1]-Envoyer vers un client YANNKO\n\n\t\t\t[2]-Envoyer vers autre banque\n")
    
    reponse=int(input("Tapez \t"))
    
    if (reponse==1) :

       os.system("clear")

       print("\n\t\tEntrer le numero de telephone du Bénéficiaire\t")
    
       RECHERCHE_TRANS()
    
    elif (reponse==2) :

        os.system("clear")
    
        print("\n \t\tCe service n'est pas encore disponible \n")
    
    else:

        os.system("clear")
    
        print("\tMerci \n\n")

        quit()

               # FONCTION DE RETRAIT 

def retrait():
    
    os.system("clear")
    
    print("\t\t\t****************BIENVENUE DANS LE MENU RETRAIT D ARGENT***************************** \n\n")
    
    print("\t\tCombien voulez vous retirer ?\n\n")
    
    somme=float(input("\n\n"))

    os.system("clear")
    
    NUMERO_TELEPHONE=int(input(f"\nEntrez le numero de telephone où sera retirer la somme de {somme} FCFA\n"))

    precedent = int(input("\n\n\t  0.Retour \n\n\t 9.Quitter \n"))

    if (precedent == 0) :

        main()

    elif (precedent == 9) :

        os.system("clear")

        quit()

                # FONCTION POUR VOIR MON SOLDE 

def solde ():
    
    os.system("clear")
    
    print("\t\t\t****************BIENVENUE DANS LE MENU MON SOLDE**************************** \n\n")
    
    print("\t\tEntrez votre numero de compte \t")
    
    NUMERO_COMPTE=int(input(""))

    numero_telephone = int (input('\n\n\t\tEntrez votre numero de telephone\n'))

    os.system("clear")

    if os.path.exists("donnee.db") :
            
            connection = sqlite3.connect("donnee.db")
            
            curseur = connection.cursor()

            requette = f"SELECT * FROM compte WHERE telephone = ? "

            curseur.execute(requette,(numero_telephone,))

            resultat_affichage = curseur.fetchone()

            print("---------------------------------------------Menu solde -----------------------------------------------\n\n")

            print('\nMr/Mm',resultat_affichage[3])

            print('\nSolde : ',resultat_affichage[1],"FCFA")

            print("----------------------------------------------------------------------------------------------------------------\n")

            connection.commit()

            connection.close()


    precedent = int(input("\n\n\t  0.Retour \n\n\t 9.Quitter \n"))

    if (precedent == 0) :

        main()

    elif (precedent == 9) :

        os.system("clear")

        quit()

    else :
        
        print("Cette fonctionnalité n'est pas dispo !")

        quit()

                # FONCTION POUR AFFICHER MON COMPTE 
                
def mon_compte () :
    
    os.system("clear")
    
    print("\t\t\t****************BIENVENUE DANS LE MENU MON COMPTE***************************** \n\n")
    
    print("\t\t\t[1]-Information sur un compte \n\n\t\t\t[2]-Modifier une information sur un compte\n\n\t\t\t[3]-Supprimer mon compte YANNKO\n\n")
    
    choix=int(input("Tapez\t"))
    
    if (choix==1) :

        os.system("clear")

        print("\n\t\tEntrez votre N° de telephone \t")

        information_compte ()

    elif (choix==2):

        os.system("clear")

        NUMERO_TELEPHONE=int(input("Entrez votre N° de telephone du client que vous voulez modifier les informations le concernant \n"))
    
    elif (choix==3) :

        os.system("clear")

        print("\t\tEntrez le N° de telephone du client que vous voulez supprimer \n")

        supprimer()
    
    else :
    
        os.system("clear")

        print("\n Merci de ressayez plus tard \n")

            # FONCTION PRINCIPAL
def main () :

    while True   :
    
        os.system("clear")
    
        print("\n******************************************************** BIENVENUE CHEZ YANNKO BANQUE ********************************************************\n\n")
    
        print("\t\t\t\t\t\t\tMENU\n\n")
    
        print("[1]-CREER UN COMPTE\n\n[2]-VERSEMENT\n\n[3]-TRANSFERT \n\n[4]-RETRAIT\n\n[5]-SOLDE\n\n[6]-MON COMPTE\n\n[7]\a-QUITTER\n\n")
    
        choix=int(input("VOUS CHOISISSEZ\t"))
    
        switch ={1 :creer_compte,2:versement,3:transfert,4:retrait,5:solde,6:mon_compte}
    
        if choix==1 :
    
            switch.get(choix,creer_compte)()
    
        elif choix==2 :
    
            switch.get(choix,versement)()
    
        elif choix==3 :
    
            switch.get(choix,transfert)()
    
        elif choix==4 :
    
            switch.get(choix,retrait)()
    
        elif choix==5 :
    
            switch.get(choix,solde)()
    
        elif choix==6 :
    
            switch.get(choix,mon_compte)()
    
        else :
    
            print("\n----------------------------------------------  MERCI  -------------------------------------------------------------\n")
           
            quit()
        
        break

main()
