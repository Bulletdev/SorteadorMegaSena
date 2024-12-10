#!/usr/bin/env python3

#
#              ⢀⣴⣿⣿⣿⣿⣿⣶⣶⣶⣿⣿⣶⣶⣶⣶⣶⣿⡿⣿⣾⣷⣶⣶⣾⣿⠀                                                                                                                          
#            ⣠⣿⣿⢿⣿⣯⠀⢹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⡇⣿⣿⣿⣿⣿⡇                                                                                                         
#        ⠀⣰⣿⣿⣷⡟⠤⠟⠁⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⡇⣿⣿⣿⣿⣿⡇ 
#       ⠀⣿⣿⣿⣿⣿⣷⣶⣿⣿⡟⠁⣮⡻⣿⣿⣿⣿⣿⣿⣿⣿⢸⡇⣿⣿⣿⣿⣿⡇ 
#       ⠘⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠀⣿⣿⣹⣿⣿⣿⣿⣿⣿⡿⢸⡇⣿⣿⣿⣿⣿⡇ 
#        ⠀⠙⢿⣿⣿⣿⡿⠟⠁⣿⣿⣶⣿⠟⢻⣿⣿⣿⣿⣿⣿⡇⣼⡇⣿⣿⣿⣿⣿⠇
#        ⠀⠀⠈⠋⠉⠁⣶⣶⣶⣿⣿⣿⣿⢀⣿⣿⣿⣿⣿⣿⣿⣇⣿⢰⣿⣿⣿⣿⣿⠀ 
#          ⠀⠀⠀⠀⠀⠙⠿⣿⣿⣿⡄⢀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣽⣿⣼⣿⣿⣿⣿⠇⠀ 
#         ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠚⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠿⠿⠿⠿⠿⠋⠀⠀ 
#       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ 
#       ⠀⠀⠀⣿⣙⡆⠀⠀⡇⠀⢸⠀⠀⢸⠀⠀ ⢸⡇⠀⠀⢸⣏⡉  ⠙⡏⠁⠀ 
#       ⠀⠀⠀⣿⣉⡷⠀⠀⢧⣀⣼ ⠀⢸⣀  ⢸⣇⡀ ⢸⣏⣁⠀ ⠀⡇⠀ 
```
from setuptools import setup, find_packages # type: ignore

setup(
    name='SorteadorMegaSena',
    version='0.1.0',
    description='Gerador de números para Mega-Sena com análise estatística',
    author='Michael Bullet',
    author_email='seu.email@example.com',
    packages=find_packages(),
    install_requires=[],
    entry_points={
        'console_scripts': [
            'mega-sena-generator=mega_sena.app:main',
        ],
    },
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: End Users/Desktop',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
    ],
    python_requires='>=3.8',

#          ____          _  _        _     _____   ______ __      __
 #        |  _ \        | || |      | |   |  __ \ |  ____|\ \    / /
  #       | |_) | _   _ | || |  ___ | |_  | |  | || |__    \ \  / /
   #      |  _ < | | | || || | / _ \| __| | |  | ||  __|    \ \/ /
    #     | |_) || |_| || || ||  __/| |_  | |__| || |____    \  /
     #    |____/  \__,_||_||_| \___| \__| |_____/ |______|    \/


 
)