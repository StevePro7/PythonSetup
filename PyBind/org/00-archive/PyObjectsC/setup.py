from setuptools import setup, Extension

module = Extension('factorial', sources=['factorial.c'])

setup(name='Factorial',
      version='1.0',
      description='Factorial calculator C extension',
      ext_modules=[module])