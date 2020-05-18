import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

packages = setuptools.find_packages() 
packages.append('.')

setuptools.setup(
    name='raspi-view',  
    version='0.4.1',
    scripts=['raspi-view'] ,
    author="Zsolt Farkas",
    description="An app to display different views on a Raspberry Pi HAT with display sh1106",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zsfarkas/raspi-view",
    packages=setuptools.find_packages(),
    keywords="raspi,raspberry,hat,display,view,monitor,screen",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)