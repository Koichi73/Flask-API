# Flask-API
flaskを用いた簡単なAPIです。在庫の登録や確認を行います。

## Function
### 1. 在庫の登録
JSONにて`name`と`amount`を登録

```bash
curl -X POST -H "Content-Type: application/json" -d '{"name" : "hoge" , "amount" : 5}' http://3.112.60.110/v1/stocks/
```

※nameは8文字以下のアルファベット<br>
※amountは正の整数

### 2. 在庫の確認
#### 2-1. 全ての在庫
```bash
curl http://3.112.60.110/v1/stocks/
```

#### 2-2. 特定の名前の在庫
```bash
curl http://3.112.60.110/v1/stocks/<確認したい在庫の名前>
```

### 3. 在庫の全削除
```bash
curl -X DELETE http://3.112.60.110/v1/stocks/
```