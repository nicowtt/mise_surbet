print "**Surbet tennis**"

#donnees entrantes:
mise_totale_sur_joueur1 = 0
mise_totale_sur_joueur2 = 0
nouveauchoix = 1
#analyse niveau de la cote:
while nouveauchoix == 1:
   #donnees entrantes:
  cotepremierjoueur = float(raw_input("Cote premier joueur:"))
  cotedeuxiemejoueur = float(raw_input("Cote deuxieme joueur:"))
  mise_totale_sur_joueur1 = 0
  mise_totale_sur_joueur2 = 0
  surbet = ((1 / cotepremierjoueur) + (1 / cotedeuxiemejoueur))
  cote_totale = cotepremierjoueur + cotedeuxiemejoueur
  cote_affine_mediane = cote_totale / 2
  cote_affine_joueur1 = 0
  cote_affine_joueur2 = 0
  pourcentageplusjoueur1 = 0
  pourcentageplusjoueur2 = 0
  cotepremierjoueursurbet = 0
  cotedeuxiemejoueursurbet = 0
  mise_totale_sur_joueur1_surbet = 0
  mise_totale_sur_joueur2_surbet = 0
  gainjoueur1 = 0
  gainjoueur2 = 0
  gain = 0
  gainfinal = 0
  gaindebut = 0
  # quel est la meilleure cote:
  meilleurecote = 0
    #calcul
  if surbet < 1:
    print "oO-----> Surbet !!"
    gaindebut = ((1 - surbet) * 100)
    print "+",gaindebut, "%"
    #diference par rapport au point d equilibre:
    #donnees entrante:
    somme_en_jeux_totale = float(raw_input("Mise totale en euros:"))
    somme_en_jeux_joueur = somme_en_jeux_totale / 2
    print "-----------------------------"
    #calcul
    #print "point d'equilibre (jeux a zero gain):"
    cote_affine_joueur1 += ((somme_en_jeux_totale / cotepremierjoueur))
    #print "mise joueur 1:", cote_affine_joueur1, "euros"
    cote_affine_joueur2 += ((somme_en_jeux_totale / cotedeuxiemejoueur))
    #print "mise joueur 2:", cote_affine_joueur2, "euros"
    print "***************************************************"
    print "*****************SURBET****************************"
    # pourcentage par rapport a l autre:
    mise_totale_sur_joueur1 += ((somme_en_jeux_totale * cotepremierjoueur) - somme_en_jeux_totale)
    mise_totale_sur_joueur2 += ((somme_en_jeux_totale * cotedeuxiemejoueur) - somme_en_jeux_totale)

    #calcul en surbet:
    print "Possibilite de gain positif si mise sur les deux joueurs "
    gainjoueur1 += cote_affine_joueur1 / surbet
    gainjoueur2 += cote_affine_joueur2 / surbet
    print "mise joueur 1:", gainjoueur1, "euros"
    print "mise joueur 2:", gainjoueur2, "euros"
    gain += gainjoueur1 * cotepremierjoueur
    print "gain total dans tous les cas:", gain, "euros"
    gainfinal += gain - somme_en_jeux_totale
    print "---------> benefice: ", gainfinal, "euros"
    print "***************************************************"
    print "pourcentage pour info:"
    pourcentageplusjoueur2 += ((cotedeuxiemejoueur / cote_totale) * 100)
    print "1/", pourcentageplusjoueur2, "%", "de chance de gagner"
    pourcentageplusjoueur1 += ((cotepremierjoueur / cote_totale) * 100)
    print "2/", pourcentageplusjoueur1, "%", "de chance de gagner"
    print "******************************************"
    nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")
  else: 
    #input:
    coteimaginairejoueur1 = 0
    coteimaginairejoueur2 = 0
    
    #calcul
    print "->", surbet, ":pas de surbet, solution possible pour surbet"
    if cotepremierjoueur < cotedeuxiemejoueur:
      ratio1 = 1.1
      surbetavecratio = surbet
      while surbetavecratio > 1:
        ratio1 += 0.1
        surbetavecratio = ((1 / cotepremierjoueur) + (1 / ratio1))
      print "-> Mise sur joueur 1 (cote ", cotepremierjoueur, ")"
      print " et attend que la cote du joueur 2 > ", ratio1, " pendant le match pour faire du benefice..."
      print "-------------------------------------------------"
      nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")
      print "-------------------------------------------------"
    else:
      ratio1 = 1.1
      surbetavecratio = surbet
      while surbetavecratio > 1:
        ratio1 += 0.01
        surbetavecratio = ((1 / cotedeuxiemejoueur) + (1 / ratio1))
      print "-> Mise sur joueur 2 (cote ", cotedeuxiemejoueur, ")"
      print " et attend que la cote du joueur 1 > ", ratio1, " pendant le match pour faire du benefice..."
      print "-------------------------------------------------"
      nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")
      print "-------------------------------------------------"       