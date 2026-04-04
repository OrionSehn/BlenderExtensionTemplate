
.PHONY: build wheels release 

PYTHON_VERSION = 3.11
PLATFORMS = win_x86_64


# Builds dependencies for CROB not covered by Bonsai + Blender
wheels: 
	sudo apt install zip
	sudo apt install python3.11
	sudo apt install python3-pip
	rm -rf src/crob/wheels/
	mkdir -p src/crob/wheels/
	python3.11 -m pip download -r requirements.txt --dest ./src/crob/wheels --only-binary=:all: --python-version=3.11 --platform=win_amd64
	python3.11 src/crob/scripts/update_wheels_manifest.py
	@echo "Wheels Built"

build:
	cd src && find crob -type f | zip ../build/CROB -@
	@echo "Build done"

release:
	mkdir -p src/crob/wheels/
	echo "Building CROB wheels..."
	python3.11 -m pip download -r requirements.txt --dest ./src/crob/wheels --only-binary=:all: --python-version=3.11 --platform=win_amd64
	python3.11 src/crob/scripts/update_wheels_manifest.py
	cd src && zip -r CROB.zip crob
