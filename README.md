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

#### Python
Nous avons choisie de travailler avec Python pour plusieurs raisons. Nous avons tout d'abord fait le projet de machine learning en python, car il est assez simple de manipuler de la donnée avec python et, il est simple de faire des algorithme de machine learning avec. De plus Python possède une bibliothèque pour faire des API qui est [FAST API](https://fastapi.tiangolo.com/). Il fut donc assez simple d'allier les deux ensembles, de plus cela nous évitait de devoir implémenter un autre langage dans le projet.  

#### FAST API 
FAST API est une bibliothèque Python qui permet de faire des API très rapidement en quelques lignes de code. Comme on peut le voir ici : 

![image_code_fast_api](/images/API_code.png)

Faire des pages est assez intuitives se qui permet d'aller vite dans l'apprentissage de cette bibliothèque. 

On peut facilement y implémenter des pages HTML pour améliorer le rendu et que cela soit plus intuitive pour les personnes utilisant FAST API. 


#### HTML5
HTML 5 est un langage extrêmement présent dans la programamtion web. Cela nous permet via des balises de structurer notre page et pouvoir ainsi avoir un meilleur rendu. Ce langage permet de mettre que le possitionnement des éléments sur la page, pour ce qui est de l'aspect et de l'emplacement il va nous falloir utiliser du CSS. 

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



