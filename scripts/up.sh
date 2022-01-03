#! /bin/bash

end=$((SECONDS+15))
arr=(hello bootay erin sexy pants ohyeah sweet juicy yum nice hottness fire spicy extra)

randArrayElement(){ arr=("${!1}"); say ${arr["$[RANDOM % ${#arr[@]}]"]}; }

open http://unknowablesymbols.com -a /Applications/Google\ Chrome.app/

open ~/Music/slow_mixtape/06-rain.mp3 -a /Applications/VLC.app/

while [ $SECONDS -lt $end ]; do
  randArrayElement "arr[@]"
  sleep 1
  :
done