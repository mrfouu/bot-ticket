# Bot Discord - Gestion de Tickets et Salons Vocaux

Ce projet est un bot Discord polyvalent conçu pour gérer des tickets d'assistance, des salons vocaux dynamiques, et bien plus. Il est développé en Python avec la bibliothèque `discord.py`.

## Fonctionnalités principales

### 1. Gestion des Tickets
- **Panneau de tickets** : Permet aux utilisateurs de créer différents types de tickets via un panneau interactif.
  - Types de tickets disponibles :
    - Création de bot personnalisé
    - Premium Bot
    - Support général
- **Gestion des tickets** :
  - Ouverture de tickets dans des salons privés nommés `ticket-[nom-utilisateur]`.
  - Bouton interactif pour fermer un ticket.

### 2. Salons Vocaux Dynamiques
- **Création automatique de salons vocaux** :
  - Lorsque qu'un utilisateur rejoint un salon vocal "hub", un salon vocal temporaire est créé en son nom.
  - Suppression automatique du salon temporaire lorsque tous les utilisateurs le quittent.
- **Configuration multi-hubs** : Possibilité de définir plusieurs hubs vocaux pour la gestion des salons dynamiques.

### 3. Commandes Diverses
- **Rich Presence** : Affichage personnalisé "Écoute PNL".
- **Publicité Discord** : Commande pour envoyer une publicité dédiée à un serveur Discord spécifique.

## Installation

### Prérequis
- Python 3.9 ou supérieur.
- La bibliothèque `discord.py` version 2.0 ou supérieure.

### Étapes d'installation
1. Clonez le dépôt :
   ```bash
   git clone <URL-du-dépôt>
   cd <nom-du-dossier>
   ```
2. Installez les dépendances nécessaires :
   ```bash
   pip install -r requirements.txt
   ```
3. Configurez le fichier `config.json` avec votre token Discord :
   ```json
   {
       "token": "VOTRE_TOKEN",
       "prefix": "!"
   }
   ```
4. Démarrez le bot :
   ```bash
   python bot.py
   ```

## Structure du Projet

```
<racine-du-projet>/
├── cogs/
│   ├── ticket.py            # Gestion des tickets
│   ├── ticket_panel.py      # Panneau de tickets interactif
│   ├── autovoice.py         # Gestion des salons vocaux dynamiques
│   └── publicité.py         # Commande de publicité pour serveur
├── bot.py                   # Fichier principal pour démarrer le bot
├── config.json              # Configuration du bot
├── requirements.txt         # Dépendances Python nécessaires
└── README.md                # Documentation du projet
```

## Commandes Disponibles

### Catégorie : Tickets
- `!openticket` : Crée un nouveau ticket.
- `!closeticket` : Ferme le ticket en cours.
- `!ticketpanel` : Affiche le panneau des tickets.

### Catégorie : Gestion des Vocaux
- Pas de commande explicite, le comportement est automatique.

### Catégorie : Divers
- `!Sinistros` : Envoie une publicité pour un serveur Discord.

## Contributions
Les contributions sont les bienvenues ! Si vous trouvez un bug ou souhaitez proposer une nouvelle fonctionnalité, n'hésitez pas à ouvrir une issue ou une pull request.

## Licence
Ce projet est sous licence MIT. Voir le fichier `LICENSE` pour plus de détails.

## Auteur
[**Mrfou**](https://github.com/mrfouu)