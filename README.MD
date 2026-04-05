# Template for a Blender extension 

## Packages a blender extension as a wheel

This template includes:
- Build scripts to automate the process of building wheel files and updating the manifest file.
- A pytest launching script, to run tests in Blender's headless mode
- A minimal example of a Blender extension that uses Python wheel files as dependencies.

## Adaptation Instructions:
- replace placeholder values `ext_name` to be the name of your extension.
- add dependencies to the requirements.txt file
- set the variables for your extension in the makefile
- implement code in the `/ext_name` directory
- implement tests in the `/ext_name` directory within relevant submodule named test_*.py

## Build process:

- A makefile is used to automate building and testing, with the following commands:
    - `make build` to build the wheel file, fetch dependency wheels, and zip extension for distribution.
    - `make test` to run tests in Blender's headless mode.
    - `make clean` to clear the wheel files and the manifest file wheels.
    
