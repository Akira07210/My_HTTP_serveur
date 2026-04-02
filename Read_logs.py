# 1) Récolter les colonnes à print.
# 2) Parcourir la première ligne pour trouver les colonnes à afficher. 
# 3) Parcourir toutes les autres lignes en printant les colonnes.
# 4) Recommencer.

import sys
import csv

dessin = r'''
--------------------------------------   ----------------------------------------------    ---------
----------------------     ----------------------------  ---------    ----------------   -----------
-------    -----------------------------------  ----------------------------------------------------
`7MM"""Mq.                       `7MM                                     `7MM                     
  MM   `MM.                        MM                                       MM                     
  MM   ,M9  .gP"Ya   ,6"Yb.   ,M""bMM      `7MMpMMMb.pMMMb.`7M'   `MF'      MM  ,pW"Wq.   .P"Ybmmm 
  MMmmdM9  ,M'   Yb 8)   MM ,AP    MM        MM    MM    MM  VA   ,V        MM 6W'   `Wb :MI  I8   
  MM  YM.  8M""""""  ,pm9MM 8MI    MM        MM    MM    MM   VA ,V         MM 8M     M8  WmmmP"   
  MM   `Mb.YM.    , 8M   MM `Mb    MM        MM    MM    MM    VVV          MM YA.   ,A9 8M        
.JMML. .JMM.`Mbmmd' `Moo9^Yo.`Wbmd"MML.    .JMML  JMML  JMML.  ,V         .JMML.`Ybmd9'   YMMMMMb  
                                                              ,V                         6'     dP 
                                                           OOb"                          Ybmmmd'   
---------------------------------------------------------------------------------------------------'''
                                                           
print(dessin)

if len(sys.argv)>1 : 
    file_path = sys.argv[1]
else :
    print("Vous devez donner le chemin du fichier CSV à lire en paramètre.")
    exit()
while 1 :
    # 1) Récolter les colonnes à print.
    print("Veuillez renseigner vos noms de colonnes à afficher.\nLorsque vous avez fini appuyez sur enter.")
    entre_utilisateur = None
    tableau_utilisateur = []
    while entre_utilisateur != "":
        entre_utilisateur=input()
        if entre_utilisateur.strip().lower() !="" and entre_utilisateur.strip().lower() != "my head" : 
            tableau_utilisateur.append(entre_utilisateur.strip().lower())
        if entre_utilisateur.strip().lower() == "my head" : 
            with open(file_path, "r", encoding="utf-8") as f:
                premiere_ligne = f.readline()
            print("Clonnes du fichier : ")
            print([champ.strip() for champ in premiere_ligne.split(";")])
        if entre_utilisateur.strip().lower() == "exit" : 
            exit()
            
    
    
    # 2) Parcourir la première ligne pour trouver les colonnes à afficher. 
    # 3) Parcourir toutes les autres lignes en printant les colonnes.
    tab_int_colonne_a_print = []
    first_line = True
    with open(file_path,"r", encoding="utf-8") as f:
        for line in f:  
            decoupe = [champ.strip().lower() for champ in line.split(";")]
            if first_line : 
                tab_int_colonne_a_print.extend(i for i in range(0,len(decoupe)) if decoupe[i] in tableau_utilisateur)
                first_line = False
            else : 
                for i in tab_int_colonne_a_print :
                    print(f" | {decoupe[i]}", end = "")
                print(" |")
    # 4) Recommencer.
        
    
    
        
    
    
        
