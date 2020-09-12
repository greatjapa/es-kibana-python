import elasticsearch
import time
from elasticsearch.helpers import bulk

def index_batch(index, docs=[], retries=1):
    client = elasticsearch.Elasticsearch(f"http://localhost:9200",sniff_on_start=False,max_retries=1,timeout=5)

    actions=[]
    for doc in docs:
        action={
            "_op_type": "index",
            "_index": index,
            "_type": index,
            "_id": doc['documentId']
        }
        actions.append({**doc, **action})

    try:
        indexed = bulk(client,actions=actions,refresh=True)
        print(f"Indexed on elasticsearch {len(actions)} documents (index: {index})")
        return True
    except Exception as e:
        print("Elasticsearch fail")
        print(f"Exception: {e}")

        if retries < 5:
            time.sleep(1)
            print("Elasticsearch: Will retry index")
            return index_batch(index, docs=docs, retries=retries+1)
        else:
            print("Elasticsearch error on index")
            print(f"Exception {e}")
            return False