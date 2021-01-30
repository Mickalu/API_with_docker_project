# API_with_docker_project
![Docker image](https://www.docker.com/sites/default/files/d8/styles/role_icon/public/2019-07/horizontal-logo-monochromatic-white.png)


Projet on a API with python and docker

## Un simple Readme sur un projet de cours utilisant à la fois Fast API et Docker.



## Description

Ce projet a pour but d'intégré un projet de machine learning dans une API et de pouvoir le déployer avec Docker. 



### Technologies utilisées

* Docker
* Python
* FAST API
* HTML 5

#### Docker
Docker permet de packager tous les services, scripts, API, librairies dont une application 
a besoin ; on appelle cela un conteneur. L'objectif est de tout réunir pour l'utiliser
sur n'importe quel noyau compatible. Cela permet d'utiliser un seul noyau qui sera partagé
par plusieurs conteneurs. Cela apporte certains avantages comme ajouter de la portabilité 
aux projets ou de moins impacter les performances des serveurs, en un mot donner de l'**agilité**.

**Docker :**

| Avantages | Inconvénients | 
|-----------|---------------|
| Docker prend en charge différents systèmes d’exploitation et plateformes de Cloud.| Le moteur Docker ne prend en charge que son propre format de conteneur. |
| La plateforme Docker offre déjà des outils natifs d’orchestration et de gestion de clusters. | Le logiciel est disponible sous la forme d’un fichier programme monolithique contenant toutes les caractéristiques. |

D'autres outils existent comme Kebernetes ou LXC par exemple.  

Nous avons décidé d'utiliser Docker car c'est un outil Open Source et simple à comprendre et à mettre en place. Il est aussi 
très répandu et utilisé donc nous avons une bonne documentation pour nous aider.

#### Python
Nous avons choisie de travailler avec Python pour plusieurs raisons. Nous avons tout d'abord fait le projet de machine learning en python, car il est assez simple de manipuler de la donnée avec python et, il est simple de faire des algorithme de machine learning avec. De plus Python possède une bibliothèque pour faire des API qui est [FAST API](https://fastapi.tiangolo.com/). Il fut donc assez simple d'allier les deux ensembles, de plus cela nous évitait de devoir implémenter un autre langage dans le projet.  

| Avantages  | Inconvénients |
|----------- |------------- |
| Peut être utilisé pour faire la partie API et la partie projet | Plutot lent pour faire réaliser les algorithmes et afficher les résultats : C++ plus rapide pour la réalisation des algorithmes |
| Langage simple d'utilisation, pas besoin de compilateur car langage interprété donc plus simple à installer | Le langage étant moins exigent en terme d'organisation on peut facilement s'y perdre si mal organisé |


#### FAST API 
FAST API est une bibliothèque Python qui permet de faire des API très rapidement en quelques lignes de code. Comme on peut le voir ici : 

![image_code_fast_api](/images/API_code.png)

Faire des pages est assez intuitives se qui permet d'aller vite dans l'apprentissage de cette bibliothèque. 

On peut facilement y implémenter des pages HTML pour améliorer le rendu et que cela soit plus intuitive pour les personnes utilisant FAST API. 

| Avantages  | Inconvénients |
|----------- |------------- |
| Très simple d'utilisation et assez intuitive | Cela n'est pas fait pour les gros projets en web, on va vite être limité, favorisé la bibliothèque [Django](https://www.djangoproject.com/) à ce moment là.  |
| étant en Python, il est extrêmement simple d'y implémenter des projets qui sont dans le même langage | Contrairement à d'autre bibliothèque, l'architecture de l'API n'est pas imposé, c'est donc au groupe de faire attention à cela |

#### HTML5
HTML 5 est un langage extrêmement présent dans la programamtion web. Cela nous permet via des balises de structurer notre page et pouvoir ainsi avoir un meilleur rendu. Ce langage permet de mettre que le possitionnement des éléments sur la page, pour ce qui est de l'aspect et de l'emplacement il va nous falloir utiliser du CSS. 

| Avantages  | Inconvénients |
|----------- |------------- |
| C'est le langage le plus utilisé pour la créatiion de pages web, il y a donc beaucoup de documentation | Pour une petite API, mettre du HTML est sans doute pas nécesaire, cela va nous faire perdre plus de temps que ajouter une vraie plus value à notre API |
| Peut rendre plus intuitive l'utilisation de notre API | Cela ajoute du volume à notre API |



## architecture

Les dossiers

* data
* function_detection
* templates
* app

#### data 
Ce dossier contient tout les fichiers csv utilent pour l'utilisation des aldorithmes de machine learning.

#### function_detection 
Ce dossier va contenit tous les fichiers python pour le traitement des données, l'entraînement des algorithmes et l'affichage des résultats.

#### templates 
Ce dossier ne va contenir que des fichiers HTML 5, qui vont permettre de créer des pages web dans notre api pour pouvoir ainsi afficher au mieux les résultats.

#### app 
C'est dans ce dossier que l'on va mettre les fichiers pour pouvoir créer et afficher l'API avec FAST API de python. 


## Installation 

#### FAST API 
install FAST API 

        pip install fastapi

install uvicorn 

        pip install uvicorn[standard]

#### Docker
* [docker pour windows](https://docs.docker.com/docker-for-windows/install/)
* [docker pour mac](https://docs.docker.com/docker-for-mac/install/)
* [docker pour linux](https://docs.docker.com/engine/install/)


# ce que nous avons appris

* Docker
* Python
* FAST API
* WSL

#### Docker 

- Utilisation des commandes docker  
- création d'un contener 
- création d'un contener avec une image 
- mettre projet dans un docker container
- lancer un container
- création d'un fichier docker-compose.yml
- créer le Dockerfile

#### Python
- utilisation des threads pour alléger le temps de calcule 

#### FAST API 
- utilisation des requetes get 
- utilisation des requetes post 
- création des pages 
- implémentation de pages HTML 
- implémentation d'une API sur un projet

#### WSL
- Implémenter Ubuntu sur Windows
- Passer de WSL1 à WLS2 
- Autoriser la virtualisation de son CPU et la désactiver
- Décompresser le contenu d'un dossier pour pouvoir installer Ubuntu



        