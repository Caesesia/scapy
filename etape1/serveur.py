import socket
import sys



class Serveur:


    def __init__(self, IP, PORT, BUFFER, MSG):
        self.IP = IP
        self.PORT = PORT
        self.BUFFER = BUFFER
        self.MSG = MSG


    def ecoute(self):


        try :
            TCP = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        except socket.error :
            print('Erreur lors de la création de la socket')
            sys.exit();

        
        TCP.bind((self.IP, self.PORT))

        
        TCP.listen(3)
        print('En écoute...')

        connexion, adresse = TCP.accept()
        print('Connecté avec : ', adresse)


        bytes = connexion.recv(self.BUFFER)
        data = bytes.decode('utf8')

        print('Message reçu du client : ', data)


        connexion.sendall(self.MSG.encode('utf8'))

        connexion.close()




SERVEUR_IP = str(input("Entrez l'@ IP utilisée par le serveur : "))
SERVEUR_PORT = int(input("Entrez le port d'écoute : "))
BUFFER = 1024
MESSAGE = "IV_{4lL0_s3LeM}"

serveur = Serveur(SERVEUR_IP, SERVEUR_PORT, BUFFER, MESSAGE)


serveur.ecoute()
