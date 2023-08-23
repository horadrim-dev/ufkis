from haystack.backends.elasticsearch7_backend import FIELD_MAPPINGS, \
    DEFAULT_FIELD_MAPPING, Elasticsearch7SearchBackend, Elasticsearch7SearchEngine

from haystack.constants import DJANGO_CT, DJANGO_ID

# https://silentsokolov.github.io/django-haystack-elasticsearch-prombiemy-avtodopolnieniia


FIELD_MAPPINGS['edge_ngram'] = {'type': 'string', 'index_analyzer': 'edgengram_analyzer', 'search_analyzer': 'standard'}


class ElasticsearchCustomBackend(Elasticsearch7SearchBackend):
    DEFAULT_SETTINGS = {
        'settings': {
            "analysis": {
                "analyzer": {
                    "default": {
                    #  добавляем удаление html тегов 
                    "char_filter": ["html_strip"],
                    "tokenizer":  "standard",
                    "filter": [
                        "lowercase",
                        "ru_stop",
                        "ru_stemmer"
                    ]
                    }
                },
                "filter": {
                    "ru_stop": {
                    "type":       "stop",
                    "stopwords":  "_russian_"
                    },
                    "ru_stemmer": {
                    "type":       "stemmer",
                    "language":   "russian"
                    }
                }
                # "analyzer": {
                #     "russian": {
                #         "tokenizer":  "standard",
                #         "filter": [
                #             "lowercase",
                #             "russian_stop",
                #             "russian_keywords",
                #             "russian_stemmer"
                #         ]
                #     },
                #     # "ngram_analyzer": {
                #     #     "type": "custom",
                #     #     "tokenizer": "lowercase",
                #     #     "filter": ["haystack_ngram"]
                #     # },
                #     # "edgengram_analyzer": {
                #     #     "type": "custom",
                #     #     "tokenizer": "lowercase",
                #     #     "filter": ["haystack_edgengram"]
                #     # },
                #     # 'russian_and_english': {
                #     #     'type': 'custom',
                #     #     'tokenizer': 'standard',
                #     #     "filter": ['lowercase', 'russian_morphology', 'english_morphology', 'ru_stopwords'],
                #     # }
                # },
                # "tokenizer": {
                #     "haystack_ngram_tokenizer": {
                #         "type": "ngram",
                #         "min_gram": 3,
                #         "max_gram": 15,
                #     },
                #     "haystack_edgengram_tokenizer": {
                #         "type": "edge_ngram",
                #         "min_gram": 2,
                #         "max_gram": 15,
                #         "side": "front"
                #     }
                # },
                # # "filter": {
                # #     "haystack_ngram": {
                # #         "type": "ngram",
                # #         "min_gram": 3,
                # #         "max_gram": 15
                # #     },
                # #     "haystack_edgengram": {
                # #         "type": "edge_ngram",
                # #         "min_gram": 2,
                # #         "max_gram": 15
                # #     },
                # #     'ru_stopwords': {
                # #         'type': 'stop',
                # #         'stopwords': u'а,без,более,бы,был,была,были,было,быть,в,вам,вас,весь,во,вот,все,всего,всех,вы,где,да,даже,для,до,его,ее,если,есть,еще,же,за,здесь,и,из,или,им,их,к,как,ко,когда,кто,ли,либо,мне,может,мы,на,надо,наш,не,него,нее,нет,ни,них,но,ну,о,об,однако,он,она,они,оно,от,очень,по,под,при,с,со,так,также,такой,там,те,тем,то,того,тоже,той,только,том,ты,у,уже,хотя,чего,чей,чем,что,чтобы,чье,чья,эта,эти,это,я,a,an,and,are,as,at,be,but,by,for,if,in,into,is,it,no,not,of,on,or,such,that,the,their,then,there,these,they,this,to,was,will,with',
                # #     },
                # #     'ru_stemming': {
                # #         'type': 'snowball',
                # #         'language': 'Russian',
                # #     }
                # # }
                # "filter": {
                #     "russian_stop": {
                #     "type":       "stop",
                #     "stopwords":  "_russian_"
                #     },
                #     "russian_keywords": {
                #     "type":       "keyword_marker",
                #     "keywords":   []
                #     },
                #     "russian_stemmer": {
                #     "type":       "stemmer",
                #     "language":   "russian"
                #     }
                # }
            }
        }
    }

    def build_schema(self, fields):
        content_field_name = ''
        mapping = {
            DJANGO_CT: {'type': 'string', 'index': 'not_analyzed', 'include_in_all': False},
            DJANGO_ID: {'type': 'string', 'index': 'not_analyzed', 'include_in_all': False},
        }

        for field_name, field_class in fields.items():
            field_mapping = FIELD_MAPPINGS.get(field_class.field_type, DEFAULT_FIELD_MAPPING).copy()
            if field_class.boost != 1.0:
                field_mapping['boost'] = field_class.boost

            if field_class.document is True:
                content_field_name = field_class.index_fieldname

            # Do this last to override `text` fields.
            if field_mapping['type'] == 'string':
                if field_class.indexed is False or hasattr(field_class, 'facet_for'):
                    field_mapping['index'] = 'not_analyzed'
                    del field_mapping['analyzer']

            mapping[field_class.index_fieldname] = field_mapping

        return (content_field_name, mapping)


class ElasticsearchCustomSearchEngine(Elasticsearch7SearchEngine):
    backend = ElasticsearchCustomBackend
