#!/bin/bash

DEPLOY_KEY="PRIVATE_KEY"
LOCAL_FILE="/Users/achoi/Desktop/nsregion"

for i in {1..10}
do
  scp -i $DEPLOY_KEY $LOCAL_FILE "USER@HOST:~"
done