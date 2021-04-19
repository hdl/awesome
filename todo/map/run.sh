#!/usr/bin/env bash

cd $(dirname "$0")

dot -Tsvg map.dot -o map.svg
