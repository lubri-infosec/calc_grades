import random
import os 

def menu():
    print("Программа Василия Бегичева!")
    print("[1] Ввод данных")
    print("[2] Генерация случайных данных")
    print("[3] Загрузка данных из data.txt")
    print("[4] Выполнение задания")
    print("[5] Вывод результата на экран")
    print("[6] Сохранение результата в results.txt")
    print("[0] Выход")

def avg_grades(grades):
    if not grades:
        return 0.0
    
    return sum(grades) // len(grades)

def convert(grade):
    if grade >= 85:
        return 5
    elif grade >= 70:
        return 4
    elif grade >= 55:
        return 3
    else:
        return 2
    
def pass_exam(grade, pass_score = 50):
    return grade >= pass_score

def calculation(grades):
    if not grades:
        return None
    
    avg_100 = avg_grades(grades)
    avg_5 = convert(avg_100)
    pass_status = [pass_exam(g) for g in grades]
    return {
        "Средняя 100 балльная" : avg_100,
        "Средняя 5 балльная": avg_5,
        "Всего значений": len(grades),
        "Количество сданных экзаменов": pass_status.count(True),
        "Количество провальных экзаменов": pass_status.count(False)
    }

def random_grade(count = 10):
    return [random.randint(0,100) for rg in range(count)]

def load_file(filename = "data.txt"):
    grades = []
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(BASE_DIR, filename)
    try:
        with open(full_path, "r",encoding="utf-8") as f:
            for line in f:
                clean_line = line.strip()
                if clean_line.isdigit():
                    grades.append(int(clean_line))
    except FileNotFoundError:
        print(f"Откладка, файл искался здесь {full_path}")
    return grades

def save_file(results,filename = "result.txt"):
    if not results:
        return
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(BASE_DIR, filename)
    
    with open(full_path, "w", encoding="utf-8") as f:
        f.write("Результаты:")
        f.write(f"Средняя 100 балльная: {results['Средняя 100 балльная']}\n")
        f.write(f"Средняя 5 балльная: {results['Средняя 5 балльная']}\n")
        f.write(f"Всего оценок обработано: {results['Всего значений']}\n")
        f.write(f"Количество сдавших экзамен: {results['Количество сданных экзаменов']}\n")
        f.write(f"Количество не сдавших экзамен: {results['Количество провальных экзаменов']}\n")

def print_res(results):
    if not results:
        print("\nОшибка! Результатов нет, выполните 4 пункт")
        return
    print("Результаты расчетов:")
    print(f"Количество оценок: {results['Всего значений']}")
    print(f"Средний балл: {results['Средняя 100 балльная']:.2f} (Оценка: {results['Средняя 5 балльная']})")
    print(f"Сдали: {results['Количество сданных экзаменов']} человек / Не сдали: {results['Количество провальных экзаменов']} человек")


    
