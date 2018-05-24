#!/bin/bash

# Get data.zip from figshare
wget https://ndownloader.figshare.com/files/11634542 -O data.zip

# Place all the data in the right place
unzip data.zip ../data


# Remove the zip file
rm data.zip