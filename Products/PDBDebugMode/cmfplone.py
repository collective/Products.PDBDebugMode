"""Monkey patches to various CMFPlone code that swallows errors we
might want to debug."""

from Products.CMFPlone.MigrationTool import MigrationTool

def upgrade(self, REQUEST=None, dry_run=None, swallow_errors=0):
    """Keep portal migrations from swallowing errors."""
    return MigrationTool.upgrade(self, REQUEST, dry_run, swallow_errors)
