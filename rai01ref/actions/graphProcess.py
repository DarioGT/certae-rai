#!/usr/bin/env python
"""
Prototype to DOT (Graphviz) converter by Dario Gomez
Table format from  django-extensions 
"""

from protoLib.utilsBase import slugify, getClassName  


class GraphProcess():

    def __init__(self):

        self.tblStyle = False         
        self.lnkStyle = '\n'

        self.dotSource = 'digraph bp {'
        self.dotSource += 'fontname="Helvetica";fontsize = 8;\n'
        self.dotSource += 'rankdir = LR;\nnode [shape=box,style=rounded,width=0,height=0,concentrate=true];\n'

        self.dotSource += 'start [label=" ",shape=circle,width=0.3]\n'
        self.dotSource += 'end [label=" ",shape=circle,width=0.3,style=bold]\n'


    def getDiagramDefinition(self, diagramSet):
        
        self.diagrams = []
        self.arcs = []
        
        for pDiag in diagramSet:
            
            gDiagram = {
                'code': getClassName(pDiag.code) ,
                'label': pDiag.code ,
                'showBorder' : getattr(pDiag, 'showBorder' , False),
                'arcs': []
            }

            for pDiagComposition in pDiag.artefactcomposition_set.all():

                #  Verifica si el nodo inicial es el contenedor 
                pArc0 = pDiagComposition.inputArt.code
                if gDiagram['label'] == pArc0: pArc0 = 'Start'

                #  Verifica si el nodo final es nulo, entonces end  
                #  Conserva el nombre diagrama y agrega un :Label 
                try: 
                    pArc1 = pDiagComposition.outputArt.code
                except: pArc1 =  'End'

                pArc01 = {
                    'n0': slugify( pArc0 ) ,
                    'n1': slugify( pArc1 )
                }

                self.arcs.append(pArc01)
                gDiagram['arcs'].append(pArc01)
    
            self.diagrams.append(gDiagram)


    def generateDotModel(self):

        # Dibuja las entidades  
        for gDiagram in self.diagrams:

            self.dotSource += '\nsubgraph cluster_{0} {{\n'.format(gDiagram.get('code'))
            self.dotSource += 'style=dotted;'
            self.dotSource += 'label="{0}";\n'.format(gDiagram.get('label', '')) 

            for gArc in gDiagram['arcs']:
                self.dotSource += '  {0} -> {1} {2}'.format( gArc['n0'] , gArc['n1'], self.lnkStyle ) 

            self.dotSource += '}\n'
        self.dotSource += '}'
  
        return self.dotSource
        