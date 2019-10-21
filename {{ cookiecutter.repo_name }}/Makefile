#################################################################################
# GLOBALS                                                                       #
#################################################################################

PROJECT_DIR := $(shell dirname $(realpath $(lastword $(MAKEFILE_LIST))))
S3BUCKET = {{ cookiecutter.s3_bucket }}
S3PROFILE = {{ cookiecutter.aws_profile }}
MINIO = {{ cookiecutter.minio }}
MINIOPROFILE = {{ cookiecutter.minio_profile }}
PROJECT_NAME = {{ cookiecutter.repo_name }}
PYTHON_INTERPRETER = {{ cookiecutter.python_interpreter }}
# GIT = {{ cookiecutter.git_remote_repo }}
USERNAME = {{ cookiecutter.author_name }}

#################################################################################
# COMMANDS                                                                      #
#################################################################################

## Install Python Dependencies
requirements: test_environment
	$(PYTHON_INTERPRETER) -m pip install -U pip setuptools wheel
	$(PYTHON_INTERPRETER) -m pip install -r requirements.txt


## Delete all compiled Python files
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete

## Lint using flake8
lint:
	flake8 src

## Make Dataset
data: requirements
	$(PYTHON_INTERPRETER) src/data/make_dataset.py data/raw data/processed

## Upload Data to S3
sync_data_to_s3:
ifeq (default,$(S3PROFILE))
	aws s3 sync data/ s3://$(S3BUCKET)/data/
else
	aws s3 sync data/ s3://$(S3BUCKET)/data/ --profile $(S3PROFILE)
endif

## Download Data from S3
sync_data_from_s3:
ifeq (default,$(S3PROFILE))
	aws s3 sync s3://$(S3BUCKET)/data/ data/
else
	aws s3 sync s3://$(S3BUCKET)/data/ data/ --profile $(S3PROFILE)
endif

## Upload to minio
sync_data_to_minio:
ifeq (default,$(MINIOPROFILE))
	rclone --size-only sync data/ $(MINIO)/data/ --stats-one-line -P --stats 2s

## Download from minio
sync_data_to_minio:
ifeq (default,$(MINIOPROFILE))
	rclone --size-only sync $(MINIO)/data/ data/ --stats-one-line -P --stats 2s


## Initial set up of python interpreter environment, version control and pre-commit hooks
initial_setup:
	@bash -c "virtualenv -p $(PYTHON_INTERPRETER) $(HOME)/envs/$(PROJECT_NAME)"
	@bash -c "git init"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install dvc[all]; dvc init"
	@bash -c "echo '[core]' >> $(PROJECT_DIR)/.dvc/config"
	@bash -c "echo 'analytics = false' >> $(PROJECT_DIR)/.dvc/config"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install pre-commit; pre-commit install; pre-commit autoupdate"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install -r $(PROJECT_DIR)/requirements.txt"
	@bash -c "echo 'CWD=$(PROJECT_DIR)' >> $(PROJECT_DIR)/.env"
	@bash -c "git add . ; git commit -am 'INITIAL COMMIT'"
	@bash -c "git remote add origin https://github.com/$(USERNAME)/$(PROJECT_NAME).git"
# 	@bash -c "git remote add origin $(GIT)"	
	@echo ">>> New virtualenv created. Activate with:\nsource $(HOME)/envs/$(PROJECT_NAME)/bin/activate"
	@echo ">>> git and dvc are ready to go"

## Following set up of python interpreter environment, version control and pre-commit hooks
following_setup:
	@bash -c "virtualenv -p $(PYTHON_INTERPRETER) $(HOME)/envs/$(PROJECT_NAME)"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install dvc[all]"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install pre-commit; pre-commit install"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install -r $(PROJECT_DIR)/requirements.txt"
	@echo ">>> New virtualenv created. Activate with:\nsource $(HOME)/envs/$(PROJECT_NAME)/bin/activate"
	@echo ">>> git and dvc are ready to go"

requirements:
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; pip install -r $(PROJECT_DIR)/requirements.txt"

environment:
	@echo ">>> Activate with:\nsource $(HOME)/envs/$(PROJECT_NAME)/bin/activate"

commit:
	$(eval EXP_FILE := "$(PROJECT_DIR)/$(PROJECT_NAME)/study_name.txt")
	$(eval EXP_NAME := $(shell cat ${EXP_FILE}))
	@bash -c "git commit -am \"completed experiment $(EXP_NAME)\"; git tag -a $(EXP_NAME) -m \"$(EXP_NAME)\""

push:
	@bash -c "git push origin --follow-tags"
	@bash -c "source $(HOME)/envs/$(PROJECT_NAME)/bin/activate; dvc push"

#################################################################################
# PROJECT RULES                                                                 #
#################################################################################



#################################################################################
# Self Documenting Commands                                                     #
#################################################################################

.DEFAULT_GOAL := help

# Inspired by <http://marmelab.com/blog/2016/02/29/auto-documented-makefile.html>
# sed script explained:
# /^##/:
# 	* save line in hold space
# 	* purge line
# 	* Loop:
# 		* append newline + line to hold space
# 		* go to next line
# 		* if line starts with doc comment, strip comment character off and loop
# 	* remove target prerequisites
# 	* append hold space (+ newline) to line
# 	* replace newline plus comments by `---`
# 	* print line
# Separate expressions are necessary because labels cannot be delimited by
# semicolon; see <http://stackoverflow.com/a/11799865/1968>
.PHONY: help
help:
	@echo "$$(tput bold)Available rules:$$(tput sgr0)"
	@echo
	@sed -n -e "/^## / { \
		h; \
		s/.*//; \
		:doc" \
		-e "H; \
		n; \
		s/^## //; \
		t doc" \
		-e "s/:.*//; \
		G; \
		s/\\n## /---/; \
		s/\\n/ /g; \
		p; \
	}" ${MAKEFILE_LIST} \
	| LC_ALL='C' sort --ignore-case \
	| awk -F '---' \
		-v ncol=$$(tput cols) \
		-v indent=19 \
		-v col_on="$$(tput setaf 6)" \
		-v col_off="$$(tput sgr0)" \
	'{ \
		printf "%s%*s%s ", col_on, -indent, $$1, col_off; \
		n = split($$2, words, " "); \
		line_length = ncol - indent; \
		for (i = 1; i <= n; i++) { \
			line_length -= length(words[i]) + 1; \
			if (line_length <= 0) { \
				line_length = ncol - indent - length(words[i]) - 1; \
				printf "\n%*s ", -indent, " "; \
			} \
			printf "%s ", words[i]; \
		} \
		printf "\n"; \
	}' \
	| more $(shell test $(shell uname) = Darwin && echo '--no-init --raw-control-chars')
