import os
from setuptools import setup

setup(
    use_scm_version={
        'write_to': os.path.join('Chromos', '_version.py')
    }
)
