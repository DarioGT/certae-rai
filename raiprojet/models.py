# -*- coding: utf-8 -*-

# This is an auto-generated model module by CeRTAE SoftMachine v13.12dgt
# for model : "rai"
# You'll have to do the following manually to clean this up:
#     * Add specific procedures  (WFlow)

from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify



class DomaineAffaires(ProtoModel):
    id_domaine_affaires = models.CharField(blank= False, null= False, max_length= 200)
    description = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.id_domaine_affaires)

    class Meta:
        unique_together = ('id_domaine_affaires',)


class Projet(ProtoModel):
    domaff_projet = models.ForeignKey('DomaineAffaires', blank= False, null= False, related_name='projet_domaff_projet')
    nom_projet = models.CharField(blank= False, null= False, max_length= 200)
    description_projet = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.domaff_projet) +  '.' + self.nom_projet)

    class Meta:
        unique_together = ('domaff_projet','nom_projet',)



class RegroupementDesModeles(ProtoModel):
    modele = models.ForeignKey('Modele', blank= False, null= False, related_name='regroupement_des_modeles_modele')
    projet = models.ForeignKey('Projet', blank= False, null= False, related_name='regroupement_des_modeles_projet')
    commentaire = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.modele) +  '.' + str( self.projet))

    class Meta:
        unique_together = ('modele','projet',)



class RegroupementCapacites(ProtoModel):
    projet = models.ForeignKey('Projet', blank= False, null= False, related_name='regroupement_capacites_projet')
    capacites = models.ForeignKey('Capacite', blank= False, null= False, related_name='regroupement_capacites_capacites')
    commentaire = models.TextField(blank = True, null = True)
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.projet) +  '.' + str( self.capacites))

    class Meta:
        unique_together = ('projet','capacites',)


class RegroupementExigences(ProtoModel):
    projet = models.ForeignKey('Projet', blank= False, null= False, related_name='regroupement_exigences_projet')
    exigences = models.ForeignKey('Exigence', blank= False, null= False, related_name='regroupement_exigences_exigences')
    commentaire = models.TextField(blank = True, null = True)
    memo = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.projet) +  '.' + str( self.exigences))

    class Meta:
        unique_together = ('projet','exigences',)

