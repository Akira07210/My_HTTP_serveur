import os
import csv
import datetime


def log_the_visit_in_CSV(informations):
    # Création de mon chemin vers le fichier log
    date = datetime.datetime.now().strftime('%d_%m')
    file_name = date + "_log_visits.csv"
    folder = "./logs"
    os.makedirs(folder, exist_ok=True)
    
    # Chemin final vers le fichier log
    file_path = os.path.join(folder, file_name)



    #################################################################################################
    ######################### Vérifier si le fichier log existe déja ################################
    need_w = True 
    fieldnames = ['Heure','IP','page','Agent','screen']

    try:    
        with open(file_path, "r", encoding="utf-8") as f:
            premiere_ligne = f.readline()
        decoupe = [champ.strip() for champ in premiere_ligne.split(";")]
        if decoupe == fieldnames:
            need_w = False      
    except:
        pass
        
    if need_w: 
        try:
            with open(file_path, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')
                writer.writeheader()
        except Exception as e:
            self.log(f"Erreur création fichier: {e}")
            self.reset_ui()
            
    
    #################################################################################################
    ################################ Ecriture dans le fichier #######################################
    
    try:
        with open(file_path, 'a', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=';')            
            writer.writerow(informations)
    except Exception as e: 
        print("Erreur ecriture : ",e) 
                
                
                