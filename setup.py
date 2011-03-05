from distutils.core import setup, Extension

setup(name = "PyGameRect",
      version = "0.1",
      ext_modules = [Extension("pygamebase", ["base.c"]), Extension("pygamerect", ["rect.c"])])
