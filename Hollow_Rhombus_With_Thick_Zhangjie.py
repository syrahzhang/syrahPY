while 1:
	a = int(input("请输入一个小于80的正奇数："))
	if (0 < a < 80) and (a % 2 == 1):
		b = int(input("请输入图形的厚度："))
		s = str(input("请输入符号："))
		m = int((a-1)/2)

		#上半部分
		x = m
		y = 1
		for i in range(0,b):
			print(" "*x,end="")
			print(s*y,end="")
			print()
			x -= 1
			y += 2

		x = m-b
		y = 1
		for j in range(0,m-b+1):
			print(" "*x,end="")
			print(s*b,end="")
			print(" "*y,end="")
			print(s*b,end="")
			print()
			x -= 1
			y += 2


		#下半部分
		x = 1
		y = (a - 2 - 2 *b)
		for i in range(0,m-b):
			print(" "*x,end="")
			print(s*b,end="")
			print(" "*y,end="")
			print(s*b,end="")
			print()
			x += 1
			y -= 2

		x = (m - b + 1)
		y = (2 * b - 1)
		for i in range(0,b):
			print(" "*x,end="")
			print(s*y,end="")
			print()
			x += 1
			y -= 2
		break

	elif (a % 2 == 0) and 0 < a < 80:
		print("您输入的数字不是奇数，请重新输入！")

	elif (a <= 0):
		print("您输入的数字不是正数，请重新输入！")

	else:
		print("您输入的数字不小于80，请重新输入！")