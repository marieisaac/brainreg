from setuptools import setup, find_namespace_packages
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

requirements = [
    "bg-atlasapi",
    "bg-space",
    "numpy",
    "configparser",
    "scikit-image",
    "multiprocessing-logging",
    "configobj",
    "slurmio",
    "imio",
    "fancylog",
    "imlib>=0.0.26",
    "napari[pyside2]>=0.3.7",
    "napari-brainreg",
    "brainreg-segment>=0.0.2",
]


setup(
    name="brainreg",
    version="0.2.2",
    description="Automated 3D brain registration",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements,
    extras_require={
        "dev": [
            "black",
            "pytest-cov",
            "pytest",
            "coverage",
            "bump2version",
            "pre-commit",
            "flake8",
        ]
    },
    python_requires=">=3.7",
    packages=find_namespace_packages(exclude=("docs", "tests*")),
    entry_points={
        "console_scripts": [
            "brainreg = brainreg.cli:main",
        ]
    },
    include_package_data=True,
    author="Adam Tyson, Charly Rousseau",
    author_email="adam.tyson@ucl.ac.uk",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Operating System :: POSIX :: Linux",
        "Operating System :: Microsoft :: Windows :: Windows 10",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
    ],
    zip_safe=False,
)
