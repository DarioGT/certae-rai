# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import ProtoModel
from protoLib.utilsBase import slugify

from rai01ref.models.mBase import DocModel, Domain 


class Artefact(DocModel):
    refArtefact = models.ForeignKey('Artefact', blank= True, null= True )

    # siempre sera un filtro de dos niveles, documento y tipo, 
    # la tabla de documento define el valor del documento, el tipo viene en el menu 
    _jDefValueDoc  = 'ARTEFACT'

    protoExt = { 
        "actions": [
            { "name": "doBPD" , "selectionMode" : "sinlge" },
        ],
        "gridConfig" : {
            "listDisplay": [ "code", "description", ],
        },
    } 


class Capacity(DocModel):
    refCapacity = models.ForeignKey('Capacity', blank= True, null= True )

    _jDefValueDoc  = 'CAPACITY'

    protoExt = { 
        "gridConfig" : {
            "listDisplay": [ "code", "description", ],
        },
    } 

class Requirement(DocModel):
    refRequirement = models.ForeignKey('Requirement', blank= True, null= True )

    _jDefValueDoc  = 'REQUIREMENT'

    protoExt = { 
        "gridConfig" : {
            "listDisplay": [ "code", "description", ],
        },
    } 

class Source(ProtoModel):
    code = models.CharField(blank= False, null= False, max_length= 200)
    reference = models.CharField(blank= True, null= True, max_length= 200)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(self.code)

    class Meta:
        app_label = 'rai01ref'
        unique_together = ('code',)


class ArtefactSource(ProtoModel):
    source = models.ForeignKey('Source', blank= True, null= True)
    artefact = models.ForeignKey('Artefact', blank= True, null= True)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return 'NoKey'

    class Meta:
        unique_together = ('source', 'artefact')
        app_label = 'rai01ref'


class ArtefactComposition(ProtoModel):
    """ Manejo de arcos, pe. las transiciones en procesos 
    """    
    containerArt = models.ForeignKey('Artefact', blank= False, null= False, related_name='artefactcomposition_set')
    inputArt = models.ForeignKey('Artefact', blank= False, null= False, related_name='+')
    outputArt = models.ForeignKey('Artefact', blank= True, null= True, related_name='+')

    condition  = models.TextField(blank = True, null = True)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    class Meta:
        app_label = 'rai01ref'

    def __unicode__(self):
        try: 
            endNode = self.outputArt.code 
        except: endNode = "/*"
        return '{0} -> {1}'.format( slugify( self.inputArt.code ), endNode ) 


class ArtefactRequirement(ProtoModel):
    artefact = models.ForeignKey('Artefact', blank= False, null= False)
    requirement = models.ForeignKey('Requirement', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.requirement))

    class Meta:
        unique_together = ('artefact','requirement',)
        app_label = 'rai01ref'


class ArtefactCapacity(ProtoModel):
    artefact = models.ForeignKey('Artefact', blank= False, null= False)
    capacity = models.ForeignKey('Capacity', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.artefact) +  '.' + str( self.capacity))

    class Meta:
        unique_together = ('artefact','capacity',)
        app_label = 'rai01ref'



class Projet(ProtoModel):
    domain = models.ForeignKey(Domain, blank= False, null= False)
    code = models.CharField(blank= False, null= False, max_length= 200)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)


    def __unicode__(self):
        return slugify(str(self.domain) +  '.' + self.code)

    class Meta:
        unique_together = ('domain','code',)
        app_label = 'rai01ref'



class ProjectArtefact(ProtoModel):
    projet = models.ForeignKey('Projet', blank= False, null= False)
    artefact = models.ForeignKey('Artefact', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str(self.artefact) +  '.' + str( self.projet))

    class Meta:
        unique_together = ('artefact','projet',)
        app_label = 'rai01ref'


class ProjectCapacity(ProtoModel):

    projet = models.ForeignKey('Projet', blank= False, null= False)
    capacity = models.ForeignKey('Capacity', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.projet) +  '.' + str( self.capacity))

    class Meta:
        unique_together = ('projet','capacity',)
        app_label = 'rai01ref'


class ProjectRequirement(ProtoModel):
    projet = models.ForeignKey('Projet', blank= False, null= False)
    requirement = models.ForeignKey('Requirement', blank= False, null= False)

    notes = models.TextField(blank = True, null = True)
    description  = models.TextField(blank = True, null = True)

    def __unicode__(self):
        return slugify(str( self.projet) +  '.' + str( self.requirement))

    class Meta:
        unique_together = ('projet','requirement',)
        app_label = 'rai01ref'

