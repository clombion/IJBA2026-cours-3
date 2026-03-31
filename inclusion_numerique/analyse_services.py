import csv
from collections import Counter

def analyser_niveaux_service(input_file, output_file):
    services_counts = {}
    levels = ["Expert", "Maîtrise", "Basique", "Non"]

    try:
        with open(input_file, mode='r', encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                niveau_service = row.get('niveau_service', '')
                if not niveau_service:
                    continue
                
                # On sépare les différents services (ex: "TABLETTE/Expert, ORDI/Maîtrise")
                items = [item.strip() for item in niveau_service.split(',')]
                for item in items:
                    if '/' in item:
                        try:
                            service, niveau = item.split('/', 1)
                            if service not in services_counts:
                                services_counts[service] = Counter()
                            services_counts[service][niveau] += 1
                        except ValueError:
                            continue

        # Écriture du fichier CSV de sortie
        with open(output_file, mode='w', encoding='utf-8', newline='') as f:
            writer = csv.writer(f)
            # En-tête : Service, Expert, Maîtrise, Basique, Non
            writer.writerow(["Service"] + levels)
            
            for service in sorted(services_counts.keys()):
                counts = services_counts[service]
                row = [service] + [counts.get(lvl, 0) for lvl in levels]
                writer.writerow(row)
        
        print(f"✅ Analyse terminée. Fichier généré : {output_file}")

    except FileNotFoundError:
        print(f"❌ Erreur : Le fichier source '{input_file}' est introuvable.")

if __name__ == "__main__":
    INPUT_FILENAME = 'RAW_met_lieux_inclusion_numerique - RAW_met_lieux_inclusion_numerique.csv'
    OUTPUT_FILENAME = 'analyse_services_resultat.csv'
    analyser_niveaux_service(INPUT_FILENAME, OUTPUT_FILENAME)
