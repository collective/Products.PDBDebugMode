from setuptools import setup, find_packages
import os

version = '2.0.dev0'

setup(name='Products.PDBDebugMode',
      version=version,
      description="Post-mortem debugging on Zope exceptions",
      long_description=open("README.txt").read() + "\n" + open(
          os.path.join("docs", "HISTORY.txt")).read(),
      classifiers=[
          "Environment :: Web Environment",
          "Topic :: Software Development :: Libraries :: Python Modules",
          "Framework :: Plone",
          "Framework :: Plone :: 5.2",
          "Framework :: Zope :: 4",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
          "Programming Language :: Python :: 2.7",
          "Programming Language :: Python :: 3.6",
          "Programming Language :: Python :: 3.7",
      ],
      keywords='',
      author='Ross Patterson',
      author_email='me@rpatterson.net',
      url='https://github.com/collective/Products.PDBDebugMode',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Products'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.monkeypatcher',
          # -*- Extra requirements: -*-
          'six',
      ],
      extras_require={
          'ipdb': ['ipdb>=0.3'],
          'zodb': ['zope.testrunner'],
          'zodb-testing': ['zope.testing'],
      },
      entry_points={
          # -*- Entry points: -*-
          'z3c.autoinclude.plugin': 'target = plone',
      },
      )
