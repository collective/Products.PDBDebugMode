"""Monkey patches to various ATContentTypes code that swallows errors
we might want to debug."""

import sys
import pdb

from Products.ATContentTypes.content.base import ATCTMixin

def initializeArchetype(self, **kwargs):
    """Don't swallow errors on ATCT content creation."""
    self.initializeLayers()
    self.markCreationFlag()
    self.setDefaults()
    if kwargs:
        self.edit(**kwargs)
    self._signature = self.Schema().signature()
    if self.isPrincipiaFolderish:
        self.copyLayoutFromParent()

ATCTMixin.initializeArchetype = initializeArchetype
