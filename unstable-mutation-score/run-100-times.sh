#!/bin/bash

for run in {1..100}
do
  mvn -Pquality org.pitest:pitest-maven:mutationCoverage@pitest-check -Dverbose=true -DoutputFormats=JSON,METHODS > target/$run.output.txt
done