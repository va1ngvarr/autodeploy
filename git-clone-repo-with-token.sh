#!/usr/bash

{ # try
    git clone https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}
} || { # catch
	cd ${GITHUB_REPOSITORY_PATH}
    git pull https://${GITHUB_USER}:${GITHUB_TOKEN}@github.com/${GITHUB_REPOSITORY}
}
