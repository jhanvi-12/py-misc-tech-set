# Elasticsearch Guide

## Overview
Elasticsearch is a distributed, RESTful search and analytics engine designed for horizontal scalability, reliability, and easy management. This guide provides instructions for setting up Elasticsearch and basic usage.

 
## Prerequisites
* [![ElasticSearch][elasticsearch]][ElasticSearch-url]

## Table of content
1. [Installation](#installation)
2. [ElasticSearch](#elasticsearch)
2. [Connection](#connection)
3. [Indexing](#indexing)
4. [Mapping](#mapping)

## Usage

Once Elasticsearch is installed and running, you can perform various operations such as indexing documents, searching, aggregations, and more using the Elasticsearch RESTful API.

## Installation
You can install fastapi, awswrangler and opensearch-py using pip:

```bash
pip install fastapi
pip install awswrangler
pip install opensearch-py
```

## ElasticSearch
## What is an Elastic search ?
- Imagine you have a huge pile of documents, like articles, emails, or tweets, and you need to find specific information in them quickly. That's where Elasticsearch comes in handy!

- Think of Elasticsearch as a super-fast, super-smart librarian for your pile of documents. It's like having a librarian who knows exactly where each word is in every document and can fetch the exact ones you need in the blink of an eye.

## What is an index in Elasticsearch?
#### 1. Indexing: 
- In Elasticsearch, an index is like a database in traditional relational databases. It's a collection of documents that have somewhat similar characteristics. Each document in an index is a JSON object, and Elasticsearch indexes these documents in a way that makes them searchable.

- Imagine you have a collection of books. You could organize them into different categories like fiction, non-fiction, or science fiction. In Elasticsearch, each category would be like an index, and each book would be a document within that index. This organization makes it easier and faster to search for specific information.

## Connection
Import Required Libraries:
1. Elastic Search class and Connect to Elastic Search.
```python
import awswrangler as wr
from config import elasticsearch_config

class ESearch:
    """The Class will help to connect elastic search and create a object of it to get
    the required information and data from elastic search.
    """
    def __init__(self):
        pass

    def connect_elasticsearch(self):
    """This method establishes a connection to Elasticsearch using the awswrangler library.
    It uses the configuration settings provided (host, username, and password) to connect to the Elasticsearch.
    Returns:
        Return Elasticsearch client details
    """
    client = wr.opensearch.connect(
        host=elasticsearch_config.ELASTIC_SEARCH_HOST,
        username=elasticsearch_config.ELASTIC_SEARCH_USERNAME,
        password=elasticsearch_config.ELASTIC_SEARCH_PASSWORD,
    )
    return client
```

## Indexing
```python
    # 2. Generate Index in Elastic Search
    def generate_index(self, index_name, doc_type, data):
        """This method generates an index in Elasticsearch and populates it with the provided data.

        Args:
            index_name (str): Name of the index to be created.
            doc_type (str): Type of documents to be indexed.
            data (list): List of dictionaries containing the data to be indexed.
        """
        client = self.connect_elasticsearch()
        dictionaries = [
            {
                "_index": index_name,
                "_type": doc_type,
                "_source": doc
            }
            for doc in data
        ]
        data = wr.opensearch.index_documents(
            client,
            documents=dictionaries,
            index=elasticsearch_config.ELASTIC_SEARCH_INDEX
        )
        return data
```

## Document and Fields
- In Elasticsearch, a document is a basic unit of information that can be indexed. 
- It is expressed in JSON format and can contain any number of fields, which are key-value pairs. 
- Fields represent the attributes or properties of the document.

## Mapping
- In Elasticsearch, mapping defines the structure of documents within an index, specifying the fields and their characteristics. It determines how each field is indexed and stored, similar to how a schema defines the structure of a table in a relational database.

- For example:
    - We define a mapping for the books index.
    - We specify properties for each field such as title, author, publication_date, and genre.
    - Each field is assigned a data type (text, date, keyword) based on the nature of the data it holds.

```json
PUT /books
{
  "mappings": {
    "properties": {
      "title": { "type": "text" },
      "author": { "type": "text" },
      "publication_date": { "type": "date" },
      "genre": { "type": "keyword" }
    }
  }
}

```
### Indexing

After defining the mapping, we can index documents into Elasticsearch. Indexing refers to the process of storing documents in an index, making them searchable.
```json
POST /books/_doc/1
{
  "title": "The Great Gatsby",
  "author": "F. Scott Fitzgerald",
  "publication_date": "1925-04-10",
  "genre": "Fiction"
}
```

## ElasticSearch CRUD operations to perform using Index.
- Replace {index_name} with the desired index name which we created using above function.
1. ### Create(Index)
```json
POST /{index_name}/_doc
{
  // Document data
}
```

2. ### Read(Retrieve)
```json
GET /{index_name}/_search
{
  "query": {
    "match": {
      "name": "John"
    }
  }
}

```

3. ### Update
```json
POST /{index_name}/_update_by_query
{
  "query": {
    "match": {
      "name": "John"
    }
  },
  "script": {
    "source": "ctx._source.age += params.increment",
    "params": {
      "increment": 1
    }
  }
}
```

4. ### Delete
```json
POST /{index_name}/_delete_by_query
{
  "query": {
    "match": {
      "name": "John"
    }
  }
}

```

#### Searching: 
    - When you need to find something, you tell Elasticsearch what you're looking for, like a word or a phrase. It then quickly sifts through all the documents in its index and pulls out the ones that match your search.

#### Scoring: 
    - Not all matches are created equal. Elasticsearch also ranks the results based on how closely they match what you're looking for. So, the most relevant documents pop up first, like the best books on a library shelf.

#### Speed: 
    - One of the coolest things about Elasticsearch is how fast it is. It's designed to handle massive amounts of data and return search results almost instantly, even if you have millions of documents to search through.

[ElasticSearch]: https://img.shields.io/badge/-ElasticSearch-005571?style=for-the-badge&logo=elasticsearch
[elasticsearch-url]: https://www.elastic.co/
