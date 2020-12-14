#!/bin/bash
# {{@@ header() @@}}
#
# Vokabeln von http://www.vokabeln.de/v5/vorschau/Griechisch_Alltag.htm
# bis und mit Basiswortschatz: Abschnitt 1 bis 10: Abschnitt 10


IFS='%'
entry=($(grep -v "^#" ~/.i3/greek/basiswortschatz.csv | shuf | tail -n 1))
unset IFS
echo "German: ${entry[0]}"
echo "Greek: ${entry[1]}"
