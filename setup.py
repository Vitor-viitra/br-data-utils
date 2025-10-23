from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="br_data_utils_vitorgdias",
    version="0.0.1",
    author="vitorgdias",
    author_email="vitorgdias.data@gmail.com",
    description="Pacote simples para limpar e validar dados brasileiros.",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vggd18/br-data-utils",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)