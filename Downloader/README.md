# RumbleVerse Build Downloader

## Overview

This script is designed to automate the process of downloading and installing builds for RumbleVerse. It fetches available builds from a specified API, allows the user to select a build, downloads the chosen build, and optionally unzips the downloaded file to a specified directory.

## Features

- Fetches available builds from a given API URL.
- Displays a list of available builds for user selection.
- Downloads the selected build to a specified directory.
- Optional unzipping of the downloaded build.

## Requirements

To run this script, you need Python installed on your system. Additionally, the following Python packages are required:

- `requests`
- `zipfile` (built-in, no installation required)
- `os` (built-in, no installation required)
- `time` (built-in, no installation required)

These dependencies are listed in the `requirements.txt` file.

## Installation

1. Clone the repository or download the script.
2. Install the required Python packages:
   
   ```bash
   pip install -r requirements.txt


## Usage

1. Run the script in a Python environment:
    
   ```bash
   pip install -r requirements.txt

2. Follow the on-screen prompts to select and download a build.

## Configuration

Before running the script, ensure the API URL is correctly set to point to the RumbleVerse builds API. The default API URL is set in the script, but it can be modified to point to a different endpoint if needed.

### Setting the API URL

1. In the script, locate the following line:
   
   ```python
   API_URL = "https://rvapi.ferivoq.me/api/"

Replace the URL with the desired API endpoint. Ensure that the new API URL points to a valid and accessible API that provides RumbleVerse build information in a compatible format.

## Building to .exe

For building an .exe file you will need Windows.
Run the `build.bat` file and it will do it's job.

## Contributing

We warmly welcome contributions to this project. Whether it's improving the code, fixing bugs, or adding new features, your help is appreciated.

### Guidelines for Contributing
1. **Fork the Repository**: Start by forking the repository and then cloning your fork to your local machine.
2. **Create a New Branch**: For each new feature or fix, create a new branch based on the latest version of the main branch.
3. **Code Conventions**: Follow the existing code style and conventions. Write clean, readable, and well-documented code.
4. **Test Your Changes**: Ensure that your changes do not break existing functionality. Test the script thoroughly.
5. **Submit a Pull Request**: Push your changes to your fork and submit a pull request to the main repository. Provide a clear description of the changes and the purpose of the pull request.

## License

This script is released under the MIT License.

### MIT License Summary
- **Permission**: The software and its associated documentation files can be used, copied, modified, merged, published, distributed, sublicensed, and/or sold.
- **Conditions**: Appropriate credit must be given, and the MIT License text must be included in substantial portions of the software.
- **Limitations**: The software is provided 'as is', without warranty of any kind.

For more details, refer to the full [MIT License](https://opensource.org/licenses/MIT).

