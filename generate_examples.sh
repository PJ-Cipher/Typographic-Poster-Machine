#!/bin/bash
mkdir -p examples

python poster.py "The cosmos is within us. We are made of star-stuff." \
  --author "Carl Sagan" --style editorial --color coral \
  --output examples/editorial.png

python poster.py "Stay hungry. Stay foolish." \
  --author "Steve Jobs" --style brutalist --color black \
  --output examples/brutalist.png

python poster.py "We are all just walking each other home." \
  --author "Ram Dass" --style noir --color blue \
  --output examples/noir.png

python poster.py "Simplicity is the ultimate sophistication." \
  --author "Leonardo da Vinci" --style minimal --color teal \
  --output examples/minimal.png

python poster.py "Not all those who wander are lost." \
  --author "J.R.R. Tolkien" --style vintage --color amber \
  --output examples/vintage.png

python poster.py "Do not go gentle into that good night." \
  --author "Dylan Thomas" --style bold --color purple \
  --output examples/bold.png

echo "Done! Check the examples/ folder."