# 有限体 GF(p^n) for 🐍

これは Python で有限体を使用するためのライブラリです。GF(p) や GF(p^n) の生成、元の四則演算を行うことができます。

## 想定環境

- Python 3.8 ~

## 機能

- GF(p) や GF(p^n) の作成
- 有限体の元を生成 (剰余演算より)
- 生成された元の有限体上での四則演算
- 任意の元の逆元を取得

## 使い方

### インストール方法

`pip` コマンドからインストールできます:

```bash
$ pip install git+https://github.com/syakoo/galois-field
```

### 使用例

#### GF(11)

```python
from galois_field import GFp

# GF(11) の作成
gf = GFp(11)

# 元を作成
el1 = gf.elm(5)  # 5 (mod 11)
el2 = gf.elm(13) # 2 (mod 11)

# 演算
el1 + el2 # 7 (mod 11)
el1 - el2 # 3 (mod 11)
el1 * el2 # 10 (mod 11)
el1 / el2 # 8 (mod 11)

# 逆元
el1.inverse() # 9 (mod 11)
el2.inverse() # 6 (mod 11)
```

#### GF(5^4)

モニックな既約多項式を用います。(今回は x^4 + 2)

```python
from galois_field import GFpn

# GF(5^4) の作成
gf = GFpn(5, [1, 0, 0, 0, 2])

# 元を作成
el1 = gf.elm([1, 2])  # 1x + 2
el2 = gf.elm([1, 2, 3, 4, 5]) # 2x^3 + 3x^2 + 4x + 3

# 演算
el1 + el2 # 2x^3 + 3x^2
el1 - el2 # 3x^3 + 2x^2 + 2x + 4
el1 * el2 # 2x^3 + 1x + 2
el1 / el2 # 3x^3 + 4x^2

# 逆元
el1.inverse() # 3x^3 + 4x^2 + 2x + 1
el2.inverse() # 1x^3 + 1x^2 + 2x + 1
```

### 注意点

- 値の範囲が `2^64 bit` まで、積が正しい値を取得できるのを保証しているのは最大で `2^32 bit` で、10 進数で 10 桁までの演算が可能です。
- 範囲内の値を用いていたとしても、確実に値は保証されているものではないためご注意ください。(こちらは責任をとりません)

## コントリビュートするには

このライブラリは追加したい機能が多く、コントリビューターを募集しています。`Issues` や `PullRequest` を気軽にお願いします。

### 開発用の環境構築

以下のコマンドで開発用の環境を構築してください:

#### 仮想環境 `.venv` の作成 & 起動

```bash
$ python -m venv .venv
$ source .venv/bin/activate
```

#### 依存関係のインストール

```bash
$ pip install -r requirements.dev.txt
```

#### テスト

```bash
$ pytest
```

#### フォーマット確認

```bash
$ flake8 galois_field
```

## ライセンス

MIT LICENSE
