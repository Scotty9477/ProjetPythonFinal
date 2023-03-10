class AB:
    def __init__(self, racine: list = None, gauche=None, droite=None):
        self.racine = racine
        self.gauche = gauche
        self.droite = droite

    def get_racine(self):
        return self.racine

    def get_gauche(self):
        return self.gauche

    def get_droite(self):
        return self.droite

    def set_racine(self, racine):
        self.racine = racine

    def set_gauche(self, gauche):
        self.gauche = gauche

    def set_droite(self, droite):
        self.droite = droite

    def est_vide(self):
        return self.racine is None

    def taille(self):
        if self.racine is None:
            return 0
        else:
            taille_gauche = self.gauche.taille() if self.gauche else 0
            taille_droite = self.droite.taille() if self.droite else 0
            return 1 + taille_gauche + taille_droite

    def prefixe(self):
        resultat = []
        if self.racine is not None:
            resultat.append(self.racine)
            if self.gauche is not None:
                resultat.extend(self.gauche.prefixe())
            if self.droite is not None:
                resultat.extend(self.droite.prefixe())
        return resultat

    def infixe(self):
        resultat = []
        if self.racine is not None:
            if self.gauche is not None:
                resultat.extend(self.gauche.infixe())
            resultat.append(self.racine)
            if self.droite is not None:
                resultat.extend(self.droite.infixe())
        return resultat

    def postfixe(self):
        resultat = []
        if self.racine is not None:
            if self.gauche is not None:
                resultat.extend(self.gauche.postfixe())
            if self.droite is not None:
                resultat.extend(self.droite.postfixe())
            resultat.append(self.racine)
        return resultat

    def hauteur(self):
        if self.racine is None:
            return 0
        else:
            hauteur_gauche = self.gauche.hauteur() if self.gauche is not None else 0
            hauteur_droite = self.droite.hauteur() if self.droite is not None else 0
            return 1 + max(hauteur_gauche, hauteur_droite)

    def estABR(self, min=float('-inf'), max=float('inf')):
        if self.racine is None:
            return True
        elif min < self.racine[0] < max:
            return (self.gauche is None or self.gauche.estABR(min, self.racine[0])) \
                and (self.droite is None or self.droite.estABR(self.racine[0], max))
        else:
            return False

    def est_equilibre(self):
        if self.racine is None:
            return True
        else:
            return abs((self.gauche.hauteur() if self.gauche else 0)
                       - (self.droite.hauteur() if self.droite else 0)) <= 1 \
                and (self.gauche.est_equilibre() if self.gauche else True) \
                and (self.droite.est_equilibre() if self.droite else True)

    def rotation_gauche(self):
        nouveau_racine = self.droite
        self.droite = nouveau_racine.gauche
        nouveau_racine.gauche = self
        return nouveau_racine

    def rotation_droite(self):
        nouveau_racine = self.gauche
        self.gauche = nouveau_racine.droite
        nouveau_racine.droite = self
        return nouveau_racine

