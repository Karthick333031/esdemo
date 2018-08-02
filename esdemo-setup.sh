#! /bin/bash
#######################################################
# ES Demo Setup - PreReq
#######################################################

docker pull docker.elastic.co/elasticsearch/elasticsearch:6.3.2
docker run -d -p 9200:9200 -p 9300:9300 -e "discovery.type=single-node" docker.elastic.co/elasticsearch/elasticsearch:6.3.2
sleep 5
curl -H 'Content-Type: application/json' -XPOST 'http://127.0.01:9200/test/sample' -d "{\"package_id\":\"abc123\",\"package_name\":\"test package 1\",\"package_desc\":\"This is first test package\"}"
curl -H 'Content-Type: application/json' -XPOST 'http://127.0.01:9200/test/sample' -d "{\"package_id\":\"abc456\",\"package_name\":\"test package 2\",\"package_desc\":\"This is second test package\"}"
mkvirtualenv esdemo
pip install flask
pip install flask_table
pip install elasticsearch
pip install requests
workon esdemo
