
.PHONY: deps package wheels zip build clean test

PYTHON_VERSION = 3.11
PLATFORM = win_amd64
EXT_NAME = ext_name
BLENDER_PATH = "C:/Program Files/Blender Foundation/Blender 4.4/blender.exe"

# Updates dependencies for build
deps: 
	sudo apt update
	sudo apt install zip
	sudo apt install python$(PYTHON_VERSION)
	sudo apt install python3-pip
	python$(PYTHON_VERSION) -m pip install --upgrade pip setuptools build

package:
	python$(PYTHON_VERSION) -m build --wheel --outdir build
# 	copy wheel files to extension folder
	cp build/*.whl ./$(EXT_NAME)/wheels/
	python$(PYTHON_VERSION) $(EXT_NAME)/$(EXT_NAME)/scripts/update_wheels_manifest.py

# Grabs wheels for extension dependencies
wheels:
	rm -rf ./$(EXT_NAME)/wheels/
	mkdir -p ./$(EXT_NAME)/wheels/
	python$(PYTHON_VERSION) -m pip download -r requirements.txt --dest ./$(EXT_NAME)/wheels --only-binary=:all: --python-version=$(PYTHON_VERSION) --platform=$(PLATFORM)
	python$(PYTHON_VERSION) $(EXT_NAME)/$(EXT_NAME)/scripts/update_wheels_manifest.py
	@echo "Wheels Built"

# Zips the extension for distribution
zip: 
	find $(EXT_NAME) -type f | zip ./build/$(EXT_NAME) -@
	@echo "Zip Created"

clean:
	rm -rf $(EXT_NAME).egg-info/ 
	python$(PYTHON_VERSION) $(EXT_NAME)/$(EXT_NAME)/scripts/clear_wheels_manifest.py
	@echo "Cleaned build artifacts and cleared manifest"

# Builds the extension, zips for distribution
build: deps wheels package zip clean

# Tests the extension by running pytest in Blender's Python environment
test:
	@echo "Running tests..."
	$(BLENDER_PATH) -P run_pytest.py -b
