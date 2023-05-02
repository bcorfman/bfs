#!/bin/bash
sudo apt update
sudo apt install -y nodejs
poetry config virtualenvs.in-project true
poetry config virtualenvs.prefer-active-python true 
poetry install
