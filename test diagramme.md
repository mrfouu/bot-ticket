### **1. Diagramme ER Structuré en Mermaid.js**

Voici le diagramme ER réorganisé pour ressembler à la structure du projet de bot Discord :

mermaid

Copy

erDiagram
    %% Section 1: Entités principales
    USERS {
        string id
        string first_name
        string last_name
        string email
        string password
        bool is_admin
    }

    PLACES {
        string id
        string title
        text description
        decimal price
        float latitude
        float longitude
        string user_id
    }

    REVIEWS {
        string id
        text text
        int rating
        string user_id
        string place_id
    }

    AMENITIES {
        string id
        string name
    }

    PLACES_AMENITIES {
        string place_id
        string amenity_id
    }

    %% Section 2: Relations entre les entités
    USERS ||--o{ PLACES : "owns"
    USERS ||--o{ REVIEWS : "writes"
    PLACES ||--o{ REVIEWS : "has"
    PLACES }o--o{ AMENITIES : "has"
    PLACES_AMENITIES }o--|| PLACES : "references"
    PLACES_AMENITIES }o--|| AMENITIES : "references"

    %% Section 3: Légendes et descriptions
    note right of USERS
        **USERS** : Table des utilisateurs.
        - Un utilisateur peut posséder plusieurs places.
        - Un utilisateur peut écrire plusieurs reviews.
    end note

    note right of PLACES
        **PLACES** : Table des lieux.
        - Une place appartient à un utilisateur.
        - Une place peut avoir plusieurs reviews.
        - Une place peut avoir plusieurs commodités.
    end note

    note right of REVIEWS
        **REVIEWS** : Table des avis.
        - Un avis est écrit par un utilisateur.
        - Un avis est associé à une place.
    end note

    note right of AMENITIES
        **AMENITIES** : Table des commodités.
        - Une commodité peut être associée à plusieurs places.
    end note

    note right of PLACES_AMENITIES
        **PLACES_AMENITIES** : Table de jointure.
        - Lie une place à une commodité.
    end note

---

### **2. Explication des Modifications**

#### **a. Sections Structurées**

- **Section 1 : Entités principales** : Les tables (`USERS`, `PLACES`, `REVIEWS`, `AMENITIES`, `PLACES_AMENITIES`) sont listées avec leurs attributs.
    
- **Section 2 : Relations entre les entités** : Les relations entre les tables sont clairement définies.
    
- **Section 3 : Légendes et descriptions** : Chaque entité est accompagnée d'une note explicative pour décrire son rôle et ses relations.
    

#### **b. Légendes et Descriptions**

- Les notes (`note right of`) ajoutent des descriptions détaillées pour chaque entité, ce qui rend le diagramme plus **compréhensible** et **professionnel**.
    
- Ces notes sont visibles dans l'éditeur Mermaid.js et peuvent être exportées avec le diagramme.