"""
django haystack 规定,要在某个APP下进行检索,就要在这里创建search_indexes.py文件
在里面定义一个 XXIndex 类（XX 为含有被检索数据的模型),并且继承 SearchIndex 和 Indexable类
"""


from haystack import indexes
from .models import BookMark


class BookMarkIndex(indexes.SearchIndex, indexes.Indexable):
    text = indexes.CharField(document=True, use_template=True)

    def get_model(self):
        return BookMark

    def index_queryset(self, using=None):
        return self.get_model().objects.all()
