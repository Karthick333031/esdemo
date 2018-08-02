#######################################################
# ES Demo App
#######################################################

from flask import Flask
from flask import Flask, render_template, json, request
import requests
from elasticsearch import Elasticsearch, RequestsHttpConnection
from flask_table import Table, Col

# Declare your table
class ItemTable(Table):
    package_id = Col('package_id')
    package_desc = Col('package_desc')
    package_name = Col('package_name')

app = Flask(__name__)
es = Elasticsearch('http://127.0.0.1:9200/')



@app.route("/")
def main():
    return render_template('home.html')


@app.route("/search")
def search():
    searchword = request.args.get('s', '')
    print(searchword)
    filterword = request.args.get('f', '')
    dsl = {"query": {"bool": {"should": [{"query_string":{"query": "*" + searchword + "*"}}]
        # ,"filter": { "terms":  { "package_name": filterword }
        }}}
        
    res = es.search(index="test", doc_type="sample", body=dsl)
    out = []
    for itm in res['hits']['hits']:
        out.append(itm['_source'])
    outtbl = ItemTable(out)
    return render_template('result.html',tables=[outtbl.__html__()], titles = ['package_id', 'package_desc', 'package_name'])
    #print(outtbl.__html__())
    #return outtbl.__html__()


if __name__ == "__main__":
    app.run(debug=True)    
