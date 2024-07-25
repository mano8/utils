"""Setup ve_utils"""
import pathlib
from setuptools import setup

# The directory containing this file
HERE = pathlib.Path(__file__).parent

# The text of the README file
README = (HERE / "README.md").read_text()

setup(name='ve_utils',
      version='2.5.3',
      description='Utilities helper library for Python',
      long_description=README,
      long_description_content_type="text/markdown",
      url='https://github.com/mano8/ve_utils',
      author='Eli Serra',
      author_email='eli.serra173@gmail.com',
      license='MIT',
      classifiers=[
            "License :: OSI Approved :: MIT License",
            "Programming Language :: Python :: 3",
            "Programming Language :: Python :: 3.7",
      ],
      packages=['ve_utils'],
      include_package_data=True,
      python_requires=">=3.5",
      install_requires=[],
      extras_require={
              "TEST": ["pytest", "coverage", "simplejson"],
              "JSON": ["simplejson"],
          },
      zip_safe=False
      )
