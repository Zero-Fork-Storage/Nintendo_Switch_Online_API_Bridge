#!/bin/sh -e

set -x

isort nso_bridge tests --force-single-line-imports
autoflake --remove-all-unused-imports --recursive --remove-unused-variables --in-place nso_bridge tests --exclude=__init__.py
black nso_bridge tests
isort nso_bridge tests
