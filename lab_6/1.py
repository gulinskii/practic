import xml.etree.ElementTree as ET


def load_users_data(file="users.xml"):
    try:
        root = ET.parse(file).getroot()
        return [
            {
                "user_id": int(i.find("user_id").text),
                "name": i.find("name").text,
                "age": int(i.find("age").text),
                "weight": int(i.find("weight").text),
                "fitness_level": i.find("fitness_level").text
            }
            for i in root.findall("user")
        ]
    except FileNotFoundError:
        print("Файл users.xml не найден")
        return []

def load_workouts_data(file="workouts.xml"):
    try:
        root = ET.parse(file).getroot()
        return [
            {
                "workout_id": int(i.find("workout_id").text),
                "user_id": int(i.find("user_id").text),
                "date": i.find("date").text,
                "type": i.find("type").text,
                "duration": int(i.find("duration").text),
                "distance": float(i.find("distance").text),
                "calories": int(i.find("calories").text),
                "avg_heart_rate": int(i.find("avg_heart_rate").text),
                "intensity": i.find("intensity").text
            }
            for i in root.findall("workout")
        ]
    except FileNotFoundError:
        print("Файл workouts.xml не найден")
        return []

def get_stats(users, workouts):
    print("ОБЩАЯ СТАТИСТИКА")
    print("===========================")
    print(f"Всего тренировок: {len(workouts)}")
    print(f"Всего пользователей: {len(users)}")
    print(f"Сожжено калорий: {sum(w['calories'] for w in workouts)}")
    print(f"Общее время: {sum(w['duration'] for w in workouts) / 60:.1f} часов")
    print(f"Пройдено дистанции: {sum(w['distance'] for w in workouts):.1f} км")
    print()

users = load_users_data()
workouts = load_workouts_data()
get_stats(users, workouts)
