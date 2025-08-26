import sqlite3

conexao = sqlite3.connect('bi_class.db')
cursor = conexao.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS customers (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    estado CHAR(2),
    dt_cadastro DATE NOT NULL
);

CREATE TABLE IF NOT EXISTS orders (
    id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    dt_pedido DATE NOT NULL,
    status TEXT,
    valor_total REAL NOT NULL,
    FOREIGN KEY(customer_id) REFERENCES customers(id)
);
''')

cursor.executemany('''
INSERT INTO customers (id, nome, estado, dt_cadastro)
VALUES (?, ?, ?, ?)
''', [
    (1, 'Ana', 'SP', '2024-01-05'),
    (2, 'Bruno', 'RJ', '2024-02-10'),
    (3, 'Carla', 'MG', '2024-02-15'),
    (4, 'Diego', 'SP', '2024-03-01'),
    (5, 'Eva', 'PR', '2024-04-01')
])

cursor.executemany('''
INSERT INTO orders (id, customer_id, dt_pedido, status, valor_total)
VALUES (?, ?, ?, ?, ?)
''', [
    (101, 1, '2025-03-10', 'paid', 700.00),
    (102, 1, '2025-06-05', 'paid', 450.00),
    (103, 2, '2025-01-20', 'paid', 300.00),
    (104, 2, '2025-07-15', 'paid', 600.00),
    (105, 3, '2025-03-12', 'paid', 200.00),
    (106, 3, '2025-05-09', 'paid', 300.00),
    (107, 3, '2025-08-01', 'paid', 1200.00),
    (108, 4, '2024-12-30', 'paid', 900.00),
    (109, 4, '2025-02-25', 'paid', 510.00),
    (110, 5, '2025-04-14', 'paid', 200.00),
    (111, 5, '2025-04-30', 'paid', 220.00),
    (112, 5, '2025-05-12', 'paid', 260.00)
])

conexao.commit()
conexao.close()

print("Banco criado e dados inseridos com sucesso!")
