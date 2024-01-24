import flask as f
import dao
# Create  get/post    
# Read    get  
# Update  get(/read)/post
# Delete  get(/read)/post

# get   html을 보여준다
# post  처리 후 이동한다
app = f.Flask(__name__)

@app.route("/")
def list() :
  board_list = dao.findall()
  return f.render_template("list.html", list=board_list)

@app.route('/write')
def 쓰기화면보여주기():
  return f.render_template("write.html")

@app.route("/write", methods=['post'])
def 쓰기처리():
  return f.redirect("/")

@app.route("/read")
def 읽기():
  bno = f.request.form.get('bno', type=int)
  board = dao.findone(bno)
  return f.render_template("read.html")

# /read에서 내용을 바꾸고 변경버튼 클릭
@app.route("/update", methods=['post'])
def 변경():
  bno = f.request.form.get("bno", type=int)
  title = f.request.form.get("title", type=str)
  content = f.request.form.get("content", type=str)
  dao.update(bno=bno, title=title, content=content)
  return f.redirect("/")

# /read에서 삭제버튼 클릭
@app.route("/delete", methods=['post'])
def 삭제():
  bno = f.request.form.get("bno", type=int)
  dao.delete(bno=bno)
  return f.redirect("/")