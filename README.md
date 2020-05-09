# csv-masher
CSVファイルの生成が非常に面倒なので、  
エクセルファイルから自動でCSVを生成するツールです。  
未来的にはPyPIでインストール後、コマンドラインで対応も予定してます。  

# 使い方
## exe版
csv-masher.exeを変換したいエクセルの所にコピー。  
ダブルクリックで実行するととcsvが生成されます。  
csvを生成する等の環境はノーコ ーディング環境が多いので、  
そのまま渡せる様にするイメージです。

releaseからzipファイルをダウンロード、解凍してお使いください。  
https://github.com/InTack2/csv-masher/releases


## python版
pythonを実行できる方は下記に記載します。

### 1.Pipenvをpythonに導入する
まずはPipenvをインストールしてください。  
Pipenvが対応するpythonバージョンと対象パッケージをダウンロードするので、  
バージョンはどれでもOKです。  

### 2.pythonのバージョン、パッケージ環境を構築する
下記をコマンドプロンプトで入力してください。  
PipfileとPipfile.lockを元に仮想環境を構築します。
```
cd "このプロジェクトのcloneしたパス"
pipenv install
```

### 3.実行
下記の様に実行して完了です。  
```python
pipenv shell # 仮想環境に入る
python -m main.py
# main.pyと同じ場所にある.xlsxファイルのCSVが生成される
```

### tips:exe化
Pyinstallerでexe化しておりますが、  
pipenvのコマンドを設定する事で短い文で実行する事ができます。  
```pipfile
[scripts]
build = "Pyinstaller src/csv-masher/main.py --onefile --noconsole --clean  -n csv-masher"
```
こうすることで下記のコマンドのみでbuildできます。  
成功すると「build」と「dist」というフォルダが生成され、  
distの中にcsv-masher.exeがビルドされています。  
```
pipenv run build
```