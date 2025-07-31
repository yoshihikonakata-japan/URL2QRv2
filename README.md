# URL2QRv2

URL2QRv2 は、URL リストから一括で QR コードを生成し、ベクター形式（SVG、EPS、AI）で出力する Python スクリプトです。出力サイズは 413×413 ピクセルに固定されています。

## 主な特徴

* **一括処理**：テキストファイルに記載した複数の URL をまとめて処理。
* **ベクター出力**：`.svg`、`.eps`、`.ai` の 3 形式を同時生成。
* **固定サイズ**：すべて 413×413 ピクセルに揃えて出力。
* **ファイル名自動生成**：URL の末尾 4 文字（大文字化）＋`_413x413` をファイル名のベースに採用。

## 動作環境

* Python 3.6 以上
* Windows / macOS / Linux

## 依存ライブラリ

```bash
pip install segno reportlab
```

## インストール方法

1. リポジトリをクローンまたはダウンロード

   ```bash
   ```

git clone [https://github.com/](https://github.com/)<あなたのアカウント>/URL2QRv2.git
cd URL2QRv2

````

2. 依存ライブラリをインストール
```bash
pip install segno reportlab
````

## 使い方

```bash
python URL2QRv2.py \
  -i <URL リストファイル> \
  -o <出力ディレクトリ> \
  -e <エラー訂正レベル>
```

* `-i` / `--input` : URL を 1 行ずつ記載したテキストファイル（デフォルト: `C:\pyQR\URL_List_v2\URL_List.txt`）
* `-o` / `--output`: QR コードを出力するディレクトリ（デフォルト: `C:\pyQR\QR_generate_v2`）
* `-e` / `--error-level`: QR コードの誤り訂正レベル（`l`, `m`, `q`, `h` のいずれか。デフォルト: `m`）

例：

```bash
python URL2QRv2.py \
  -i urls.txt \
  -o output_qr \
  -e h
```

## ファイル構成

```
URL2QRv2/            # プロジェクトルート
├─ URL2QRv2.py       # メインスクリプト
├─ README.md          # このファイル
└─ sample_urls.txt    # URL 一覧のサンプル
```

## 出力例

* `ABCD_413x413.svg`
* `ABCD_413x413.eps`
* `ABCD_413x413.ai`

※ `ABCD` は URL の末尾 4 文字を大文字化して使用。

## ライセンス

MIT License
