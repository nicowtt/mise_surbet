print "**Aide pour pronostic tennis**"

#donnees entrantes:
mise_totale_sur_joueur1 = 0
mise_totale_sur_joueur2 = 0
nouveauchoix = 1
nouveauchoix = input("'1' pour lancer  ou '2' pour quitter ou '3' pour surbet live:")
#calcul du surbet live
if nouveauchoix == 3:
  #input:
  cotepremierjoueur = float(raw_input("Cote premier joueur:"))
  surbetlive = (1 / cotepremierjoueur)
  ratio2 = 1.1
  surbetavecratio = 1
  surbetavecratio += (1 - surbetlive)
  sommetotale = 0
  nouveausurbet = 0
  miseenlive = 0.01
  while surbetavecratio > 1:
    ratio2 += 0.01
    surbetavecratio = ((1 / cotepremierjoueur) + (1 / ratio2))
  ratio3 = ratio2
  ratio3 -= 0.01
  print "->cote a attendre pour aucun gain:", ratio3
  misepremierparilive = float(raw_input("Entre la mise du premier pari:"))
  #calcul surbet:
  miseenlive = 1.1
  cotelive = ratio2
  while (miseenlive * cotelive) < (misepremierparilive + miseenlive) :
    miseenlive += 0.1
  print "-->somme minimale sur joueur 2 pour recuperer la mise totale:", miseenlive, "euro"
  dernierecote = float(raw_input("Entre la cote en cour:"))
  print "mise = ",miseenlive, "euros"
  calculgain = (1 / cotepremierjoueur) + (1 / dernierecote)
  derniersurbet = (1 - calculgain) * 100
  gainfinal2 = (miseenlive * derniersurbet) / 100
  print "Surbet!!+",derniersurbet, "%", "gain:", gainfinal2, "euros"
  print "******************************************"
  nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")
  # mettre une boucle jusqu'a ligne 31

else:
  while nouveauchoix == 1:
     #donnees entrantes:
    cotepremierjoueur = float(raw_input("Cote premier joueur:"))
    cotedeuxiemejoueur = float(raw_input("Cote deuxieme joueur:"))
    mise_totale_sur_joueur1 = 0
    mise_totale_sur_joueur2 = 0
    surbet = (1 / cotepremierjoueur) + (1 / cotedeuxiemejoueur)
    surbet2 = ((2 - ((1 / cotepremierjoueur) + (1 / cotedeuxiemejoueur))) * 100)
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
    marge = 0
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
      print "Probabilite de resultat selon Bookmaker pour info:"
      pourcentageplusjoueur2 += ((cotedeuxiemejoueur / cote_totale) * 100)
      print "1/", pourcentageplusjoueur2, "%", "de chance de gagner"
      pourcentageplusjoueur1 += ((cotepremierjoueur / cote_totale) * 100)
      print "2/", pourcentageplusjoueur1, "%", "de chance de gagner"
      print "******************************************"
      nouveauchoix = input("'1' pour relancer  ou '2' pour quitter:")
    else: 
      #input:
      marge += (100 - surbet2)
      coteimaginairejoueur1 = 0
      coteimaginairejoueur2 = 0
    
      #calcul
      print "*************INFO**************"
      print "* bonnes cotes = retour > 90% *"
      print "*******************************"
      print "->retour", surbet2,"% --> marge bookmaker", marge, "%"
      print "solution pendant le jeux pour surbet:"
      if cotepremierjoueur < cotedeuxiemejoueur:
        ratio1 = 1.1
        surbetavecratio = surbet
        while surbetavecratio > 1:
          ratio1 += 0.01
          surbetavecratio = ((1 / cotepremierjoueur) + (1 / ratio1))
        print "-> Mise sur joueur 1 (cote ", cotepremierjoueur, ")"
        print " et attend que la cote du joueur 2 > ", ratio1, " pendant le match pour faire du benefice..."
        print "Probabilite de resultat selon Bookmaker pour info:"
        pourcentageplusjoueur2 += ((cotedeuxiemejoueur / cote_totale) * 100)
        print "1/", pourcentageplusjoueur2, "%", "de chance de gagner"
        pourcentageplusjoueur1 += ((cotepremierjoueur / cote_totale) * 100)
        print "2/", pourcentageplusjoueur1, "%", "de chance de gagner"
        print "-------------------------------------------------"
        nouveauchoix = input("'1' pour relancer  ou '2' pour quitter ou '3' pour surbet live:")
        print "-------------------------------------------------"
      else:
        ratio1 = 1.1
        surbetavecratio = surbet
        while surbetavecratio > 1:
          ratio1 += 0.01
          surbetavecratio = ((1 / cotedeuxiemejoueur) + (1 / ratio1))
        print "-> Mise sur joueur 2 (cote ", cotedeuxiemejoueur, ")"
        print " et attend que la cote du joueur 1 > ", ratio1, " pendant le match pour faire du benefice..."
        print "Probabilite de resultat selon Bookmaker pour info:"
        pourcentageplusjoueur2 += ((cotedeuxiemejoueur / cote_totale) * 100)
        print "1/", pourcentageplusjoueur2, "%", "de chance de gagner"
        pourcentageplusjoueur1 += ((cotepremierjoueur / cote_totale) * 100)
        print "2/", pourcentageplusjoueur1, "%", "de chance de gagner"
        print "-------------------------------------------------"
        nouveauchoix = input("'1' pour relancer  ou '2' pour quitter ou '3' pour surbet live:")
        print "-------------------------------------------------" 