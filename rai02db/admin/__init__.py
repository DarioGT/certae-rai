# -*- coding: utf-8 -*-

from django.contrib import admin

from rai02db.models import DomaineAffaires
from rai02db.actions import  doImportRAI, doMatchRAI

class AdmDomaineAffaires( admin.ModelAdmin ):
    actions = [ doImportRAI, doMatchRAI  ]

admin.site.register( DomaineAffaires, AdmDomaineAffaires )


# ------------------------------------------------

from rai02db.models import ModeleRaccordement
from rai02db.actions import  doFindReplace

class AdmModeleRaccordement( admin.ModelAdmin ):
    actions = [ doFindReplace ]

admin.site.register( ModeleRaccordement, AdmModeleRaccordement )


# ------------------------------------------------

from rai02db.models import Modele
from rai02db.actions import  doMatrixRacc

class AdmModele( admin.ModelAdmin ):
    actions = [ doMatrixRacc ]

admin.site.register( Modele, AdmModele )



# ------------------------------------------------

from rai02db.models import Entite 
from rai02db.actions import  doAddModel

class AdmEntite( admin.ModelAdmin ):
    actions = [ doAddModel ]

admin.site.register( Entite, AdmEntite )