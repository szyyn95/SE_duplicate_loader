#!/bin/bash
cd totalDownload
for archive in *.7z; do 
	newFolder="`basename \"$archive\" .7z`"
	if [ $newFolder == "math.stackexchange.com" ]
	then
		echo $newFolder

		7za x -o"$newFolder" "$archive"

		post="$newFolder""/Posts.xml"
		postLink="$newFolder""/PostLinks.xml"
		nonDuplicatesRation=1.5
		exportDirectory="../allTXT/"
		exportType="txt"
		exportName="$(basename "$newFolder")"
		echo $exportName
		command="python3 ../start.py --posts $post --postsLinks $postLink --nonDuplicatesRatio $nonDuplicatesRation --exportDirectory $exportDirectory --exportType $exportType --exportName $exportName --mute 1 --txtDelimiter '<***>'"
		eval $command

		rm -r "`basename \"$archive\" .7z`"
	fi
done

# for d in */ ; do
# 	# echo $d
# 	post="$d""Posts.xml"
# 	postLink="$d""PostLinks.xml"
# 	nonDuplicatesRation=1.5
# 	# exportDirectory="../allCSV/"
# 	exportDirectory="../totalTXT/"
# 	# exportType="csv"
# 	exportType="txt"
# 	exportName="$(basename "$d")"

# 	command="python3 ../start.py --posts $post --postsLinks $postLink --nonDuplicatesRatio $nonDuplicatesRation --exportDirectory $exportDirectory --exportType $exportType --exportName $exportName --mute 1 --txtDelimiter '<***>'"
# 	eval $command
# 	# command="python3 ../mergeCSV.py"
# 	# eval $command
# done