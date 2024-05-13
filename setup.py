from setuptools import find_packages, setup

with open ("artemis/README.md", "r") as f:
    long_description = f.read()

setup(
    name='artemis',
    packages=find_packages(where="artemis"),
    version='0.1.0',
    description='Client library to interface with the Artemis vector database',
    package_dir={"": "artemis"},
    long_description= long_description,
    url= "",
    author='Manish Vasu',
    install_requires=[],
    setup_requires=['pytest-runner'],
    extras_require = {"dev": []}
)