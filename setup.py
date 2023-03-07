import setuptools
with open("README.md", "r", encoding="utf-8") as fh:
 long_description = fh.read()
setuptools.setup(
 name="NYPD-final-4egis",
 version="0.0.1",
 author="Jedrzej Rymsza",
 author_email="j.rymsza@student.uw.edu.pl",
 description="Zadanie zaliczeniowe na NYPD",
 long_description=long_description,
 long_description_content_type="text/markdown",
 url="https://github.com/4egis/NYPD-Final-assignment",
 packages=setuptools.find_packages(),
 classifiers=[
 "Programming Language :: Python :: 3",
 "License :: OSI Approved :: MIT License",
 "Operating System :: OS Independent",
 ],
 python_requires='>=3.6',
)