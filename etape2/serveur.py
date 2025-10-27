import socket
import sys
import threading



class Serveur:


    def __init__(self, IP, PORT, BUFFER, MSG):
        self.IP = IP
        self.PORT = PORT
        self.BUFFER = BUFFER
        self.MSG = MSG


    def gestion(self, connexion, adresse):

        print('Connecté avec : ', adresse)

        # Récupération du message du client
        data = connexion.recv(self.BUFFER)

	if data:
            # Affichage du message du client, accompagné de l'adresse du client
            print(f"Message reçu du client {adresse}: {data.decode('utf8')}")

            # Envoi de la réponse au client avec l'IP et le port du client
            response = f"Message reçu de {adresse}: {self.MSG}"
            connexion.sendall(response.encode('utf8'))

        # Fermeture de la socket
        connexion.close()


    def ecoute(self):

        # Ouverture de la socket TCP d'écoute
        try :
            TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error :
            print('Erreur lors de la création de la socket')
            sys.exit();

        # Liaison de l'IP et du port du serveur à la socket en écoute
        TCP.bind((self.IP, self.PORT))

        # Limite d'écoute simultanée de 3 clients
        TCP.listen(3)
        print('En écoute...')
        
        # Mise en place d'une écoute infinie
        while True:

            # Acceptation de la demande de connexion du client
            connexion, adresse = TCP.accept()
            
            # Démarrage d'un thread pour chaque nouveau client
            client = threading.Thread(target = self.gestion, args = (connexion, adresse))
            client.start()

SERVEUR_IP = str(input("Entrez l'@ IP utilisée par le serveur : "))
SERVEUR_PORT = int(input("Entrez le port d'écoute : "))
BUFFER = 1024
MESSAGE = "IV_{4lL0_s3LeM}"

# Instanciation de l'objet serveur avec les paramètres précédents
serveur = Serveur(SERVEUR_IP, SERVEUR_PORT, BUFFER, MESSAGE)

# Appel de la méthode d'écoute
serveur.ecoute()
