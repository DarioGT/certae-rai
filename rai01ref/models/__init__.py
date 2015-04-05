# -*- coding: utf-8 -*-

from django.db import models
from protoLib.models import ProtoModel

from mBase import * 
from mRai import * 

__all__ = [
	'DocModel', 'DocAttribute', 'DocType', 'Domain',
	'Artefact', 'Source', 'Requirement', 'Capacity', 
	'ArtefactCapacity', 'ArtefactComposition', 'ArtefactRequirement', 'ArtefactSource', 
	'Projet', 'ProjectArtefact', 'ProjectCapacity', 'ProjectRequirement', 
]