import functions 

def main():
    current_grades = []
    results = None
    while True:
        functions.menu()
        choice = input("\nВаш ответ: ").strip()

        if choice == "1":
            print("Введите оценки от 0 до 100 через пробел:")
            try:
                raw_input = input("> ")
                current_grades = [int(i) for i in raw_input.split() if i.isdigit()]
                print(f"Успешно! Вы ввели {len(current_grades)} оценок")
                results = None
            except ValueError:
                print("Ошибка! Ввод неккоректный, используйте целые числа")

        elif choice == "2":
            current_grades = functions.random_grade()
            print(f"Успешно! Случайные оценки сгенерированы: {current_grades}")
            results = None

        elif choice == "3":
            current_grades = functions.load_file("data.txt")   
            if current_grades:
                print(f"Успешно! Оценки загружены с data.txt: {current_grades}")
            else:
                print("Ошибка! Файл data.txt пуст, оценки не могут быть загружены")
            results = None

        elif choice == "4":
            if not current_grades:
                print("Ошибка! Нет данных для расчета, выполните 1-3 пункты")
            else:
                results = functions.calculation(current_grades)
                print("Успешно! Данные готовы к сохранению")

        elif choice == "5":
            functions.print_res(results)

        elif choice == "6":
            if not results:
                print("Ошибка! Нет результатов для расчетов, выполните 4 пункт")
            else:
                functions.save_file(results,filename = "result.txt")
                print("Успешно! Результаты сохранены в result.txt")
        
        elif choice == "0":
            print("Вы завершили программу, всего доброго!")
            break
        else:
            print("Ошибка в пункте меню! Выберите числа от 1 до 6")

if __name__ == "__main__":
    main()




