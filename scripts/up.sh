#! /bin/bash

# Open a youtube video and pause to allow chrome to start autoplaying at random 30sec starting point...
open "https://www.youtube.com/watch?v=9sJUDx7iEJw&t=$[$RANDOM % 30]s" -a /Applications/Google\ Chrome.app/
sleep 10
open "https://www.youtube.com/watch?v=JY-ajPNQMh0&t=$[$RANDOM % 30]s" -a /Applications/Google\ Chrome.app/
sleep 10

# Open a new chrome tab with a visual project...
open http://unknowablesymbols.com -a /Applications/Google\ Chrome.app/

# Randomly chop an audio file to make a random starting point then play it in VLC...
# ffmpeg -ss 10 -t 6 -i ./assets/audio/rain.mp3 ./scripts/temp/output.mp3
# open ./scripts/temp/output.mp3 -a /Applications/VLC.app/

# Create array of words and start saying them randomly at regular time interval...
#arr=(hello bootay erin sexy pants ohyeah sweet juicy yum nice hottness fire spicy extra)
#randArrayElement(){ arr=("${!1}"); say ${arr["$[RANDOM % ${#arr[@]}]"]}; }

# Set time before up script ends and init script resets it...
end=$((SECONDS+45))
while [ $SECONDS -lt $end ]; do
#  randArrayElement "arr[@]"
 sleep 1
 :
done
