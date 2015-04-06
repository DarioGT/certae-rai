from django.contrib import admin

from models import DocAttribute, DocType, Domain, Artefact, Source, Requirement, Capacity
from models import ArtefactCapacity, ArtefactComposition, ArtefactRequirement, ArtefactSource 
from models import Projet, ProjectArtefact, ProjectCapacity, ProjectRequirement 


admin.site.register( DocAttribute )
admin.site.register( Domain )

admin.site.register( Requirement )
admin.site.register( Capacity )
admin.site.register( Source )

# admin.site.register( ArtefactCapacity )
# admin.site.register( ArtefactComposition )
# admin.site.register( ArtefactRequirement )
# admin.site.register( ArtefactSource  )

admin.site.register( Projet )
# admin.site.register( ProjectArtefact )
# admin.site.register( ProjectCapacity )
# admin.site.register( ProjectRequirement  )


from actions import doBPD
class MyArtefac( admin.ModelAdmin ):
    actions = [ doBPD  ]

admin.site.register( Artefact, MyArtefac  )


from actions import doRaiMenu
class MyDocType( admin.ModelAdmin ):
    actions = [ doRaiMenu  ]

admin.site.register( DocType, MyDocType )
