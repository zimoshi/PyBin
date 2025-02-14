from setuptools import setup, find_packages

setup(
    name="pybin",
    version="0.1.0",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "pybin=pybin.org:main",
        ],
    },
    install_requires=[],
    python_requires=">=3.8",
    description="A custom Python bytecode compiler producing .pybin files",
    author="Your Name",
    author_email="153401092+zimoshi@users.noreply.github.com", 
    license="MIT",
)
