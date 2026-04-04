"""----------------------------------------------------------------------------

This script updates the list of wheel files in the blender_manifest.toml file.

It reads the list of wheel files built from the wheels directory, updates the
list in the blender_manifest.toml file by writing the new list to the file.

This is called as part of the build process to ensure that the manifest file is always
up to date with the latest wheel files.

----------------------------------------------------------------------------"""

import os


def update_wheels_manifest(wheels_dir, manifest_path):
    """
    This script is meant to update the 'blender_manifest.toml' file.
    It updates the list of wheel files in the manifest.
    """

    # List of packages already covered by other dependencies, in the case of multiple extensions being installed. 
    EXCLUDED_PACKAGES = [] # ex "numpy", "pandas", etc. 

    # Get the list of wheel files in the wheels directory:
    wheel_files = [
        f for f in os.listdir(wheels_dir)
        if f.endswith(".whl")
        and not any(f.lower().startswith(pkg) for pkg in EXCLUDED_PACKAGES)
    ]

    # Read the existing manifest file:
    lines = []
    with open(manifest_path, "r") as f:
        lines = f.readlines()

    # Find the starting line number of the wheels list in the manifest file:
    wheel_start_index = lines.index("wheels = [\n") + 1

    # Remove existing wheel files from the wheel list in the manifest file:
    while lines[wheel_start_index].strip() != "]":
        lines.pop(wheel_start_index)

    # Add the new wheel names to the manifest file:
    for wheel_file in wheel_files:
        lines.insert(wheel_start_index, f'"./wheels/{wheel_file}", \n')
        wheel_start_index += 1

    # Write the updated manifest back to the file:
    with open(manifest_path, "w") as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    # Get path to Wheels folder:
    wheels_dir = os.path.join(os.path.dirname(__file__), "..", "wheels")

    # Get path to manifest file:
    manifest_path = os.path.join(
        os.path.dirname(__file__), 
        "..", 
        "blender_manifest.toml"
    )

    # Update the manifest file:
    update_wheels_manifest(wheels_dir, manifest_path)