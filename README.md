# csv-masher
Tool to generate csv in batch.

CSVファイルの生成が非常に面倒なので、  
エクセルファイルから自動でCSVを生成するツールです。  
未来的にはPyPIでインストール後、コマンドラインで対応も予定してます。  

# 使い方
## ・exe版
csv-masher.exeを変換したいエクセルの所にコピー。  
ダブルクリックで実行するととcsvが生成されます。  
csvを生成する等の環境はノーコーディング環境が多いので、  
そのまま渡せる様にするイメージです。


## ・python版
pythonを実行できる方は下記に記載します。

### 1.Pipenvをpythonに導入する
まずはPipenvをインストールしてください。  
Pipenvが対応するpythonバージョンと対象パッケージをダウンロードするので、  
バージョンはどれでもOKです。  

### 2.pythonのバージョン、パッケージ環境を構築する
下記でOKです。  
これでPipfileとPipfile.lockを元に仮想環境を構築します。
```
cd "このプロジェクトのcloneしたパス"
pipenv install
```

### 3.実行
後は下記の様に実行して完了です。  
```python
pipenv shell # 仮想環境に入る
python -m main.py
# main.pyと同じ場所にある.xlsxファイルのCSVが生成される
```

## exe化
Pyinstallerでexe化しています。  
下記のコマンドを打つ事でbuildできます。  
pipenv便利。  
```
pipenv run build
```