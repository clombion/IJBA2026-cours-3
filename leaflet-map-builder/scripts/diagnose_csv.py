import csv
import sys

def diagnose_csv(file_path):
    try:
        with open(file_path, mode='r', encoding='utf-8') as f:
            reader = csv.reader(f)
            header = next(reader)
            
            print(f"--- Diagnostic CSV : {file_path} ---")
            print(f"Nombre de colonnes : {len(header)}")
            
            # Analyse des doublons de noms de colonnes
            seen = set()
            duplicates = []
            for i, col in enumerate(header):
                if col in seen:
                    duplicates.append(f"'{col}' (index {i})")
                seen.add(col)
                print(f"Index {i:2} : {col}")
            
            if duplicates:
                print("\n⚠️ ATTENTION : Noms de colonnes en doublon détectés !")
                for d in duplicates:
                    print(f"  - {d}")
                print("\nCONSEIL : Utilisez les index numériques (row[index]) plutôt que les noms dans le script Leaflet.")
            else:
                print("\n✅ Structure des colonnes saine (pas de doublons).")
                
    except Exception as e:
        print(f"Erreur lors du diagnostic : {e}")

if __name__ == "__main__":
    if len(sys.argv) > 1:
        diagnose_csv(sys.argv[1])
    else:
        print("Usage: python diagnose_csv.py <votre_fichier.csv>")
