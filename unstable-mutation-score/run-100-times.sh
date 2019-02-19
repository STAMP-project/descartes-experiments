#!/bin/bash

for run in {1..100}
do
  mvn -Pquality org.pitest:pitest-maven:mutationCoverage@pitest-check -Dverbose=true -DoutputFormats=JSON,METHODS -DreportsDirectory=target/pit-reports/`date +"%s"` -DtimestampedReports=false> target/$run.output.txt
  sleep 1
done