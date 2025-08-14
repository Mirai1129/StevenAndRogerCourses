def drinks_machine():
    """
    我們今天要到販賣機買飲料
    我們身上有 20 塊

    販賣機有三種飲料
    奶茶 20 塊
    紅茶 25 塊

    我們要投錢，我們想買綠茶，試著讓販賣機知道能不能買
    """
    money = int(input("請輸入您身上的錢: "))

    milk_tea_price = 20
    black_tea_price = 25

    if money < milk_tea_price and money < black_tea_price:
        print("無法購買奶茶或紅茶")
    elif money >= max(black_tea_price, milk_tea_price):
        print("可以購買紅茶或奶茶")
    elif money >= milk_tea_price:
        print("可以購買奶茶")
    elif money >= black_tea_price:
        print("可以購買紅茶")
        

def fruit_selection():
    fruit = input("請輸入水果: ")
    if fruit == "蘋果":
        print("你選擇了蘋果")
    elif fruit == "香蕉":
        print("你選擇了香蕉")
    elif fruit == "橘子":
        print("你選擇了橘子")
    else:
        print(f"未知的水果 {fruit}")

def sum_of_list(nums: list[int]) -> int:
    sum_result = 0
    for i in range(len(nums)):
        sum_result += nums[i]
        
    return sum_result


scores = [80, 90, 70, 65, 0, 95]

sum_score_of_class = sum_of_list(scores)

print(f"班級總分: {sum_score_of_class}")
