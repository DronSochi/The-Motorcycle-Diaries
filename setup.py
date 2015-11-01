from setuptools import setup

setup(
    name='maintenance',
    description="The Motorcycle Diaries -- saving information on motorcycle maintenance",
    version='0.0.1',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Operating System :: POSIX",
        "Programming Language :: Python :: 3.5",
        "Topic :: Internet :: WWW/HTTP",
    ],
    url='https://github.com/DronSochi/maintenance/',
    keywords=['bottle', 'moto', 'motorcycle'],
    packages=['maintenance'],
    install_requires=[
        'bottle',
    ],
    entry_points={
        'console_scripts': [
            'mtctl = maintenance.__main__:main',
        ],
    },
)
