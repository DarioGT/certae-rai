# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify

from rai01ref.models.mBase import RaiModel, Domain 


class Artefact(RaiModel):
    refArtefact = models.ForeignKey('Artefact', blank= True, null= True )


class Capacity(RaiModel):
    refCapacity = models.ForeignKey('Capacity', blank= True, null= True )


class Requirement(RaiModel):
    refRequirement = models.ForeignKey('Requirement', blank= True, null= True )



class Source(ProtoModel):
    code = models.CharField(blank= False, null= False, max_length= 200)
    reference = models.CharField(blank= True, null= True, max_length= 200)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.code)

    class Meta:
        unique_together = ('code',)


class ArtefactSource(ProtoModel):
    source = models.ForeignKey('Source', blank= True, null= True)
    artefact = models.ForeignKey('Artefact', blank= True, null= True)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return 'NoKey'


class ArtefactComposition(ProtoModel):
    """ Manejo de arcos, pe. las transiciones en procesos 
    """    
    containerArt = models.ForeignKey('Artefact', blank= False, null= False, related_name='containerArt_set')
    inputArt = models.ForeignKey('Artefact', blank= False, null= False, related_name='inputArt_set')
    outputArt = models.ForeignKey('Artefact', blank= True, null= True, related_name='outputArt_set')

    condition  = models.TextField(blank = True, null = True)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)


    def __unicode__(self):
        return 'NoKey'


class ArtefactRequirement(ProtoModel):
    artefact = models.ForeignKey('Artefact', blank= False, null= False)
    requirement = models.ForeignKey('Requirement', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.requirement))

    class Meta:
        unique_together = ('artefact','requirement',)


class ArtefactCapacity(ProtoModel):
    artefact = models.ForeignKey('Artefact', blank= False, null= False)
    capacity = models.ForeignKey('Capacity', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.capacity))

    class Meta:
        unique_together = ('artefact','capacity',)



class Projet(ProtoModel):
    domain = models.ForeignKey(Domain, blank= False, null= False)
    code = models.CharField(blank= False, null= False, max_length= 200)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)


    def __unicode__(self):
        return slugify(str(self.domain) +  '.' + self.code)

    class Meta:
        unique_together = ('domain','code',)



class ProjectArtefact(ProtoModel):
    projet = models.ForeignKey('Projet', blank= False, null= False)
    artefact = models.ForeignKey('Artefact', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefacts) +  '.' + str( self.projet))

    class Meta:
        unique_together = ('artefacts','projet',)


class ProjectCapacity(ProtoModel):

    projet = models.ForeignKey('Projet', blank= False, null= False)
    capacity = models.ForeignKey('Capacity', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.projet) +  '.' + str( self.capacity))

    class Meta:
        unique_together = ('projet','capacity',)


class ProjectRequirement(ProtoModel):
    projet = models.ForeignKey('Projet', blank= False, null= False)
    requirement = models.ForeignKey('Requirement', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.projet) +  '.' + str( self.requirement))

    class Meta:
        unique_together = ('projet','requirement',)

