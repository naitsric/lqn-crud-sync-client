from setuptools import find_packages, setup


setup(
    name='crud-sync-client',
    description='This client comunicate with crud-sync',
    author='Cristian Duque',
    author_email='cristian@loquenecesito.co',
    license='UNLICENSE',
    keywords='lqn',
    packages=find_packages(exclude=['docs', 'tests*']),
    install_requires=[
        'nameko',
    ],
    extras_require={
        'test': ['unittest'],
    }
)