#!/bin/zsh
set -x
rm -f twpos-data-v0.3/**/.*
# zip -r twpos-data-v0.3.zip twpos-data-v0.3
tar czf twpos-data-v0.3.tgz twpos-data-v0.3

