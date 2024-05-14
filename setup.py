from setuptools import find_packages, setup

def get_requirements()->List[str]:
    requirements_list : List[str] = []
    return requirements_list
setup(
    name="sensor",
    version="0.0.2",
    author="testuser",
    author_email="test@cdac.in",
    packages=find_packages(),
    install_requires= get_requirements() #["pymongo"]
)
