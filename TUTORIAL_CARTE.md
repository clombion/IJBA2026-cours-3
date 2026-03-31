# 🗺️ Tutoriel : Créer une carte interactive avec Leaflet & GitHub Pages

Ce guide explique comment transformer un fichier CSV contenant des adresses ou des coordonnées GPS en une carte web dynamique, sans base de données complexe, et la déployer gratuitement.

## 1. Préparation des données (Le CSV)
Avant de coder, analysez votre fichier CSV.
*   **Coordonnées** : Assurez-vous d'avoir des colonnes `latitude` et `longitude`.
*   **Attention aux doublons** : Si votre CSV a plusieurs colonnes avec le même nom (comme c'était le cas ici), il faudra accéder aux données par leur **index numérique** (0, 1, 2...) plutôt que par leur nom.
*   **Hébergement** : Le fichier CSV doit être dans le même dossier que votre fichier `index.html` sur GitHub.

## 2. Structure de base de la carte (HTML/CSS)
Créez un fichier `index.html`. Nous utilisons **Leaflet**, la bibliothèque référence pour les cartes web.

```html
<!DOCTYPE html>
<html>
<head>
    <title>Ma Carte Interactive</title>
    <link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
    <style>
        #map { height: 100vh; width: 100%; } /* La carte prend tout l'écran */
        body { margin: 0; }
    </style>
</head>
<body>
    <div id="map"></div>
    
    <!-- Scripts nécessaires -->
    <script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
    
    <script>
        // Initialisation : [Latitude, Longitude], Zoom
        var map = L.map('map').setView([44.837, -0.579], 12);

        // Fond de carte (CartoDB Positron pour un style sobre)
        L.tileLayer('https://{s}.basemaps.cartocdn.com/light_all/{z}/{x}/{y}{r}.png', {
            attribution: '© OpenStreetMap'
        }).addTo(map);
    </script>
</body>
</html>
```

## 3. Chargement des données CSV (PapaParse)
Plutôt que de convertir manuellement le CSV en JSON, on utilise **PapaParse** pour le lire en direct depuis le navigateur.

```javascript
Papa.parse('votre_fichier.csv', {
    download: true,
    header: false, // On utilise false si on a des doublons de noms de colonnes
    skipEmptyLines: true,
    complete: function(results) {
        const data = results.data.slice(1); // On enlève la ligne d'en-tête
        
        data.forEach(function(row) {
            const lat = parseFloat(row[18]); // Index de la colonne Latitude
            const lon = parseFloat(row[19]); // Index de la colonne Longitude

            if (!isNaN(lat) && !isNaN(lon)) {
                // Création d'un point (CircleMarker)
                L.circleMarker([lat, lon], {
                    radius: 6,
                    fillColor: "#ff7800",
                    color: "#000",
                    weight: 1,
                    fillOpacity: 0.8
                }).addTo(map)
                  .bindPopup(`<b>${row[1]}</b><br>${row[9]}`); // Popup avec nom et adresse
            }
        });
    }
});
```

## 4. Ajout de contexte géographique (Contours GeoJSON)
Pour rendre la carte plus professionnelle, on peut ajouter les limites administratives (ex: le contour d'une métropole).

```javascript
fetch('https://raw.githubusercontent.com/.../communes.geojson')
    .then(res => res.json())
    .then(data => {
        L.geoJSON(data, {
            style: {
                color: "#333",
                weight: 2,
                fillOpacity: 0,
                dashArray: '5, 5' // Ligne pointillée
            }
        }).addTo(map);
    });
```

## 5. Déploiement sur GitHub Pages
C'est l'étape qui rend votre carte publique et accessible via une URL.

1.  **Versionner** : Envoyez vos fichiers (`index.html` et le `.csv`) sur votre dépôt GitHub.
    ```bash
    git add .
    git commit -m "Déploiement de la carte"
    git push origin main
    ```
2.  **Activer Pages** : 
    *   Allez sur votre dépôt GitHub sur le web.
    *   **Settings** > **Pages**.
    *   Sous "Build and deployment", choisissez la branche `main` et le dossier `/ (root)`.
    *   Enregistrez.
3.  **Accéder à la carte** : Votre carte sera disponible sous quelques minutes à l'adresse :
    `https://votre-pseudo.github.io/votre-repo/`

## 💡 Conseils de pro
*   **Performance** : Leaflet supporte bien jusqu'à 1000-2000 points. Au-delà, utilisez des "Clusters" (regroupements de points).
*   **Accessibilité** : Testez toujours votre carte sur mobile, les popups doivent rester lisibles.
*   **Fonds de carte** : Vous pouvez changer le style de la carte sur [Leaflet Provider Demo](https://leaflet-extras.github.io/leaflet-providers/preview/).
