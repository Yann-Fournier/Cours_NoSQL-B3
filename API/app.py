import flask_cors
import pandas as pd
from bson import ObjectId  # Import nécessaire pour ObjectId
from pymongo import MongoClient
from flask import Flask, request, jsonify

# Connexion à MongoDB
client = MongoClient("mongodb://localhost:27017/Scibio")  # Remplacez par l'URL de votre serveur MongoDB
db = client["NoSQL"]  # Nom de la base de données
collection = db["Livres"]  # Nom de la collection

# Création de l'application
app = Flask(__name__)
app.config["PORT"] = 5000
app.config["HOST"] = "localhost"
app.config["DEBUG"] = True
flask_cors.CORS(app)

# Route GET pour la page d'accueil
@app.route('/', methods=['GET'])
def accueil():
    return "Bienvenue sur la page d'accueil de l'API du cours de NoSQL"

# Route GET pour récupérer tous les livres
@app.route('/get_books', methods=['GET'])
def get_books():
    # Récupérer tous les documents de la collection
    documents = list(collection.find())
    # Transformer en DataFrame
    df = pd.DataFrame(documents)
    # Convertir la colonne "_id" en string
    if '_id' in df.columns:
        df['_id'] = df['_id'].astype(str)
    return df.to_json(orient="records")

# Route GET pour récupérer tous les livres
@app.route('/get_book_by_id', methods=['GET'])
def get_books_by_id():
    id = request.args.get('id')  # Récupérer un paramètre spécifique
    # Récupérer tous les documents de la collection
    documents = list(collection.find({"_id": ObjectId(id)}))
    # Transformer en DataFrame
    df = pd.DataFrame(documents)
    # Convertir la colonne "_id" en string
    if '_id' in df.columns:
        df['_id'] = df['_id'].astype(str)
    # df.drop(columns=['_id'], inplace=True)  # Supprime la colonne "_id"
    return df.to_json(orient="records")

# Route POST pour ajouter un livre
@app.route('/add_book', methods=['POST'])
def add_book():
    Nom = request.args.get('Nom', default="Aucun nom disponible")  # Récupérer un paramètre spécifique
    Prix = request.args.get('Prix', default="Aucun prix disponible")  # Récupérer un paramètre spécifique
    Description = request.args.get('Description', default="Aucune description disponible")  # Récupérer un paramètre spécifique
    Isbn = request.args.get('Isbn', default="Aucun isbn disponible")  # Récupérer un paramètre spécifique
    Photo = request.args.get('Photo', default="Aucune photo disponible")  # Récupérer un paramètre spécifique
    Editeur = request.args.get('Editeur', default="Aucun éditeur disponible")  # Récupérer un paramètre spécifique
    Categorie = request.args.get('Categorie', default="Aucune categorie disponible")  # Récupérer un paramètre spécifique
    try:
        Prix = float(Prix)
    except ValueError:
        Prix = "Aucun prix disponible"
    # Ajouter le document dans la collection
    collection.insert_one({"Nom": Nom, "Prix": Prix, "Description": Description, "Isbn": Isbn, "Photo": Photo, "Editeur": Editeur, "Categorie": Categorie})
    return "Livre ajouté avec succès"

# Route DELETE pour supprimer un livre
@app.route('/delete_book', methods=['DELETE'])
def delete_book():
    id = request.args.get('id')  # Récupérer un paramètre spécifique
    collection.delete_one({"_id": ObjectId(id)})
    return "Livre supprimé avec succès"

# Route PUT pour mettre à jour un livre
@app.route('/update_book', methods=['PUT'])
def update_book():
    id = request.args.get('id')  # Récupérer un paramètre spécifique
    Nom = request.args.get('Nom')  # Récupérer un paramètre spécifique
    Prix = request.args.get('Prix')  # Récupérer un paramètre spécifique
    Description = request.args.get('Description')  # Récupérer un paramètre spécifique
    Isbn = request.args.get('Isbn')  # Récupérer un paramètre spécifique
    Photo = request.args.get('Photo')  # Récupérer un paramètre spécifique
    Editeur = request.args.get('Editeur')  # Récupérer un paramètre spécifique
    Categorie = request.args.get('Categorie')  # Récupérer un paramètre spécifique
    if Prix is not None:
        try:
            Prix = float(Prix)
        except ValueError:
            Prix = "Aucun prix disponible"
    
    book = {} # Créer un dictionnaire vide
    if Nom is not None: # Vérifier si le paramètre est renseigné
        book["Nom"] = Nom
    if Prix is not None: # Vérifier si le paramètre est renseigné
        book["Prix"] = Prix
    if Description is not None:
        book["Description"] = Description
    if Isbn is not None:
        book["Isbn"] = Isbn
    if Photo is not None:
        book["Photo"] = Photo
    if Editeur is not None:
        book["Editeur"] = Editeur
    if Categorie is not None:
        book["Categorie"] = Categorie
        
    collection.update_one({"_id": ObjectId(id)}, {"$set": book}) # Mettre à jour le document
    return "Livre mis à jour avec succès"

# Lancement de l'application
if __name__ == '__main__':
    app.run(port=app.config["PORT"], host=app.config["HOST"], debug=app.config["DEBUG"])