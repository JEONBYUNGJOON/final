# 데이터 : model
# 모델을 다루는 클래스 : Data Access Object(DAO, 다오)
board_list=[]
bno = 1
# 추가(save), 전체출력(findall), 하나출력(findone), 변경(update), 삭제(delete)
# 글 : 글번호, 제목, 내용, 닉네임, 조회수

def save(title:str, content:str, nickname:str)->bool:
  global bno
  b = dict(bno=bno,title=title,content=content,nickname=nickname,readcnt=0)
  board_list.append(b)
  bno+=1
  return True

def findall():
  return board_list

# findone, update, delete는 일단 찾는다
# findone은 글을 찾아서 출력한다. 따라서 조회수도 증가해야 한다
def findone(bno:int)->dict:
  for board in board_list:
    if board['bno']==bno:
      board['readcnt']+=1
      return board
  return None

# 변경은 찾아서 제목과 내용을 바꾼다
def update(bno:int, title:str, content:str)->bool:
  for board in board_list:
    if board['bno']==bno:
      board['title'] = title
      board['content'] = content
      return True
  return False

# 삭제
def delete(bno:int)->bool:
  for board in board_list:
    if board['bno']==bno:
      board_list.remove(board)
      return True
  return False