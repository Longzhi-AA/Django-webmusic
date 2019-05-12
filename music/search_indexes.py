# from haystack import indexes
#
# from music.models import Music_info
#
# class MusicinfIndex(indexes.SearchIndex,indexes.Indexable):
#     text = indexes.CharField(document=True,use_template=True)
#
#     def get_model(self):
#         return  Music_info
#
#     def index_queryset(self, using=None):
#         return self.get_model().objects.all()