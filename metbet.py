import time

#donnees entrantes:
mise_totale_sur_joueur1 = 0
mise_totale_sur_joueur2 = 0
nouveauchoix = 1

#analyse niveau de la cote:
while nouveauchoix == 1:
   #donnees entrantes:
  cotepremierjoueur = float(raw_input("entre la cote du premier joueur:"))
  cotedeuxiemejoueur = float(raw_input("entre la cote du deuxieme joueur:"))
  mise_totale_sur_joueur1 = 0
  mise_totale_sur_joueur2 = 0
  if (cotepremierjoueur + cotedeuxiemejoueur) > 4:
    print "-----> ok cote positive"
   #diference par rapport au point d equilibre:
    #donnees entrante:
    somme_en_jeux_totale = float(raw_input("entre la somme totale que tu veux jouer:"))
    print "-----------------------------"
    somme_en_jeux_joueur = somme_en_jeux_totale / 2
    cote_totale = cotepremierjoueur + cotedeuxiemejoueur
    cote_affine_mediane = cote_totale / 2
    cote_affine_joueur1 = 0
    cote_affine_joueur2 = 0
    pourcentageplusjoueur1 = 0
    pourcentageplusjoueur2 = 0
    print "point d'equilibre (jeux a zero gain):"
    cote_affine_joueur1 += ((somme_en_jeux_totale / cotepremierjoueur))
    print "mise joueur 1:", cote_affine_joueur1, "euros"
    cote_affine_joueur2 += ((somme_en_jeux_totale / cotedeuxiemejoueur))
    print "mise joueur 2:", cote_affine_joueur2, "euros"
    print "-----------------------------"
    # pourcentage par rapport a l autre:
    mise_totale_sur_joueur1 += ((somme_en_jeux_totale * cotepremierjoueur) - somme_en_jeux_totale)
    mise_totale_sur_joueur2 += ((somme_en_jeux_totale * cotedeuxiemejoueur) - somme_en_jeux_totale)


    print "pourcentage:"
    pourcentageplusjoueur2 += ((cotedeuxiemejoueur / cote_totale) * 100)
    print "1/", pourcentageplusjoueur2, "%", "de chance de gagner", mise_totale_sur_joueur1, "euros avec la mise de", somme_en_jeux_totale, "euros"
    pourcentageplusjoueur1 += ((cotepremierjoueur / cote_totale) * 100)
    print "2/", pourcentageplusjoueur1, "%", "de chance de gagner", mise_totale_sur_joueur2, "euros avec la mise de", somme_en_jeux_totale, "euros"
    print "******************************************"
    nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")
  else: 
    print "mauvaise cote (inferieure a 4)"
    print "_______________________________"
    nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")