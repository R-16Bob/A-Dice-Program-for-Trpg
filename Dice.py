# 这是一个骰子程序
# 可以输入骰子面数和次数。    by R-16Bob
# V3.0 现在可以直接在命令行选择功能了
import time
import random
import argparse

def ten():
    again = 'y'
    while(1):
        print("Rolling...")
        time.sleep(1)
        d100 = random.randint(1, 100)
        print(d100)
        print("roll again?(y or n)")
        again = input(prompt)
        if again!='y':
            break


def main():
    again = 'y'
    while (again == 'y'):
        print("Enter number of faces:")
        face = int(input(prompt))  ##输入骰子面数
        print("Enter number of Dice:")
        number = int(input(prompt))  ##输入骰子个数
        print("------------------------------------------------")
        for i in range(number):
            print("Rolling...")
            time.sleep(1)
            result = random.randint(1, face)
            print(result)
        print("roll again?(y or n)")
        again = input(prompt)


def anko():
    while (True):
        str = input("input: ")
        if str == 'q':
            break
        num = int(str[0])
        face = int(str[2:])

        if num == 1:
            print(f'【{str}={random.randint(1, face)}】')
        else:
            print(f'【{str}=', end='')
            print(f'{random.randint(1, face)}', end='')
            for i in range(num - 1):
                print(', ', end='')
                print(f'{random.randint(1, face)}', end='')
            print('】')


def menu():
    parser = argparse.ArgumentParser()
    parser.add_argument('-d', '--Roll_a_D100', action='store_true', default=False)
    parser.add_argument('-r', '--Roll_a_Dice', action='store_true', default=True, help='Roll a Dice')
    parser.add_argument('-a', '--Anko', action='store_true', default=False, help='Anko mode')

    args = parser.parse_args()  # 解析命令行参数到args变量中

    if args.Roll_a_D100:
        ten()
    elif args.Anko:
        print('input a string, for example,1d6. type q to quit')
        anko()
    elif args.Roll_a_Dice:
        main()
    else:
        parser.print_help()  # 如果没有匹配的参数，则打印帮助信息


if __name__ == "__main__":
    prompt = ">>"
    menu()
