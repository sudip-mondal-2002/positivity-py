from setuptools import setup, find_packages
import os,codecs
VERSION = '1.1.0'
DESCRIPTION = 'Detecting if text is in positive or negative sense. Can be used to classify reviews.'
LONG_DESCRIPTION = 'Detecting if text is in positive or negative sense. Can be used to classify reviews. Created using the logics of natural language processing.'
here = os.path.abspath(os.path.dirname(__file__))

with codecs.open(os.path.join(here, "README.md"), encoding="utf-8") as fh:
    long_description = "\n" + fh.read()
# Setting up
setup(
    name="positivitypy",
    version=VERSION,
    author="sudip-mondal-2002 (Sudip Mondal)",
    author_email="<sudipmondal.2002@rediffmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=long_description,
    packages=find_packages(),
    install_requires=['opencv-python', 'pyautogui', 'pyaudio'],
    keywords=['python', 'NLP', 'machine-learning', 'review', 'classification'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)