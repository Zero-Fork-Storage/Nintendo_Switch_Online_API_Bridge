#!/usr/bin/env bash

set -e
set -x

flake8 nso_bridge tests
black nso_bridge tests --check
isort nso_bridge tests --check-only