from django.db import models

# Create your models here.



class Exigence(ProtoModel):
    nom_exigence = models.CharField(blank= False, null= False, max_length= 200)
    description_exigence = models.TextField(blank = True, null = True)
    categorie_exigence = models.ForeignKey('CategorieExigence', blank= False, null= False, related_name='exigence_categorie_exigence')
    domaine_affaires = models.ForeignKey('DomaineAffaires', blank= True, null= True, related_name='exigence_domaine_affaires')
    eclatement = models.ForeignKey('Exigence', blank= True, null= True, related_name='exigence_eclatement')
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.nom_exigence +  '.' + str( self.categorie_exigence))

    class Meta:
        unique_together = ('nom_exigence','categorie_exigence',)


class CategorieExigence(ProtoModel):
    nom_categorie = models.CharField(blank= False, null= False, max_length= 200)
    description_categorie = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.nom_categorie)

    class Meta:
        unique_together = ('nom_categorie',)


class AttributExigence(ProtoModel):
    nom_attribut_exigence = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)
    categorie_exigence = models.ForeignKey('CategorieExigence', blank= False, null= False, related_name='attribut_exigence_categorie_exigence')

    def __unicode__(self):
        return slugify(self.nom_attribut_exigence +  '.' + str( self.categorie_exigence))

    class Meta:
        unique_together = ('nom_attribut_exigence','categorie_exigence',)


class ValeurExigence(ProtoModel):
    valeur_exigence = models.TextField(blank = True, null = True)
    exigence = models.ForeignKey('Exigence', blank= False, null= False, related_name='valeur_exigence_exigence')
    attribut = models.ForeignKey('AttributExigence', blank= False, null= False, related_name='valeur_exigence_attribut')
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.exigence) +  '.' + str( self.attribut))

    class Meta:
        unique_together = ('exigence','attribut',)