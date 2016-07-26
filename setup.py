from setuptools import setup, find_packages

setup(
    name='FlexGet-extras',
    version='1.0',
    description='Collection of FlexGet plugins',
    packages=find_packages(exclude=['tests']),
    install_requires=['FlexGet>2.2'],
    tests_require=['pytest'],
    entry_points="""
        [FlexGet.plugins]
        from_uoccin = extras.input.from_uoccin
        uoccin_lookup = extras.metainfo.uoccin_lookup
        uoccin_processors = extras.output.uoccin_processors"""
)
