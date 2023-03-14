#!/bin/bash


set -e



VERSION=3.8



rm -rf _temp
cp -R ../src _temp

docker build -f check-signature-Dockerfile-$VERSION --tag check-signature-python-$VERSION .
docker run --rm check-signature-python-$VERSION > check-signature-python-$VERSION.txt

rm -rf _temp


