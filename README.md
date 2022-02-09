# todolist_api

## set up
### 安裝 pipenv
```
pip install pipenv
```
### 安裝 dependencies 並開啟虛擬環境
```
pipenv install
pipenv shell
```
### 新建 .env 檔並輸入以下內容
```
JWT_SECRET_KEY = '隨便填寫，越亂越好'
MONGODB_SETTINGS = {
    'host': 'mongodb://...'
}
```
### 設定 ENV_FILE_LOCATION
```
export ENV_FILE_LOCATION=./.env
```
### 執行 run.py
```
python run.py
```

## testing
### 新建 .env.test 檔並輸入以下內容
```
JWT_SECRET_KEY = '隨便填寫，越亂越好'
MONGODB_SETTINGS = {
    'host': 'mongodb://... 和正式使用不同 database'
}
```
### 設定 ENV_FILE_LOCATION
```
export ENV_FILE_LOCATION=./.env.test
```
### 執行測試
```
python -m unittest tests/*.py
```
