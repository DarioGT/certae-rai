from django.conf.urls import patterns, url
from rai02db.raccordement import getModeleRaccordement, createRaccordement, deleteRaccordement, listRaccordement

urlpatterns = patterns('',
    url('getModeleRaccordement/$', getModeleRaccordement),
    url('createRaccordement/$', createRaccordement),
    url('deleteRaccordement/$', deleteRaccordement),
    url('listRaccordement/$', listRaccordement),
)