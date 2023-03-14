#!/bin/bash




docker build -f analyze-signature-Dockerfile-3.10 --tag analyze-signature-python-3-10 .
docker run --rm analyze-signature-python-3-10 > analyze-signature-python-3.10.txt


