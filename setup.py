
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
     name='Chromos',
     version='1.4',
     scripts=['Chromos.py'] ,
     author="devanshshukla99",
     description="A Package for Getting Colored Text in CLI ",
     long_description= long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/devanshshukla99/Chromos",
     license = "MIT LICENCE",
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )


# python3 setup.py bdist_wheel
