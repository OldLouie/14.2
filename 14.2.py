import sqlite3

# Подключаемся к базе данных (или создаем её)
conn = sqlite3.connect('not_telegram.db')

# Создаем объект курсора
cursor = conn.cursor()

# Создаем таблицу Users, если она ещё не создана (можно закомментировать, если таблица уже создана)
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

# Заполняем таблицу 10 записями (можно закомментировать, если данные уже есть)
users_data = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000)
]

# Удаляем все данные из таблицы перед заполнением (если необходимо)
# cursor.execute('DELETE FROM Users')

# Вставляем данные только если таблица пуста
if cursor.execute('SELECT COUNT(*) FROM Users').fetchone()[0] == 0:
    cursor.executemany('INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)', users_data)

# Удаляем запись с id=6
cursor.execute('DELETE FROM Users WHERE id = ?', (6,))

# Подсчитываем общее количество записей
cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]

# Подсчитываем сумму всех балансов
cursor.execute('SELECT SUM(balance) FROM Users')
all_balances = cursor.fetchone()[0]

# Вычисляем средний баланс
average_balance = all_balances / total_users if total_users > 0 else 0

# Выводим средний баланс в консоль
print(average_balance)

# Сохраняем изменения и закрываем соединение
conn.commit()
conn.close()