password = 'a123456'
i = 3
while  i > 0 :
	pwd = input ('密碼多少')
	if pwd == password :
		print ('密碼正確 ，登入成功')
		break
	else : 
		i = i - 1
		if i > 0 :
			print ('登入失敗，還有' , i , '機會')

		
		









