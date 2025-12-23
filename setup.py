from pathlib import Path
from setuptools import setup


long_description = Path("README.md").read_text() + "\n" + Path("CHANGES.md").read_text()

version = "3.0.0"

setup(
    name="Products.PDBDebugMode",
    version=version,
    description="Post-mortem debugging on Zope exceptions",
    long_description_content_type="text/markdown",
    long_description=long_description,
    classifiers=[
        "Development Status :: 5 - Production/Stable",
        "Environment :: Web Environment",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Framework :: Plone",
        "Framework :: Plone :: 6.2",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.13",
    ],
    keywords="Plone, debug, pdb",
    author="Ross Patterson",
    author_email="me@rpatterson.net",
    url="https://github.com/collective/Products.PDBDebugMode",
    license="GPL",
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.10",
    install_requires=[
        "collective.monkeypatcher",
        "Products.CMFCore",
        "Products.CMFPlone",
        "Zope",
    ],
    extras_require={
        "ipdb": ["ipdb>=0.3"],
        "zodb": ["zope.testrunner >= 6.4"],
        "zodb-testing": ["zope.testing"],
    },
    entry_points={
        # -*- Entry points: -*-
        "z3c.autoinclude.plugin": "target = plone",
    },
)
