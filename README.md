```
# Note need all.json and booknames.json from kjvdata repo
python parse.py > test-ndjosn.json

curl -X PUT \
  http://localhost:9200/kjvonly/ \
  -H 'Cache-Control: no-cache' \
  -H 'Content-Type: application/json' \
  --data-binary @mapping.json

curl -X GET   http://localhost:9200/kjvonly/_doc/gen_1_1   -H 'Cache-Control: no-cache'

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
            {"match":{"book":"col"} }
        ]
        }
    },
    "sort":{ "number": "ASC"},
    "_source":["text", "book"],
    "size":176
}'
```