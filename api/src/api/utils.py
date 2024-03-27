class AutoIncrement:
    """ Classe pour générer des identifiants auto-incrémentés """
    _id: int = 0

    @classmethod
    def next(cls) -> int:
        """ Méthode pour générer un nouvel identifiant """
        cls._id += 1
        return cls._id