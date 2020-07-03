import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="markdown_code_symlinks",
    version="0.0.2",
    author="SymbiFlow Authors",
    author_email="symbiflow@lists.librecores.org",
    description="Python library to solve cross-reference links \
            when building sphinx documentation.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/SymbiFlow/markdown-code-symlinks",
    packages=setuptools.find_packages(),
    install_requires=['docutils', 'sphinx', 'recommonmark', 'packaging'],
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 2.7",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: ISC License",
        "Operating System :: OS Independent",
    ],
)
