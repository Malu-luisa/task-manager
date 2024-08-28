import sqlite3

# Conexão com o banco de dados
def connect_db():
    conn = sqlite3.connect('tasks.db')
    return conn

# Criação da tabela de tarefas
def create_table():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS tasks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            status TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Adicionar uma nova tarefa
def add_task(title, description, status='Not Started'):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('INSERT INTO tasks (title, description, status) VALUES (?, ?, ?)',
                   (title, description, status))
    conn.commit()
    conn.close()

# Obter todas as tarefas
def get_tasks():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM tasks')
    tasks = cursor.fetchall()
    conn.close()
    return tasks

# Atualizar uma tarefa existente
def update_task(task_id, title, description, status):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE tasks
        SET title = ?, description = ?, status = ?
        WHERE id = ?
    ''', (title, description, status, task_id))
    conn.commit()
    conn.close()

# Remover uma tarefa
def delete_task(task_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM tasks WHERE id = ?', (task_id,))
    conn.commit()
    conn.close()

# Adicionar nova tarefa (interface do usuário)
def add_new_task():
    title = input("Digite o título da tarefa: ")
    description = input("Digite a descrição da tarefa: ")
    add_task(title, description)
    print("Tarefa adicionada com sucesso!")

# Listar todas as tarefas (interface do usuário)
def list_tasks():
    tasks = get_tasks()
    for task in tasks:
        print(f"ID: {task[0]}, Título: {task[1]}, Descrição: {task[2]}, Status: {task[3]}")

# Editar uma tarefa (interface do usuário)
def edit_task():
    task_id = int(input("Digite o ID da tarefa que deseja editar: "))
    title = input("Novo título: ")
    description = input("Nova descrição: ")
    status = input("Novo status: ")
    update_task(task_id, title, description, status)
    print("Tarefa atualizada com sucesso!")

# Remover uma tarefa (interface do usuário)
def remove_task():
    task_id = int(input("Digite o ID da tarefa que deseja remover: "))
    delete_task(task_id)
    print("Tarefa removida com sucesso!")

# Menu principal
def menu():
    print("Sistema de Gerenciamento de Tarefas")
    print("1. Adicionar nova tarefa")
    print("2. Listar todas as tarefas")
    print("3. Editar uma tarefa")
    print("4. Remover uma tarefa")
    print("5. Sair")

if __name__ == "__main__":
    create_table()

    while True:
        menu()
        choice = input("Escolha uma opção: ")

        if choice == '1':
            add_new_task()
        elif choice == '2':
            list_tasks()
        elif choice == '3':
            edit_task()
        elif choice == '4':
            remove_task()
        elif choice == '5':
            print("Saindo...")
            break
        else:
            print("Opção inválida. Tente novamente.")
