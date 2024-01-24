board_list = []
print("1111111111111111111")
board_list.append(dict(bno=1,title="aa",content="aaa",nickname='spring',readcnt=0))
board_list.append(dict(bno=2,title="bb",content="bbb",nickname='spring',readcnt=0))
board_list.append(dict(bno=3,title="cc",content="ccc",nickname='spring',readcnt=0))
print(board_list)
bno = 4

def save(title:str, content:str, nickname:str)->bool:
  global bno
  b = dict(bno=bno,title=title,content=content,nickname=nickname,readcnt=0)
  board_list.append(b)
  bno+=1
  return True

def findall()->list:
  print(board_list)
  return board_list

def findone(bno:int)->dict:
  for board in board_list:
    if board['bno']==bno:
      return board
  return None