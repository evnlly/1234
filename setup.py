from setuptools import setup
setup(
    name='m1234',
    version='1.0',
    description='Provides a decorator for memory usage tracking. The part of FOSS␣→course.',
    license='MIT',
    author='evnlly',
    author_email='anastasia@borodulina.me',
    url='https://github.com/evnlly/1234',
    packages=['mtracker'],
    install_requires=[], # it is empty since we use standard python library
    extras_require={
        'test': [
        'pytest',
        'coverage',
        ],
    },
    python_requires='>=3',
)