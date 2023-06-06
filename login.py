from flask import Flask, request

app = Flask(__name__)

@app.route('/login', methods=['POST'])
def login():
    # 從請求中獲取使用者名稱和密碼
    username = request.form.get('username')
    password = request.form.get('password')

    # 在此處執行身份驗證邏輯，例如檢查使用者名稱和密碼是否正確

    # 處理登入邏輯
    if username == 'admin' and password == 'password':
        # 登入成功的處理
        return '登入成功'
    else:
        # 登入失敗的處理
        return '登入失敗'

if __name__ == '__main__':
    app.run()
