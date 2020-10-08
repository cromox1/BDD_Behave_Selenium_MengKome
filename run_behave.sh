#!/bin/bash

masani=`date +%Y%m%d_%H%M%S`
file1=console_output_behave_${masani}.txt

torun="$1"

if [ x"$torun" == x2 ]; then

pwd > 'logs'/"$file1"
echo "$ behave --no-capture " >> 'logs'/"$file1"
echo >> 'logs'/"$file1"
behave --no-capture | tee -a 'logs'/"$file1"

elif [ x"$torun" == x1 ]; then

pwd > 'logs'/"$file1"
echo "$ behave " >> 'logs'/"$file1"
echo >> 'logs'/"$file1"
behave | tee -a 'logs'/"$file1"

else

echo
echo "This script save the console output to a file"
echo "./run_behave.sh 1  -- to run basic behave only"
echo "./run_behave.sh 2  -- to run behave with more info ( --no-capture )"
echo

fi
