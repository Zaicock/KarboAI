from setuptools import setup, find_packages

setup(
    name="karboai",
    version="1.0.0",
    author="Hisoka",
    description="KarboAI Python SDK",
    packages=find_packages(),
    install_requires=[
        "requests>=2.32.0"
    ],
    python_requires=">=3.8",
)
