# Makefile to run python files.
# Yes, I am using the powershell script to make a docker file to run make commands.

CWD := $(CURDIR)
NAME := cat-cnn

.DEFAULT:
	@echo ""
	@echo "make <OPTIONS>"
	@echo "OPTIONS choices:"
	@echo "	run 	- begins training CNN model"
	@echo "	clean 	- cleans created files, if any"
	@echo ""
	@echo "See make file for docker commands"

run:
	python3 ./src/main.py

clean:
	rm *.png

test:
	-$(MAKE) clean
	python3 test.py


# --------
# Docker scripts
# --------

# build the docker image
docker-build:
	docker build -t $(NAME) $(CWD)

# run the docker image
docker-run:
	docker run --rm -it -v "$(CWD):/usr/$(NAME)" -w /usr/$(NAME) $(NAME)

# remove the docker image
docker-clean:
	docker rmi $(NAME)

# print current docker images (check if the docker image was made)
docker-images:
	docker images

# create docker container
docker:
	$(MAKE) docker-build
	$(MAKE) docker-run