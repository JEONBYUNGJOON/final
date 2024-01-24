import flask as f
import dao
app = f.Flask(__name__)

@app.route("/")
def 목록():
  result = dao.findall()
  return f.render_template("list.html", list=result)

# /read?bno=1 또는 /read?bno=2
@app.route("/read")
def 읽기():
  bno = f.request.args.get("bno", type=int)
  board = dao.findone(bno)
  return f.render_template("read.html", board=board)

@app.route("/write")
def 쓰기_화면():
  return f.render_template("write.html")

@app.route("/write", methods=['post'])
def 쓰기():
  title = f.request.form.get("title", type=str)
  content = f.request.form.get("content", type=str)
  nickname = f.request.form.get("nickname", type=str)
  dao.save(title=title, content=content, nickname=nickname)
  return f.redirect("/")

app.run(debug=True)