mkdir -p tmp
rm -f tmp/urls.txt

while read id
do echo https://osu.ppy.sh/beatmapsets/$id >> tmp/urls.txt
done < id.txt
