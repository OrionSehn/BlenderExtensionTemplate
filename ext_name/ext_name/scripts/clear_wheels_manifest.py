"""----------------------------------------------------------------------------

This script is meant to clear the list of wheel files in the 'blender_manifest.toml' file.

It removes all wheel files from the manifest, so that the manifest is ready to be updated with new wheel files.

This is useful when you want to clear the manifest before adding new wheel files, 
to ensure that the manifest is always up to date with the latest wheel files.

It is called as part of the cleanup step in the build process. 

----------------------------------------------------------------------------"""

import os


def clear_wheels_manifest(manifest_path):
    """
    This script is meant to update the 'blender_manifest.toml' file.
    It updates the list of wheel files in the manifest.
    """

    # Read the existing manifest file:
    lines = []
    with open(manifest_path, "r") as f:
        lines = f.readlines()

    # Find the starting line number of the wheels list in the manifest file:
    wheel_start_index = lines.index("wheels = [\n") + 1

    # Remove existing wheel files from the wheel list in the manifest file:
    while lines[wheel_start_index].strip() != "]":
        lines.pop(wheel_start_index)

    #  clear the lines between the wheel list in the manifest file:
    while lines[wheel_start_index].strip() != "]":
        lines.pop(wheel_start_index)

    # Write the updated manifest back to the file:
    with open(manifest_path, "w") as f:
        for line in lines:
            f.write(line)


if __name__ == "__main__":
    # Get path to Wheels folder:
    wheels_dir = os.path.join(os.path.dirname(__file__), "..", "..", "wheels")

    # Get path to manifest file:
    manifest_path = os.path.join(
        os.path.dirname(__file__), 
        "..", 
        "..",
        "blender_manifest.toml"
    )

    # Update the manifest file:
    clear_wheels_manifest(manifest_path)