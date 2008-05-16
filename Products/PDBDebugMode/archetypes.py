"""Monkey patches to various AT code that swallows errors we might
want to debug."""

from Products.CMFCore.utils import getToolByName

from Products.Archetypes.BaseObject import BaseObject

def initializeArchetype(self, **kwargs):
    """Don't swallow errors on AT content creation."""
    self.initializeLayers()
    self.markCreationFlag()
    self.setDefaults()
    if kwargs:
        kwargs['_initializing_'] = True
        self.edit(**kwargs)
    self._signature = self.Schema().signature()

BaseObject.initializeArchetype = initializeArchetype

from Products.Archetypes.ArchetypeTool import ArchetypeTool

def getCatalogsByType(self, portal_type):
    """Don't swallow catalog access errors."""
    catalogs = []
    catalog_map = getattr(self, 'catalog_map', None)
    if catalog_map is not None:
        names = self.catalog_map.get(portal_type, ['portal_catalog'])
    else:
        names = ['portal_catalog']
    for name in names:
        catalogs.append(getToolByName(self, name))
    return catalogs
        
ArchetypeTool.getCatalogsByType = getCatalogsByType
