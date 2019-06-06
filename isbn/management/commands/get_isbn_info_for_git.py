from django.core.management.base import BaseCommand
from isbn.models import Book, SearchWord
from datetime import datetime
import requests
import urllib.request
import urllib.parse
import json 

class Command(BaseCommand):

    """ カスタムコマンド定義 """

    def handle(self, *args, **options):
        # ここに実行したい処理を書く
        print("Djangoカスタムコマンドのテストです。")

        word_list =[]
        queryset = SearchWord.objects.all().filter(flag=True)
        for item in queryset:
            word_list.append(item.word)
       
        print(word_list)

        for word in word_list:
            #検索ワードに登録されているワードの書籍情報を検索
            API = "https://app.rakuten.co.jp/services/api/BooksBook/Search/20170404"
            APPLICATION_ID = "XXXXXXXXX"
            values = {
                "applicationId": APPLICATION_ID,
                "format": "json",  # 出力形式
                "title": word
            }
            #パラメータのエンコード処理        
            params = urllib.parse.urlencode(values)
            # リクエスト用のURLを生成 
            url = API + "?" + params
            #リクエストを投げる。
            req = requests.get(url)
            # json形式で取得
            data = json.loads(req.text)

            for i in range(len(data['Items'])):
                if not Book.objects.filter(isbn=data['Items'][i]['Item']['isbn']).exists():
                    #年月日を日付型に変換
                    if "日" not in data['Items'][i]['Item']['salesDate']:
                        salesDate = data['Items'][i]['Item']['salesDate'] + "01日"
                        salesDate = salesDate.replace('年','/').replace('月','/').replace('日','')
                        salesDate = datetime.strptime(salesDate, '%Y/%m/%d')
                    else:
                        salesDate = data['Items'][i]['Item']['salesDate'].replace('年','/').replace('月','/').replace('日','')
                        salesDate = datetime.strptime(salesDate, '%Y/%m/%d')
           
                    #新規登録
                    isbn_data = Book.objects.create(
                        word = SearchWord.objects.get(word=word),
                        isbn = data['Items'][i]['Item']['isbn'],
                        salesDate = salesDate,
                        title = data['Items'][i]['Item']['title'],
                        itemPrice = data['Items'][i]['Item']['itemPrice'],
                        imageUrl = data['Items'][i]['Item']['mediumImageUrl'],
                        reviewAverage = data['Items'][i]['Item']['reviewAverage'],
                        reviewCount = data['Items'][i]['Item']['reviewCount'],
                        itemUrl = data['Items'][i]['Item']['itemUrl'],
                        )            