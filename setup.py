import sys
from os.path import join
from setuptools import setup


install_requires = [
    'docopt>=0.6,<0.7'
    'menpofit>=0.3,<0.4',
    'menpodetect>=0.3,<0.4',
    'numpy'  # note that we don't explicitly version numpy,
             # let menpo handle that
]

if sys.version_info.major == 2:
    install_requires.append('pathlib==1.0')

setup(name='menpocli',
      description='A command line interface to the Menpo Project',
      author='James Booth',
      author_email='james.booth08@imperial.ac.uk',
      packages=['menpocli'],
      scripts=[join('bin', 'menpofit')],
      install_requires=install_requires
      )
