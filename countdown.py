def countdown():
    print("Программа обратного отсчета")
    print("--------------------------")
    
    while True:
        try:
            num = int(input("Введите целое положительное число: "))
            if num <= 0:
                print("Ошибка: число должно быть положительным!")
                continue
                
            print(f"\nОбратный отсчет от {num} до 0:")
            while num >= 0:
                print(num)
                num -= 1
            break
            
        except ValueError:
            print("Ошибка: введите целое число!\n")

if __name__ == "__main__":
    countdown()
