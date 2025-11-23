import setuptools
   
setuptools.setup(
    name="cadmus_methods_extraction",
    version="0.1.0",
    author="Simona E. Doneva",
    author_email="donevasimona@gmail.com",
    description="A lightweight standalone tool for extracting the Methods section from biomedical full-text articles, designed as a complement to cadmus.",
    packages=setuptools.find_packages(),
    classifiers=[
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: LINUX/MACOS",
       ],
    install_requires=[
      'pandas',
      'bs4',
      'biopython',
      'python-dateutil',
      'lxml',
      'IPython',
      'papermage[dev,predictors,visualizers]',
      'ftfy',
      'pyarrow==20.0.0',
      ],
    python_requires='==3.11'
)
