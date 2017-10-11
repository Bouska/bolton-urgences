# bolton-urgences

Bolton est un projet qui a pour but de centraliser l'état des services d'urgences de France en temps réel et se découpe en deux sous-objectifs :
- Une API et un format standardisé pour récupérer l'état des services d'urgences ;
- Un site web basique affichant les données de l'API à la façon de [doctr.ca](https://www.doctr.ca/).

## Statut
Pour l'instant, j'ai [listé](ENDPOINTS.md) tous les services d'urgences français qui diffuse en temps réel leur temps d'attente et leur nombre de patient en attente, avec un scraper primitif si besoin.  

## Roadmap
La prochaine étape est de spécifier un format pour définir un service d'urgence (basé sur le [schéma hospital](https://schema.org/Hospital) ?) et son état.
