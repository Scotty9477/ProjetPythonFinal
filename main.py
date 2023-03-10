import AB as arbre

if __name__ == '__main__':
    A1 = arbre.AB()
    print("A1 est vide: ", A1.est_vide())
    A2 = arbre.AB([5])
    print("A2 est vide: ", A2.est_vide())
    A3 = arbre.AB([3])
    A2.set_gauche(A3)
    Atest = arbre.AB([5],
                     arbre.AB([5],
                              arbre.AB([3]),
                              arbre.AB([8]))
                     , arbre.AB([12],
                                arbre.AB([10]),
                                arbre.AB([15],
                                         arbre.AB([14]),
                                         arbre.AB([16]))
                                ))
    print("Atest est vide: ", Atest.est_vide())
    print("Taille de Atest: ", Atest.taille())
    print("Prefixe de Atest: ", Atest.prefixe())
    print("Infixe de Atest: ", Atest.infixe())
    print("Postfixe de Atest: ", Atest.postfixe())
    print("Hauteur de Atest: ", Atest.hauteur())
    print("Atest est un ABR: ", Atest.estABR())
    print ("Atest est eqyilibre: ", Atest.est_equilibre())
    print ("Prefixe de Atest apres  rotation vers la droite: ", Atest.rotation_droite().prefixe())
