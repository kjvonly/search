```
# Note need all.json and booknames.json from kjvdata repo
python parse.py > data-ndjson.json

curl -X PUT \
  http://localhost:9200/kjvonly/ \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  --data-binary @mapping.json

curl -X PUT \
  http://localhost:9200/kjvonly/_bulk \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  --data-binary @data-ndjson.json

# Delete Index
curl -XDELETE   http://localhost:9200/kjvonly

curl -X GET   http://localhost:9200/kjvonly/_doc/1_1_1   -H 'Cache-Control: no-cache'

curl -X GET \
  'http://localhost:9200/kjvonly/_doc/_search?q=beware' \
  -H 'Cache-Control: no-cache' \


curl   --silent -X POST \
  http://localhost:9200/kjvonly/_doc/_search \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{"query":
    {"bool":
        {"must": [
            {"match":{"book":"col"} },
            {"match":{"text":"beware"} }

        ]
        }
    },
    "sort":{ "number": "ASC"},
    "_source":["text", "book"],
    "size":176
}'

curl   --silent -X POST \
  http://localhost:9200/kjvonly/_doc/_search \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  -d '{"query":
    {"bool":
        {"must": [
            {"match":{"book":"col"} },
            {"match":{"text": "beware"} }
        ],        
        }
    },

    "sort":{ "number": "ASC"},
    "_source":["text", "book"],
    "size":176
}'
```