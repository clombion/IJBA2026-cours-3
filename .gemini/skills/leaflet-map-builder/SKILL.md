---
name: leaflet-map-builder
description: Guide de création de cartes Leaflet interactives à partir de fichiers CSV et déploiement sur GitHub Pages. Utilisez ce skill pour transformer des données tabulaires en visualisations géographiques avec PapaParse, GeoJSON et une stratégie de pilotage structurée.
---

# 🗺️ Leaflet Map Builder

Ce skill automatise le processus de création de cartes de données (DataViz) pour le web. Il suit une approche progressive allant du diagnostic des données au déploiement final.

## 🛠️ Workflow de Pilotage

Suivez ces phases de manière séquentielle pour garantir un résultat professionnel :

### 1. Phase de Diagnostic (CSV)
Analysez la structure brute du fichier avant de coder quoi que ce soit.
- Utilisez `scripts/diagnose_csv.py` pour identifier :
    - Les noms et index des colonnes.
    - La présence de doublons (ex: deux colonnes "latitude").
    - La validité des coordonnées GPS.

### 2. Phase d'Angle d'Analyse (Stratégie)
Définissez la problématique avec l'utilisateur (ex: hypothèse de désert numérique ou de concentration de l'offre).
- Identifiez les colonnes "métier" à mettre en avant (tarifs, services, publics cibles).

### 3. Phase de Nettoyage (Scripting)
Si le CSV est complexe, créez un script Python pour :
- Agréger des données (ex: compter des occurrences).
- Simplifier le format pour l'affichage web.
- Nettoyer les doublons ou les cellules vides.

### 4. Phase de Prototypage (Leaflet)
Utilisez l'asset `assets/template_map.html` comme base.
- **Contrainte 1** : Lecture directe du CSV via `PapaParse`.
- **Contrainte 2** : Fond de carte sobre (CartoDB Positron recommandé pour une meilleure lisibilité).
- **Contrainte 3** : Gestion des index numériques (`row[index]`) si le CSV a des noms de colonnes en doublon.

### 5. Phase de Raffinement (UX/UI)
Améliorez la lecture de la carte :
- Remplacez les marqueurs icônes par des `CircleMarker`.
- Ajoutez un contour GeoJSON pour délimiter le territoire (consultez `references/geojson_sources.md`).
- Personnalisez les popups avec des informations utiles.

### 6. Phase de Déploiement (GitHub Pages)
Finalisez la mise en ligne :
- Poussez `index.html` et le CSV sur le dépôt.
- Guidez l'utilisateur pour activer GitHub Pages dans les réglages du repo.

## 📦 Ressources incluses

- **Scripts** : `scripts/diagnose_csv.py` - Analyseur de structure CSV.
- **Assets** : `assets/template_map.html` - Boilerplate Leaflet + PapaParse.
- **Références** : `references/geojson_sources.md` - Liens vers les GeoJSON administratifs français.
