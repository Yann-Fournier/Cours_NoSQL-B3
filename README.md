# Cours de NoSQL

- Mes données sont stockées dans des fichiers csv dans le dossier CSV
- Vous pouvez utilisée le code ce trouvant dans le dossier MongoDB pour remplir votre base de données
- Le code de l'API ce trouve dans le dossier API. Il faut installer les dépendances python présentent dans le fichier requirements.txt à la racine du répo.

### API documentation 

---

- 1 - **GET** http://localhost:5000/get_books

Permet de récupérer les informations de tous les livres.
Aucun paramètre ne doit être spécifier.

- 2 - **GET** http://localhost:5000/get_book_by_id

Permet de récupérer les information d'un livre en fonction de son identifiant

Paramètre :

Nom | Valeur | Type
--- | --- | ---
id | Chaîne de caractère | Obligatoire

- 3 - **POST** http://localhost:5000/add_book

Permet d'ajouter un livre dans la base de données

Paramètres :

Nom | Valeur | Type
--- | --- | ---
Nom | Chaîne de caractère | Obligatoire
Prix | Nombre (Il faut utiliser un point pour les nombres à virgule) | Obligatoire
Description | Chaîne de caractère | Obligatoire
Isbn | Chaîne de caractère | Obligatoire
Photo | Chaîne de caractère | Obligatoire
Editeur | Chaîne de caractère | Obligatoire
Categorie | Chaîne de caractère | Obligatoire

- 4 - **DELETE** http://localhost:5000/delete_book

Permet de supprimer un livre 

Paramètre :

Nom | Valeur | Type
--- | --- | ---
id | Chaîne de caractère | Obligatoire

- 5 - **PUT** http://localhost:5000/update_book

Permet de modifier les information d'un livre

Paramètres :

Nom | Valeur | Type
--- | --- | ---
id | Chaîne de caractère | Obligatoire
Nom | Chaîne de caractère | Facultatif
Prix | Nombre (Il faut utiliser un point pour les nombres à virgule) | Facultatif
Description | Chaîne de caractère | Facultatif
Isbn | Chaîne de caractère | Facultatif
Photo | Chaîne de caractère | Facultatif
Editeur | Chaîne de caractère | Facultatif
Categorie | Chaîne de caractère | Facultatif
