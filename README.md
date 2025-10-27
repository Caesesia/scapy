# Pseudos

### Caesesia -> `REDACTED`
### Evvvvvvvve -> `REDACTED`
### FlavienSR -> `REDACTED`

<br>

# Etape 1

### Objectifs
<ul>
	<li>Créer une classe client et serveur</li>
	<li>Vérifier la bonne connexion TCP via Wireshark</li>
</ul>

<br>

### Description

Ce projet du module Python pour la Cyber nous initie au scripting Python dans le domaine du réseau, ainsi qu'à la POO (Programmation Orientée Objet).  
L'objectif du projet est d'instaurer une connexion TCP entre une machine client et une machine serveur et vérifier le bon fonctionnement de la connexion en envoyant et recevant des messages, ainsi qu'en gérant les éventuelles erreurs à l'aide du module sys.  

On utilise une classe client et serveur respectivement pour l'aspect POO. Ceci correspond à l'étape 1, et les scripts correspondants peuvent être trouvés dans les répertoires personnels de chaque membre du projet (répertoires "`REDACTED`", "`REDACTED`", "`REDACTED`").  

<br>

### Exécution

Cette étape étant une introduction à la POO et à une simple connexion TCP, elle est relativement simple à exécuter.  
Il suffit simplement d'avoir 2 machines à sa disposition, s'assurer qu'elles puissent communiquer entre elles (les mettre sur le même réseau) à l'aide d'un ping par exemple, puis lancer les scripts.  

On lancera d'abord serveur.py sur la machine serveur désignée (afin d'entamer l'écoute, car c'est toujours le client qui initie la connexion), puis client.py sur la machine client.

Serveur :
```
python serveur.py
```

Client :
```
python client.py
```

<br>

### Vérification

On vérifie le bon fonctionnement de cette connexion et de l'envoi et la réception des messages avec les captures suivantes :

![image alt](https://github.com/Caesesia/RES403/blob/c21b9992794bb7368327b99fa115b22f83f933c5/images/screen1_etape1.png)

![image alt](https://github.com/Caesesia/RES403/blob/c21b9992794bb7368327b99fa115b22f83f933c5/images/screen2_etape1.png)

# Etape 2

### Objectifs
<ul>
    <li>Implémenter du multithreading</li>
    <li>Obtenir plusieurs connexions simultanées</li>
</ul>

<br>

### Description

L'étape suivante consiste à mettre en place du multithreading côté serveur. Le multithreading est la capacité du serveur à générer et gérer plusieurs instances continues et différentes de connexions avec des clients, afin de garantir une disponibilité multiple.  
La modification du script dans cette étape ne concerne donc que le côté serveur, car le client n'a pas à gérer de multithreading.  

<br>

### Exécution

Même chose qu'à l'étape 1, il suffit de s'assurer de la communication entre le client et le serveur, puis lancer serveur.py sur la machine serveur, et client.py sur la machine client.

<br>

### Vérification

On vérifie le fonctionnement du multithreading en lançant un script client.py depuis plusieurs machines vers la même machine serveur, qui doit retourner des informations de connexion pour chaque client en cours.

# Etape 3

### Objectifs
<ul>
    <li>Sécuriser la connexion avec TLS</li>
</ul>

<br>

### Description

Finalement, la dernière étape concerne le chiffrement de la communication avec TLS, afin de rendre les données illisibles pour quelqu'un qui inspecterait les paquets de la connexion.  

Pour cela, nous avons besoin de générer un certificat et une clef privée, qui seront utilisés tant par le client que le serveur pour vérifier l'authenticité du certificat opposé, ainsi que pour prouver leur identité à leur correspondant.
Ces fichiers porteront les extensions .crt et .key respectivement. Un 3ème fichier est présent, avec l'extension .csr : il correspond au Certificate Signing Request, qui contient des informations utilisée par l'Autorité de Certificat afin d'obtenir un certificat SSL/TLS reconnu pour notre domaine (DN).
Comme nous sommes sur un projet purement utilisé en testing local, nous n'avons pas de DN et n'utilisons donc pas de certificat validé par le CA (Certificate Authority) pour chiffrer la communication : notre propre certificat auto-signé suffit amplement.

<br>

### Exécution

Encore une fois, même chose que pour les étapes 1 et 2, seulement le mot de passe PEM pour le cryptage est "test" (à entrer lors du lancement de serveur.py).

<br>

### Vérification

![image alt](https://github.com/Caesesia/RES403/blob/c21b9992794bb7368327b99fa115b22f83f933c5/images/screen1_etape3.png)

![image alt](https://github.com/Caesesia/RES403/blob/c21b9992794bb7368327b99fa115b22f83f933c5/images/screen2_etape3.png)
Nous pouvons voir que c'est bien chiffré

# <i>Bonus</i>
<ul>
    <li>Utiliser Diffie-Hellman</li>
</ul>
