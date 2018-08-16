from distutils.core import setup

setup(
    name="datasets",
    version="1.0",
    description="datasets, a set of utility classes for loading image datasets",
    author="Romain Mormont",
    author_email="romain.mormont@gmail.com",
    packages=["datasets"],
    install_requires=['scikit-learn', 'numpy', 'pillow']
)
