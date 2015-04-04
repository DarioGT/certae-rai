from django.db import models

# Create your models here.



class CategorieCapacite(ProtoModel):
    nom_categorie_capacite = models.CharField(blank= False, null= False, max_length= 200)
    decription = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.nom_categorie_capacite)

    class Meta:
        unique_together = ('nom_categorie_capacite',)

class Capacite(ProtoModel):
    nom_capacite = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)
    categorie_capacite = models.ForeignKey('CategorieCapacite', blank= False, null= False, related_name='capacite_categorie_capacite')
    domaine_affaires = models.ForeignKey('DomaineAffaires', blank= False, null= False, related_name='capacite_domaine_affaires')
    memo = models.TextField(blank = True, null = True)
    eclatement = models.ForeignKey('Capacite', blank= True, null= True, related_name='capacite_eclatement')

    def __unicode__(self):
        return slugify(self.nom_capacite +  '.' + str( self.categorie_capacite))

    class Meta:
        unique_together = ('nom_capacite','categorie_capacite',)

class AttributCapacite(ProtoModel):
    nom = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)
    categorie_capacite = models.ForeignKey('CategorieCapacite', blank= False, null= False, related_name='attribut_capacite_categorie_capacite')
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.nom +  '.' + str( self.categorie_capacite))

    class Meta:
        unique_together = ('nom','categorie_capacite',)

class ValeurCapacite(ProtoModel):
    valeur_capacite = models.TextField(blank = True, null = True)
    capacite = models.ForeignKey('Capacite', blank= False, null= False, related_name='valeur_capacite_capacite')
    attribut = models.ForeignKey('AttributCapacite', blank= False, null= False, related_name='valeur_capacite_attribut')
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.capacite) +  '.' + str( self.attribut))

    class Meta:
        unique_together = ('capacite','attribut',)