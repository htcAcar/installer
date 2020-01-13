import setuptools

with open("README.md", "r") as  fh:
    long_description=fh.read()


setuptools.setup(
    name="installer",
    version="1.0.0",
    author="Hatice Acar,Berilcan Kutlu, Emrah Urhan",
    author_email="hatice_acar@hacettepe.edu.tr, kutlu.berilcan@student.atilim.edu.tr, eurhan@infodif.com",
    description="File installer",
    long_description= long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/hatice_acar/mini_installer",
    packages=setuptools.find_packages(),
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
     entry_points={
        'console_scripts' : ['mini_installer=mini_installer.main:main'],
    },
    install_requires=[
        'PyYaml',
        'argparse',
    ],

)