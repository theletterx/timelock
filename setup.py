from distutils.core import setup, Extension

kernels_sha256 = Extension('timelock.kernels.sha256',
                    libraries = ['crypto'],
                    sources = ['timelock/kernels/sha256module.c'])

setup (name = 'Timelock',
       version = '0.1.1',
       description = 'Timelock encryption',
       ext_modules = [kernels_sha256])


