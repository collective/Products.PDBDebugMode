from pathlib import Path
from setuptools import find_packages
from setuptools import setup


long_description = Path("README.md").read_text() + "\n" + Path("CHANGES.md").read_text()

version = "2.2.dev0"

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
        "Framework :: Plone :: 5.2",
        "Framework :: Plone :: 6.0",
        "Framework :: Zope :: 4",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="Plone, debug, pdb",
    author="Ross Patterson",
    author_email="me@rpatterson.net",
    url="https://github.com/collective/Products.PDBDebugMode",
    license="GPL",
    packages=find_packages(exclude=["ez_setup"]),
    namespace_packages=["Products"],
    include_package_data=True,
    zip_safe=False,
    python_requires=">=3.6",
    install_requires=[
        "setuptools",
        "collective.monkeypatcher",
        # -*- Extra requirements: -*-
        "six",
    ],
    extras_require={
        "ipdb": ["ipdb>=0.3"],
        "zodb": ["zope.testrunner"],
        "zodb-testing": ["zope.testing"],
    },
    entry_points={
        # -*- Entry points: -*-
        "z3c.autoinclude.plugin": "target = plone",
    },
)
