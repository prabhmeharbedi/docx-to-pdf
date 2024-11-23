#!/bin/bash

docker build -t docx-to-pdf .
docker run -d -p 8080:5000 docx-to-pdf
