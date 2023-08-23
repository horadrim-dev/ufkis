from haystack import indexes
from .models import Organization


class OrganizationIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)
    name = indexes.CharField(model_attr='name', null=True)
    short_name = indexes.CharField(model_attr='short_name', null=True)
    # short_description = indexes.CharField(model_attr='short_description', null=True)
    # description = indexes.CharField(model_attr='description', null=True)

    def get_model(self):
        return Organization
