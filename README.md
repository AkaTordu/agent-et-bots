# Diagramme de Flux du Chatbot pour Agence Immobilière

## Aperçu

Ce dépôt contient un diagramme Mermaid représentant le flux d'un chatbot conçu pour une agence immobilière. Le chatbot gère les demandes d'ajout de propriétés (appartements, maisons, etc.) à la liste de l'agence et renvoie une acceptation ou un rejet en fonction de critères prédéfinis.

## Diagramme

Le diagramme de flux est créé à l'aide de Mermaid et illustre les étapes suivantes :

1. **Interaction Utilisateur** : L'utilisateur envoie une demande pour ajouter une propriété.
2. **Réception par le Chatbot** : Le chatbot reçoit et analyse la demande.
3. **Détermination du Type de Propriété** : Le chatbot demande le type de propriété (appartement, maison, ou autre).
4. **Validation des Critères** : Pour les appartements et les maisons, le chatbot valide la demande en fonction des critères suivants :
   - Surface >= 40m²
   - Prix <= 500 000€
   - Localisation : Paris ou Lyon
5. **Décision** : Selon la validation :
   - Si les critères sont respectés, la demande est acceptée.
   - Si les critères ne sont pas respectés ou si le type de propriété est 'autre', la demande est rejetée.
6. **Réponse** : Le chatbot envoie une confirmation ou un rejet à l'utilisateur.
