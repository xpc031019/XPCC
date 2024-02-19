from flask import Flask，request，render_template

app=Flask（——name——）

@app.route（“/”，methods=[“GET","POST"])
def index（）:
return（render_template（“index.html”))

if——name——==“——main——”：
app.run（）
