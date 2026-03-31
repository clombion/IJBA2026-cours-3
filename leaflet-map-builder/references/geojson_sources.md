# 🌍 Sources GeoJSON pour la France

Voici des sources fiables pour récupérer les contours administratifs au format GeoJSON, indispensables pour l'habillage de vos cartes.

## 1. France GeoJSON (Grégoire David)
Dépôt très complet et facile d'accès via GitHub raw.
- **Communes de la Gironde (33)** : `https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements/33-gironde/communes-33-gironde.geojson`
- **Départements français** : `https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/departements.geojson`
- **Régions** : `https://raw.githubusercontent.com/gregoiredavid/france-geojson/master/regions.geojson`

## 2. Portails Open Data locaux (Bordeaux Métropole)
Pour des données plus fines ou thématiques (quartiers, zones QPV).
- **Portail Open Data Bordeaux Métropole** : `https://opendata.bordeaux-metropole.fr/`
- Rechercher le format "GeoJSON" dans l'onglet Export.

## 3. Data.gouv.fr (Contours officiels)
Les données d'Etalab, format IGN.
- **Contours des communes (Admin Express)** : `https://www.data.gouv.fr/fr/datasets/contours-des-communes-de-france-simplifie-avec-regions-et-departement-overpass-turbo/`

## 💡 Conseil technique
Pour charger ces fichiers dans Leaflet :
```javascript
fetch('URL_DU_GEOJSON')
    .then(res => res.json())
    .then(data => {
        L.geoJSON(data, {
            style: { color: "#2c3e50", weight: 2, fillOpacity: 0.05 }
        }).addTo(map);
    });
```
