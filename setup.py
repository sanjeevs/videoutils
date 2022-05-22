from setuptools import setup

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="videoutils",
    version="0.0.1",
    description="Scripts for saving and splitting video files for other projects",
    scripts=['scripts/video_capture.py', 'scripts/video_split.py'],
    long_description=long_description,
    long_description_content_type="text/markdown",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 3 - Alpha"
    ],

    url="https://github.com/sanjees/videoutils",
    author="Sanjeev Singh",
    author_email="snjvsingh123@gmail.com",

    install_requires = ['opencv-python>=4'],
    py_modules = ['videoutils'],
    extras_require = {
        "dev": [
            "pytest >= 3.7",
            "check-manifest",
            "twine",
        ],
    },
)