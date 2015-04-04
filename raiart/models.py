from django.db import models

# Create your models here.


class CategorieArtefact(ProtoModel):
    nom_categorie_artefact = models.CharField(blank= False, null= False, max_length= 200)
    description_categorie_artefact = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.nom_categorie_artefact)

    class Meta:
        unique_together = ('nom_categorie_artefact',)

class Artefact(ProtoModel):
    nom_artefact = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)
    domaine_affaires = models.ForeignKey('DomaineAffaires', blank= False, null= False, related_name='artefact_domaine_affaires')
    categorie_artefact = models.ForeignKey('CategorieArtefact', blank= False, null= False, related_name='artefact_categorie_artefact')
    memo = models.TextField(blank = True, null = True)
    eclatement = models.ForeignKey('Artefact', blank= True, null= True, related_name='artefact_eclatement')

    def __unicode__(self):
        return slugify(self.nom_artefact +  '.' + str( self.categorie_artefact))

    class Meta:
        unique_together = ('nom_artefact','categorie_artefact',)

class AttributArtefact(ProtoModel):
    nom_attribut_artefact = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)
    categorie_artefact = models.ForeignKey('CategorieArtefact', blank= False, null= False, related_name='attribut_artefact_categorie_artefact')

    def __unicode__(self):
        return slugify(self.nom_attribut_artefact +  '.' + str( self.categorie_artefact))

    class Meta:
        unique_together = ('nom_attribut_artefact','categorie_artefact',)

class ValeurArtefact(ProtoModel):
    valeur_artefact = models.TextField(blank = True, null = True)
    artefact = models.ForeignKey('Artefact', blank= False, null= False, related_name='valeur_artefact_artefact')
    attribut = models.ForeignKey('AttributArtefact', blank= False, null= False, related_name='valeur_artefact_attribut')

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.attribut))

    class Meta:
        unique_together = ('artefact','attribut',)



class RegroupementArtefacts(ProtoModel):
    artefacts = models.ForeignKey('Artefact', blank= False, null= False, related_name='regroupement_artefacts_artefacts')
    projet = models.ForeignKey('Projet', blank= False, null= False, related_name='regroupement_artefacts_projet')
    commentaire = models.TextField(blank = True, null = True)
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefacts) +  '.' + str( self.projet))

    class Meta:
        unique_together = ('artefacts','projet',)      



class Source(ProtoModel):
    nom_source = models.CharField(blank= False, null= False, max_length= 200)
    description_source = models.TextField(blank = True, null = True)
    reference_source = models.CharField(blank= True, null= True, max_length= 200)
    date_mise_a_jour = models.TimeField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.nom_source)

    class Meta:
        unique_together = ('nom_source',)


class SourcesArtefact(ProtoModel):
    commentaire = models.TextField(blank = True, null = True)
    source = models.ForeignKey('Source', blank= True, null= True, related_name='sources_artefact_source')
    artefact = models.ForeignKey('Artefact', blank= True, null= True, related_name='sources_artefact_artefact')

    def __unicode__(self):
        return 'NoKey'


class CompositionArtefact(ProtoModel):
    commentaire = models.TextField(blank = True, null = True)
    memo = models.TextField(blank = True, null = True)
    artefact_parent = models.ForeignKey('Artefact', blank= False, null= False, related_name='composition_artefact_artefact_parent')
    artefact_enfant = models.ForeignKey('Artefact', blank= True, null= True, related_name='composition_artefact_artefact_enfant')

    def __unicode__(self):
        return 'NoKey'

        
class ExigencesArtefact(ProtoModel):
    artefact = models.ForeignKey('Artefact', blank= False, null= False, related_name='exigences_artefact_artefact')
    exigence = models.ForeignKey('Exigence', blank= False, null= False, related_name='exigences_artefact_exigence')
    commentaire = models.TextField(blank = True, null = True)
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.exigence))

    class Meta:
        unique_together = ('artefact','exigence',)

class CapacitesArtefact(ProtoModel):
    commentaire = models.TextField(blank = True, null = True)
    memo = models.TextField(blank = True, null = True)
    artefact = models.ForeignKey('Artefact', blank= False, null= False, related_name='capacites_artefact_artefact')
    capacite = models.ForeignKey('Capacite', blank= False, null= False, related_name='capacites_artefact_capacite')

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.capacite))

    class Meta:
        unique_together = ('artefact','capacite',)