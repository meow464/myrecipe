from distutils.core import setup, Extension


# Put the name of your extension here
setup(name='myrecipe',
      version='1.0',
      ext_modules=[
          Extension('myrecipe', # Put the name of your extension here
                    ['myrecipe.c', 'version.m'],
                    libraries=[],
                    library_dirs=[],
                    )
      ] 
    )
