import socket
import sys
import ssl

# Définition de la classe Client
class Client:

    # Initialisation des attributs
    def __init__(self, IP, PORT, BUFFER):
        self.IP = IP
        self.PORT = PORT
        self.BUFFER = BUFFER

    # Méthode de connexion TCP au serveur
    def connexion(self):

        # Initialisation de la connexion au serveur
        try:
            TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            
            # Création de la variable d'encryption
            context = ssl.create_default_context(ssl.Purpose.SERVER_AUTH)

            # Chargement du certificat
            context.load_verify_locations("domain.crt")

            # Pas d'utilisation de nom d'hôte reconnu
            context.check_hostname = False

            # Pas de vérification d'authenticité du certificat
            context.verify_mode = ssl.CERT_NONE

            # Encryption de la communication
            TLS_TCP = context.wrap_socket(TCP, server_hostname=self.IP)
            
        except socket.error:
            print("Erreur de connexion")
            sys.exit()

        # Connexion avec l'IP et le port souhaités
        TLS_TCP.connect((self.IP, self.PORT))
        print("Connexion établie avec le serveur.")

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

        # Fermeture de la socket après avoir quitté la boucle
        TLS_TCP.close()
        print("Connexion fermée.")

# Paramètres utilisés lors de la connexion, et choisis par l'utilisateur
SERVEUR_IP = str(input("Entrez l'@ IP du serveur : "))
SERVEUR_PORT = int(input("Entrez le port du serveur : "))
BUFFER = 1024

# Instanciation de la classe avec les paramètres entrés précédemment
client = Client(SERVEUR_IP, SERVEUR_PORT, BUFFER)

# Appel de la méthode de connexion avec les valeurs des paramètres entrés
client.connexion()
