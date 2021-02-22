#!/usr/bin/env bash

docker run -d -p 8070:8080 -e PORT="8080" check
