#!/bin/bash

for build in {129..148}; do
    echo $build
    cat $build.txt | grep "Generated [0-9][0-9]* mutations Killed [0-9][0-9]*"
done
