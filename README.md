学籍番号マークシート(解答用紙)とそのリーダーのサンプル

学籍番号マークシートの作成は以下を参考にTeXで行いました。
* https://unilab.gbb60166.jp/tex/msheet.htm
「METAFONT を利用したマークシート・フォントの作成」

マークシートリーダー以下を参考にしました。
* http://qiita.com/sbtseiji/items/6438ec2bf970d63817b8
「PythonとOpenCVで簡易OMR（マークシートリーダ）を作る」

学籍番号マークシート(解答用紙)は、上のTeXをからpdfを作成、
それのスクリーンショットからPowerPointに貼り付けました。
上記「PythonとOpenCVで簡易OMR（マークシートリーダ）を作る」にあったマーカーを配置し、
マークシートリーダーのソースを調整しました。

こちらの環境は
* macOS Sierra
* python3.5
* OpenCV
* ScanSnap iX500
です。

How to test

まず、サンプルデータが読めるかどうか検討してみる。
* 必要なソフトはMacportsから
<pre>
$ sudo port install opencv +python35
</pre>
でインストールできる。
<pre>
$ python marksheet.py 20170912130856.jpg
</pre>
とすると
<pre>
ln -s 20170912130856.jpg 1_33_010987_X.jpg
</pre>
と、学籍番号をファイル名として出力する。

次に、自分でマークしたものでテストしてみよう。
* answersheet.pdfをカラーまたはグレースケールでプリントする。
* 適当にペンでマークを入れてScanSnap iX500で300dpi、jpegで読み込む
そのファイル名を20171011.jpgとする
<pre>
$ python marksheet.py 20171011.jpg
</pre>
とすると学籍番号をファイル名として出力する。ちゃんと読めるだろうか?

Tips
* 読めなかった場合は"z"、複数マークしていた場合は"y"と出力する。
* マークシートのサイズを変えるとmarksheet.pyの値を変更しなければならない。
その方法について略記する。読み取りの参考になるのは、res.pngである。これは
<pre>
python marksheet.py xxxx.jpg
</pre>
とすると生成される。読み込まれたマークシートはどの部分がわかる。
これがズレている場合は正常に読めない。
例としては20170912130856.jpgを読み取った場合のres.pngを見て欲しい。
このズレを直すには
marksheet.pyの
<pre>
    43      img = img[398:_nrow*100-88,42:ncol*100-1-34]
</pre>
を適宜変更して欲しい。

