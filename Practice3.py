#Practice 06-3 게시판 페이징하기 

def getTotalPage(m,n): #m : 총 건수 n:한 페이지당 보여줄 건수 
	if m % n == 0 :
		return m // n 
	else:
		return m // n + 1 




		