import sqlite3

# Функция для создания структуры БД
def create_database():
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Создание таблицы для клиентов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS clients (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            first_name TEXT NOT NULL,
            last_name TEXT NOT NULL,
            email TEXT UNIQUE
        )
    ''')

    # Создание таблицы для телефонов
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS phones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            client_id INTEGER NOT NULL,
            phone TEXT UNIQUE,
            FOREIGN KEY (client_id) REFERENCES clients (id) ON DELETE CASCADE
        )
    ''')

    conn.commit()
    conn.close()

# Функция для добавления нового клиента
def add_client(first_name, last_name, email, phones=None):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    # Добавление клиента
    cursor.execute('''
        INSERT INTO clients (first_name, last_name, email)
        VALUES (?, ?, ?)
    ''', (first_name, last_name, email))

    client_id = cursor.lastrowid

    # Добавление телефонов, если они указаны
    if phones:
        for phone in phones:
            cursor.execute('''
                INSERT INTO phones (client_id, phone)
                VALUES (?, ?)
            ''', (client_id, phone))

    conn.commit()
    conn.close()

# Функция для добавления телефона для существующего клиента
def add_phone(client_id, phone):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO phones (client_id, phone)
        VALUES (?, ?)
    ''', (client_id, phone))

    conn.commit()
    conn.close()

# Функция для изменения данных о клиенте
def update_client(client_id, first_name=None, last_name=None, email=None):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    if first_name:
        cursor.execute('''
            UPDATE clients
            SET first_name = ?
            WHERE id = ?
        ''', (first_name, client_id))

    if last_name:
        cursor.execute('''
            UPDATE clients
            SET last_name = ?
            WHERE id = ?
        ''', (last_name, client_id))

    if email:
        cursor.execute('''
            UPDATE clients
            SET email = ?
            WHERE id = ?
        ''', (email, client_id))

    conn.commit()
    conn.close()

# Функция для удаления телефона для существующего клиента
def delete_phone(phone):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM phones
        WHERE phone = ?
    ''', (phone,))

    conn.commit()
    conn.close()

# Функция для удаления существующего клиента
def delete_client(client_id):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        DELETE FROM clients
        WHERE id = ?
    ''', (client_id,))

    conn.commit()
    conn.close()

# Функция для поиска клиента по данным
def find_client(search_term):
    conn = sqlite3.connect('clients.db')
    cursor = conn.cursor()

    cursor.execute('''
        SELECT c.id, c.first_name, c.last_name, c.email, p.phone
        FROM clients c
        LEFT JOIN phones p ON c.id = p.client_id
        WHERE c.first_name LIKE ? OR c.last_name LIKE ? OR c.email LIKE ? OR p.phone LIKE ?
    ''', (f'%{search_term}%', f'%{search_term}%', f'%{search_term}%', f'%{search_term}%'))

    results = cursor.fetchall()
    conn.close()
    return results

# Демонстрация работы функций
if __name__ == '__main__':
    # Создание структуры БД
    create_database()

    # Добавление клиентов
    add_client('Иван', 'Иванов', 'ivan@example.com', ['1234567890'])
    add_client('Петр', 'Петров', 'petr@example.com', ['9876543210', '5555555555'])

    # Добавление телефона для существующего клиента
    add_phone(1, '9999999999')

    # Изменение данных о клиенте
    update_client(1, first_name='Иван', last_name='Сидоров')

    # Поиск клиента
    print("Найдены клиенты:")
    for row in find_client('Иван'):
        print(row)

    # Удаление телефона
    delete_phone('5555555555')

    # Удаление клиента
    delete_client(2)

    # Поиск клиента после удаления
    print("Найдены клиенты после удаления:")
    for row in find_client('Петр'):
        print(row)