from setuptools import setup, find_packages

setup(
    name="config-transformer",
    version="1.0",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "toml==0.10.2",
        "argparse==1.4.0"
    ],
    entry_points={
        'console_scripts': [
            'config-transformer = src.cli:main',
        ],
    },
)
