import socket
import sys
import ssl

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
            
        except socket.error :
            sys.exit();

        # Connexion avec l'IP et le port souhaités
        TLS_TCP.connect((self.IP, self.PORT))

        # Envoi du message désiré au serveur
        try :
            TLS_TCP.send(self.MSG.encode('utf8'))
        except socket.error :
            sys.exit()

        print('Message envoyé au serveur avec succès')

        # Récupération de la réponse du serveur, limitée par le buffer
        data = TLS_TCP.recv(self.BUFFER)

        # Fermeture de la socket
        TLS_TCP.close()

        print('Réponse du serveur : ', data)



# Paramètres utilisés lors de la connexion, et choisis par l'utilisateur
SERVEUR_IP = str(input("Entrez l'@ IP du serveur : "))
SERVEUR_PORT = int(input("Entrez le port du serveur : "))
BUFFER = 1024
MESSAGE = str(input("Veuillez entrer le message à envoyer au serveur : "))


# Instanciation de la classe avec les paramètres entrés précédemment
client = Client(SERVEUR_IP, SERVEUR_PORT, BUFFER, MESSAGE)

# Appel de la méthode de connexion avec les valeurs des paramètres entrés
client.connexion()
