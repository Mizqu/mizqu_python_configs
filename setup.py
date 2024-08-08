from setuptools import setup, find_packages

setup(
    name="mizqu_configs",
    version="1.0.0",
    packages=find_packages(),
    url = "https://github.com/Mizqu/mizqu_python_configs",
    install_requires="pypyodbc >= 1.3",
    python_requires=">=3.10"
)
