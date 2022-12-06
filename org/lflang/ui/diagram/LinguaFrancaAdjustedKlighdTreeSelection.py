#!/usr/bin/env python
""" generated source for module LinguaFrancaAdjustedKlighdTreeSelection """
# 
#  * KIELER - Kiel Integrated Environment for Layout Eclipse RichClient
#  *
#  * http://rtsys.informatik.uni-kiel.de/kieler
#  * 
#  * Copyright 2022 by
#  * + Kiel University
#  *   + Department of Computer Science
#  *     + Real-Time and Embedded Systems Group
#  * 
#  * This code is provided under the terms of the Eclipse Public License (EPL).
#  
# package: org.lflang.ui.diagram
# import java.util.HashMap
# import java.util.Iterator
# import org.eclipse.elk.core.util.Pair
# import org.eclipse.emf.ecore.EObject
# import com.google.common.base.Function
# import com.google.common.collect.Iterators
# import de.cau.cs.kieler.klighd.KlighdTreeSelection

# 
#  * @author als
#  
class LinguaFrancaAdjustedKlighdTreeSelection(KlighdTreeSelection):
    """ generated source for class LinguaFrancaAdjustedKlighdTreeSelection """
    #  The LF model 
    model = None

    #  Cached map of imports 
    importedReactors = dict()

    #      * Create LF adjusted wrapper around KlighdTreeSelection.
    #      * 
    #      * @param source copy data from original KlighdTreeSelection
    #      
    def __init__(self, source, lfModel):
        """ generated source for method __init__ """
        super(LinguaFrancaAdjustedKlighdTreeSelection, self).__init__(source.getPaths())
        self.model = lfModel
        #  Create import map
        for imp in lfModel.getImports():
            for impReactor in imp.getReactorClasses():
                self.importedReactors.put(impReactor.getReactorClass(), impReactor)

    #      * {@inheritDoc}
    #      
    def sourceElementIterator(self):
        """ generated source for method sourceElementIterator """
        return Iterators.transform(iterator(), Function())

    #      * {@inheritDoc}
    #      
    def sourceViewPairIterator(self):
        """ generated source for method sourceViewPairIterator """
        return Iterators.transform(iterator(), Function())

    #      * Find the reactor import for the given model element.
    #      * 
    #      * @param sourceEObj the original associate
    #      * @param diagramElement the diagram element
    #      * @return the associated reactor import or the original associate
    #      
    def findImport(self, sourceEObj, diagramElement):
        """ generated source for method findImport """
        parent = diagramElement
        while True:
            parentSource = getViewContext().getSourceElement(parent)
            if self.importedReactors.containsKey(parentSource):
                return self.importedReactors.get(parentSource)
                #  associate with import
            parent = parent.eContainer()
            if not ((parent != None)):
                break
        return sourceEObj
        #  keep old association
