# 🗺️ Stratégie & Technique : Créer une carte interactive avec l'IA

Ce guide est un aide-mémoire complet pour piloter une IA (comme Gemini ou ChatGPT) afin de transformer un fichier CSV brut en une carte interactive professionnelle déployée sur GitHub Pages.

---

## I. Guide de Pilotage : Comment diriger l'IA ?

Pour obtenir un résultat de qualité "journalisme de données", ne demandez pas tout d'un coup. Suivez ces étapes de dialogue avec l'IA :

1.  **Phase de Diagnostic :** Demandez d'abord une description détaillée du CSV ("Décris-moi ce CSV"). L'IA doit identifier les colonnes et les erreurs potentielles (doublons de noms, colonnes vides).
2.  **Phase d'Angle d'Analyse :** Exposez votre hypothèse (ex: "Je pense que l'offre est insuffisante"). Demandez quelles colonnes sont les plus pertinentes pour prouver ce point.
3.  **Phase de Nettoyage :** Demandez un script Python pour extraire une statistique précise (ex: compter les niveaux de service). Cela crée une base de données propre.
4.  **Phase de Prototypage :** Demandez une carte Leaflet avec deux contraintes :
    *   Lecture **directe** du CSV (via PapaParse).
    *   Un style **sobre** (ex: CartoDB Positron au lieu d'OpenStreetMap standard).
5.  **Phase de Raffinement Visuel :** Demandez de remplacer les icônes par des points (`CircleMarker`) pour mieux voir la densité, et d'ajouter le contour GeoJSON du territoire (ex: Bordeaux Métropole).
6.  **Phase de Déploiement :** Demandez à l'IA de "pusher" les fichiers sur GitHub pour activer la visualisation en ligne.

---

## II. Fiche Technique (Aide-mémoire Code)

### 1. Structure HTML/JS de base
Utilisez **Leaflet** pour la carte et **PapaParse** pour lire le CSV sans base de données.

```html
<!-- Bibliothèques à inclure dans le <head> ou avant </body> -->
<link rel="stylesheet" href="https://unpkg.com/leaflet@1.9.4/dist/leaflet.css" />
<script src="https://unpkg.com/leaflet@1.9.4/dist/leaflet.js"></script>
<script src="https://cdnjs.cloudflare.com/ajax/libs/PapaParse/5.3.0/papaparse.min.js"></script>
```

### 2. Lecture du CSV (Le piège des index)
Si votre CSV a des colonnes en doublon, forcez l'IA à utiliser les **index numériques** des colonnes plutôt que leurs noms :

```javascript
Papa.parse('data.csv', {
    download: true,
    header: false, // Important si noms de colonnes en doublon
    complete: function(results) {
        const data = results.data.slice(1); // On ignore l'en-tête
        data.forEach(row => {
            const lat = parseFloat(row[18]); // Index de la latitude
            const lon = parseFloat(row[19]); // Index de la longitude
            // ... création du point sur la carte
        });
    }
});
```

### 3. Style Visuel (Points vs Icônes)
Pour une carte de densité, préférez les `CircleMarker` aux marqueurs classiques :

```javascript
L.circleMarker([lat, lon], {
    radius: 6,
    fillColor: "#e67e22",
    color: "#d35400",
    weight: 1,
    fillOpacity: 0.8
}).addTo(map);
```

### 4. Contour Géographique (GeoJSON)
Ajoutez une couche de contexte pour délimiter votre zone d'étude :

```javascript
fetch('url_du_fichier.geojson')
    .then(res => res.json())
    .then(data => {
        L.geoJSON(data, {
            style: { color: "#2c3e50", weight: 2, fillOpacity: 0.05, dashArray: '5, 5' }
        }).addTo(map);
    });
```

---

## III. Déploiement GitHub Pages

1.  Vérifiez que `index.html` et votre `.csv` sont à la racine du dépôt.
2.  Allez dans **Settings > Pages** sur GitHub.
3.  Sélectionnez la branche `main` et cliquez sur **Save**.
4.  L'URL de votre carte sera : `https://[votre-pseudo].github.io/[nom-du-repo]/`
