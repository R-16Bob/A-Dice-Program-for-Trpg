#这是一个骰子程序     
#可以输入骰子面数和次数。    by R-16Bob
#  更新v2.01 增加命令功能,修改D100有0的错误
# v2.02 增加提示符
import time
import random

def help():
	print("---------------------------------------------------") 
	print("t- roll a D100")
	print("m- jump to main program")
	print("h- You now are using this function")
	print("e- exit this program")
	
def ten():
	print("Rolling...")	
	time.sleep(1)
	d100=random.randint(1,100)
	print(d100)
	
def main():
	again='y'
	while(again=='y'):
		print("Enter number of faces:")
		face=int(input(prompt))                      ##输入骰子面数
		print("Enter number of Dice:")
		number=int(input(prompt))                   ##输入骰子个数
		print("------------------------------------------------")
		for i in range(number):
			print("Rolling...")
			time.sleep(1)
			result=random.randint(1,face)
			print(result)
		print("roll again?(y or n)")
		again=input(prompt)

def menu():
	print("This is a Dice program by R-16Bob")
	print("Enter 'h'for help if you first use .")
	while(1):
		command=input(prompt)
		if(command=='h'):
			help()
		if(command=='t'):
			ten()
		if(command=='m'):
			main()
		if(command=='e'):
			break 
		
			
prompt = ">>"
menu() 			
