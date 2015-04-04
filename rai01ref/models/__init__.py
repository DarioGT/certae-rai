# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import ProtoModel

from mBase import * 
from mRai import * 

__all__ = [
	'RaiModel', 'DocAttribute', 'DocumentType', 'Domain',
	'Artefact', 'Source', 'Requirement', 'Capacity', 
	'ArtefactCapacity', 'ArtefactComposition', 'ArtefactRequirement', 'ArtefactSource', 
	'Projet', 'ProjectArtefact', 'ProjectCapacity', 'ProjectRequirement', 
]