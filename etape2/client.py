import socket
import sys


# Définition de la classe Client
class Client:

    # Initialisation des attributs
    def __init__(self, IP, PORT, BUFFER, MSG):
        self.IP = IP
        self.PORT = PORT
        self.BUFFER = BUFFER
        self.MSG = MSG

    # Méthode de connexion TCP au serveur
    def connexion(self):

        # Initialisation de la connexion au serveur
        try :
            TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error :
            sys.exit();

        # Connexion avec l'IP et le port souhaités
        TCP.connect((self.IP, self.PORT))

	# Boucle d'envoi et de réception des messages
        while True:
            # Demande de message à l'utilisateur
            message = input("Entrez le message à envoyer (ou 'exit' pour quitter) : ")

            if message.lower() == 'exit':
                print("Déconnexion...")
                break  # Sortir de la boucle si l'utilisateur entre 'exit'

            # Envoi du message au serveur
            try:
                TLS_TCP.send(message.encode('utf8'))
                print("Message envoyé au serveur.")
            except socket.error:
                print("Erreur lors de l'envoi du message.")
                break

            # Récupération de la réponse du serveur, limitée par le buffer
            try:
                data = TLS_TCP.recv(self.BUFFER)
                print(f"Réponse du serveur : {data.decode('utf8')}")
            except socket.error:
                print("Erreur lors de la réception des données.")
                break

        # Fermeture de la socket
        TCP.close()

        print('Réponse du serveur : ', data)



# Paramètres utilisés lors de la connexion, et choisis par l'utilisateur
SERVEUR_IP = str(input("Entrez l'@ IP du serveur : "))
SERVEUR_PORT = 80
BUFFER = 1024
MESSAGE = str(input("Veuillez entrer le message à envoyer au serveur : "))


# Instanciation de la classe avec les paramètres entrés précédemment
client = Client(SERVEUR_IP, SERVEUR_PORT, BUFFER, MESSAGE)

# Appel de la méthode de connexion avec les valeurs des paramètres entrés
client.connexion()
