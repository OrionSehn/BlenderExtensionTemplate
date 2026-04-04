
.PHONY: build wheels release 

PYTHON_VERSION = 3.11
PLATFORM = win_x86_64
EXT_NAME = ext_name

wheels: 
	sudo apt install zip
	sudo apt install python$(PYTHON_VERSION)
	sudo apt install python3-pip
	rm -rf src/crob/wheels/
	mkdir -p src/crob/wheels/
	python$(PYTHON_VERSION) -m pip download -r requirements.txt --dest ./src/$(EXT_NAME)/wheels --only-binary=:all: --python-version=$(PYTHON_VERSION) --platform=$(PLATFORM)
	python$(PYTHON_VERSION) src/crob/scripts/update_wheels_manifest.py
	@echo "Wheels Built"



zip: 
	cd src && find $(EXT_NAME) -type f | zip ../build/$(EXT_NAME) -@
	@echo "Build done"

build: wheels zip
	
test:
	@echo "Running tests..."

