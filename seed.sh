#!/bin/bash


# prep data for elastic search
zcat /data/json.gz/all.json.gz >all.json
zcat /data/json.gz/booknames.json.gz >booknames.json
python3 parse.py > data-ndjson.json

# populate the elastic search index
curl -X PUT \
    $1:9200/kjvonly/ \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/json' \
    --data-binary @mapping.json

curl -X PUT \
    $1:9200/kjvonly/_bulk \
    -H 'Cache-Control: no-cache' \
    -H 'Content-Type: application/json' \
    --data-binary @data-ndjson.json

sleep 10000