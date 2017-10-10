#!/bin/sh

j=0
for i in `ls |  sort --version-sort`
do
	file_name=`printf "frame-%05d.obj" "$j"`;
	echo $i "-->" $file_name
	mv $i $file_name -v
	let j=j+1;
done
