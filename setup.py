from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))
with open(path.join(here, 'README.rst'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='fontmeta',
    version='1.4.0',
    description='An Utility to get ttf/otf font metadata',
    long_description=long_description,
    url='https://github.com/codesigntheory/fontmeta',
    author='Utsob Roy',
    author_email='roy@codesign.com.bd',
    license='MIT',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only'
    ],
    keywords='Font TTF OTF',
    packages=find_packages(where='src'),
    package_dir={"": "src"},
    py_modules=["fontmeta"],
    install_requires=['fonttools'],
    entry_points={
        'console_scripts': [
            'fontmeta=fontmeta:main',
        ],
},
)
