from django.shortcuts import render
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from isbn.models import Book, SearchWord
from . forms import SearchWordForm
from django.urls import reverse_lazy


class BookListView(ListView):
    # 利用するモデルを指定
    model = Book
    # データを渡すテンプレートファイルを指定
    template_name = 'isbn/isbn_list.html'
    # Bookテーブルの全データを取得するメソッドを定義
    def queryset(self):
        return Book.objects.all()


class SearchWordCreateView(CreateView):   
    # 利用するモデルを指定
    model = SearchWord
    # 利用するフォームクラス名を指定
    form_class = SearchWordForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('isbn:create_done')


def create_done(request):
    # 登録処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'isbn/create_done.html')


class WordListView(ListView):
    # 利用するモデルを指定
    model = SearchWord
    # データを渡すテンプレートファイルを指定
    template_name = 'isbn/searchword_list.html'

    # 家計簿テーブルの全データを取得するメソッドを定義
    def queryset(self):
        return SearchWord.objects.all()


class WordUpdateView(UpdateView):   
    # 利用するモデルを指定
    model = SearchWord
    # 利用するフォームクラス名を指定
    form_class = SearchWordForm
    # 登録処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('isbn:update_done')

       
def update_done(request):
    # 更新処理が正常終了した場合に呼ばれるテンプレートを指定
    return render(request, 'isbn/update_done.html')


class WordDeleteView(DeleteView):
    #利用するモデルを指定
    model = SearchWord
    #削除処理が正常終了した場合の遷移先を指定
    success_url = reverse_lazy('isbn:delete_done')


def delete_done(request):
    return render(request, 'isbn/delete_done.html')