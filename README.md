# Furhat Remote API Python Package

[![Example Image](./resources/face.png)](./resosurces/face.png)


This package serves as a guide for utilizing the Furhat robot's Python application. It facilitates the creation of facial expressions using new `.png` assets and textures, compiling them into `.charpack` character pack format. Additionally, it includes scripts demonstrating how to play and modify faces programmatically using Python.

## Installation

You can install the package using pip:

```bash
pip install furhat-remote-api
```

## Usage

### `create_charpacks.py`

This script creates character packs for Furhat. 

- **Global Variables and Paths**:
  - `texture_sources`: Path to the source directory containing texture files (`plot_src`).
  - `char_mane`: Name of the character being created (`Amauri`).
  - `texture_type`: Type of texture being used (`facial-hair`).
  - `texture_name`: Name of the texture (`boxplot`).

- **Functionality**:
  - Copies the source folder to a new folder.
  - Renames and moves images to a designated folder for textures.
  - Updates JSON files with new texture references.
  - Packages the characters into a `.charpack` file.

### `play_faces.py`

This script demonstrates how to play faces, aka change the face after a some time (defined as a paramrter) on Furhat to create animations

- **Global Variables and Paths**:
  - IP address (`10.100.237.184`) or `localhost` for the Furhat robot or SDK.
  
- **Functionality**:
  - Connects to the Furhat robot or SDK using the provided IP address.
  - Retrieves available voices and sets a voice for the robot.
  - Loads a specific face (character) and performs actions like speaking, gestures, and transitioning between different facial expressions.

Remember to replace placeholder variables, such as IP addresses, file paths, and character names, with your specific configurations. These scripts offer an interface to interact with Furhat robot functionalities through Python, enabling users to create and control various facial expressions and actions programmatically.

Refer to the code comments and documentation within the repository for detailed guidance on each script's functionality, inputs, and expected outputs.
