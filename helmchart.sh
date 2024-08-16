#!/bin/bash

cd bc4m
helm package ../bc4m-chart
helm repo index .
git add .
git commit -m "bc4m-chart is added"
git push  
