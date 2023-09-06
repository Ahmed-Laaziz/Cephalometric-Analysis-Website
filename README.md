<div align="center">
  <h1>🌟 Medical 🌟 - We care about your health </h1>
</div>


<div align="center">
  <img src="https://media.licdn.com/dms/image/D5612AQGwC94DVIlNTg/article-cover_image-shrink_600_2000/0/1672179883165?e=2147483647&v=beta&t=FU51Ux0Z1DOip-gjtlIGopC9aS41ADPbSAdHtdgVuJI" alt="Screenshot-2023-09-05-205414" border="0">
</div>

# Contexte général du projet
La radiographie céphalométrique est couramment utilisée comme outil standard dans
le diagnostic orthodontique et la planification du traitement, ainsi que dans la planification de la chirurgie corrective et plastique. Le marquage des repères anatomiques du
crâne et des tissus mous environnants dans les céphalogrammes latéraux est une partie
essentielle du processus de diagnostic et de planification. Les repères céphalométriquessont 
utilisés pour un certain nombre d’analyses orthodontiques (par exemple Schwarz,
Steiner, Ricketts) où plusieurs mesures linéaires et angulaires sont calculées à partir de
leurs positions. La précision avec laquelle les repères sont situés a un impact direct sur
les résultats des analyses effectuées et les décisions de traitement qui en résultent

# Django

Django est un framework web Python open source qui est largement utilisé dans l'industrie pour plusieurs raisons :

1. **Productivité** : Django favorise la productivité des développeurs grâce à son système de gestion des modèles de données, son ORM (Object-Relational Mapping) et son administration automatique de l'interface d'administration. Il permet de créer rapidement des applications web complexes.

2. **Convention** sur la configuration : Django suit le principe "convention over configuration", ce qui signifie que de nombreuses décisions de conception sont prises par défaut. Cela permet aux développeurs de se concentrer sur la logique métier plutôt que de passer du temps à configurer l'application.

3. **Sécurité** : Django est livré avec de nombreuses fonctionnalités de sécurité intégrées pour protéger contre les attaques courantes, telles que la protection contre les injections SQL, la protection contre les attaques CSRF (Cross-Site Request Forgery) et plus encore.

#  Besoins fonctionnels

Les acteurs en interaction avec notre système sont :
* Super-Utilisateur.
* Utilisateurs.
Le Super-Utilisateur peut faire les actions suivantes :
1. Accéder à la base de données.
2.  Gérer la base de données.
L’utilisateur peut faire les actions suivantes :
1.  Remplir les champs requis et puis insérer une image correspondant à une téléradiographie de profile afin d’effectuer des analyses céphalométriques
2. Consulter et télécharger un document sous format PDF qui contient les analyses
médicales qui correspond au patient en question.

# Besoins non-fonctionnels

Notre site doit répondre aux critères suivants :
* Ergonomie :
1.  Interface simple et compréhensible.
2.  Le site doit être développée d’une façon compréhensive par tous les utilisateurs,
présenter les informations d’une façon simple et claire, faire apparaître les choix
ou les saisis des utilisateurs.
*  Performance :
1.  Notre site doit répondre à toutes les exigences des utilisateurs d’une manière
optimale.


#### Conception UML

Voici la conception UML de notre application
*4.1* Diagramme de cas d'utilisation  | *4.2* Diagramme de séquence 
:------------:|:---------------:
![Imgur](https://i.ibb.co/3hRwS79/img12.png)  |  ![Imgur](https://i.ibb.co/jMDCqqL/img13.png) 

# Mode d’emploi
Pour démarrer cette partie front-end( à noter il faut démarrer la partie backend en premier , pour consommer les APIS backend avec Axios) , suivez les étapes suivantes :
1.	Téléchargez le projet sur votre ordinateur
2.	Ouvrez-le dans votre éditeur de code (VScode par exemple)
3.	Tapez sur le terminal les commandes de lignes suivantes : npm start 
4.	Naviguez vou vers : http://localhost:8080/

# Aperçu
Acceuil  |  Champs à remplir pour récupérer des analyses céphalométriques
:-------------:|:----------------:
![Imgur](https://i.ibb.co/j9tqz1C/img14.png)  |  ![Imgur](https://i.ibb.co/Hz9K5XN/img15.png)

 Exemple d’une mauvaise image insérée par l’utilisateur |   Message d’erreur obtenu après la validation
:-------------:|:----------------:
![Imgur](https://i.ibb.co/xHSDmt7/img16.png)  |  ![Imgur](https://i.ibb.co/ZWrSvCC/img17.png)  

 Exemple d’un remplissement des champs |    Les informations personnelles du patient sur la première page du PDF d'analyses
:-------------:|:----------------:
![Imgur](https://i.ibb.co/F4xVcXP/img18.png)  |  ![Imgur](https://i.ibb.co/3fr4fvs/img19.png)  

 Les analyses céphalométriques selon « Downs » |   Les analyses céphalométriques selon « Steiner »
:-------------:|:----------------:
![Imgur](https://i.ibb.co/KyXn3w9/img20.png)  |  ![Imgur](https://i.ibb.co/JQRt8TJ/img21.png)  

 Les analyses céphalométriques qui correspond au patient |   Les interprétations des valeurs des angles céphalométriques récupérées
:-------------:|:----------------:
![Imgur](https://i.ibb.co/9TsbYkZ/img22.png)  |  ![Imgur](https://i.ibb.co/25PW0Mq/img23.png)  

- [Ahmed Laaziz] (mailto:laazizahmed72@gmail.com) - [LinkedIn]([your-linkedin-profile-link](https://www.linkedin.com/in/ahmed-laaziz-4b2168218/))

---

<div align="center">⭐ Don't forget to star this repository if you find it helpful! ⭐</div>
