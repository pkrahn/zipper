# count foxes in .txt data files
 for filename in *.txt; do echo $filename; cut -d , -f 2 "$filename" | grep fox | sort | uniq -c; done
