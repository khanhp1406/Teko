from django_elasticsearch_dsl import Document,Text
from django_elasticsearch_dsl.registries import registry
from elasticsearch_dsl import Index
from book.models import Book
from elasticsearch_dsl import  analyzer
from elasticsearch import Elasticsearch

es = Elasticsearch()
folding_analyzer = analyzer('folding_analyzer',
                           tokenizer="standard",
                           filter=["lowercase", "asciifolding"]
                           )
@registry.register_document
class BookDocument(Document):
    name = Text
    class Index:
        # Name of the Elasticsearch index
        name = 'books'
        using = es
        # See Elasticsearch Indices API reference for available settings
        settings = {'number_of_shards': 1,
                    'number_of_replicas': 0,}

    class Django:
        model = Book # The model associated with this Document

        # The fields of the model you want to be indexed in Elasticsearch
        fields = [
            'id_tiki',
            'name',
            'category',
            'short_description',
            'price',
            'discount',
            'thumnail',
        ]
BookDocument.init()