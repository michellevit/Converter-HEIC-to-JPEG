# HEIC Converter


![Python](https://img.shields.io/badge/Python-3.12.0-ffdb4f.svg)
![Pillow](https://img.shields.io/badge/Pillow-10.3.0-blue.svg)


A Python script that converts .heic files into .jpg format.


## Table of Contents
- [Dependencies](#dependencies)
- [How To Install](#how-to-install)
- [How To Run the Converter](#how-to-run)
- [Credits](#credits)


## Dependencies<a name="dependencies"></a>
- Python 3.12.0
- Pillow Library 10.1.0


## How To Install<a name="how-to-install"></a>
- Download the repository
- Create a virtual environment
    - Make sure python is downloaded
    - Open Powershell terminal
    - Navigate to HEIC-Converter root directory
    - Run: `python -m venv venv`
- Install Dependencies
    - Run: `pip install -r requirements.txt`
- Activate virtual env
  - Navigate to HEIC-Converter root directory
  - Run: `.\venv\Scripts\activate`
- Add .heic files to the 'files-unconverted' folder
- Double-click the 'run-converter.bat' file
- Converted filed will be listed in terminal, and should appear in the 'files-converted' folder


## How To Run the Converter<a name="how-to-run"></a>
- Save a .png file to the project folder
  * Note: make sure there are no other .png files in the folder
- Double-click the 'run-generator.bat' file
- The favicon will appear in the project folder (of file type .ico)
  * Note: This converter will not resize the image, so make sure the input file has the correct dimensions (recommended: 32px x 32px)


## Credits<a name="credits"></a>
Michelle Flandin