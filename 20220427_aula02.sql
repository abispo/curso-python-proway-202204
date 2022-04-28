
-- Aula 20220427

# Modelagem de dados

/*

    Modelagem de dados (Normalização de tabelas)
    Formas normais
    - Normalização de tabelas
    1FN
      - Primeira forma normal
      - Na primeira forma normal garantimos que os dados das colunas são atômicos (indivisíveis)
      - Ou, falando de outra maneira, quando temos um dado multivalorado em uma coluna

    2FN
      - Segunda forma normal
      - Precisa obrigatoriamente estar na 1FN
      - Uma coluna não chave não pode ser dependente apenas de 1 parte da chave primária, deve ser dependente do todo

    3FN
      - Terceira forma normal
      - Precisa obrigatoriamente estar na 2FN
      - E um campo não chave não pode depender de outros campos não chave
          
    

    Tipos de relacionamentos entre tabelas
        1:1, 1:N, N:N
    
    
    CRUD
    Create
        INSERT
    
    Retrieve
        SELECT
    
    Update
        UPDATE
    
    Delete
        DELETE

*/

# Escolhendo a base de dados onde vamos fazer as operações (executar os comandos SQL)
CREATE DATABASE 20220427_aula02;
USE 20220427_aula02;

-- Aplicando a primeira forma normal
-- Sendo a tabela tb_users:
CREATE TABLE IF NOT EXISTS tb_users(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    phones VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

# Inserindo dados dos clientes
INSERT INTO tb_users(name, phones) VALUES
    ("Maria", "11946782391"),
    ("Julia", "11945892019"),
    ("Viviane", "4792361789,4789023845");   # Coluna multivalorada
    
INSERT INTO tb_users(name) VALUES ("Vanessa");

SELECT * FROM tb_users;
# Vamos aplicar a primeira forma normal (1FN)

CREATE TABLE tb_phones(
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,           # Chave estrangeira da tabela tb_users
    phone VARCHAR(20) NOT NULL,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES tb_users(id)
);

SELECT * FROM tb_phones;

INSERT INTO tb_phones (user_id, phone) VALUES
    (1, "11946782391"),
    (2, "11945892019"),
    (3, "4792361789"),
    (3, "4789023845");

SELECT * FROM tb_phones;

############################################################################################################

# Aplicando a segunda forma normal (2FN)

CREATE TABLE IF NOT EXISTS tb_students_projects(
    student_id INT NOT NULL,        # NULL/ NOT NULL indica se uma coluna pode receber valores nulos ou não
    project_id INT NOT NULL,
    student VARCHAR(200) NOT NULL, # aluno
    project VARCHAR(200) NOT NULL, #) NOT NULL,
    PRIMARY KEY(student_id, project_id)
);

INSERT INTO tb_students_projects (student_id, project_id, student, project) VALUES
    (1, 1, "Carla", "EAD"),
    (1, 2, "Carla", "Refinaria"),
    (2, 2, "Vanessa", "Refinaria");

SELECT * FROM tb_students_projects ;

# A linha abaixo não será inserida, pois haverá uma violação de chave primária
INSERT INTO tb_students_projects (student_id, project_id, student, project) VALUES
    (1, 1, "Bruna", "Montadora");

# Aplicando a 2FN (Criar uma nova tabela para cada atributo que depende apenas de um lado da chave primária)

CREATE TABLE tb_students(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO tb_students(name) VALUES
    ("Carla"),
    ("Vanessa"),
    ("Bruna");

SELECT * FROM tb_students ;

CREATE TABLE tb_projects(
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO tb_projects (name) VALUES
    ("EAD"),
    ("Refinaria"),
    ("Montadora");
    
SELECT * FROM tb_projects ;

# Apagando as colunas 
ALTER TABLE tb_students_projects DROP COLUMN student;
ALTER TABLE tb_students_projects DROP COLUMN project;

# DESC mostra uma descrição das colunas de uma tabela
DESC tb_students_projects ;

# Adicionar as chaves estrangeiras
ALTER TABLE tb_students_projects ADD FOREIGN KEY (student_id) REFERENCES tb_students(id);
ALTER TABLE tb_students_projects ADD FOREIGN KEY (project_id) REFERENCES tb_projects(id);

SELECT * FROM tb_students_projects ;

############################################################################################################

# Aplicando a terceira forma normal (3FN)
# DROP TABLE tb_orders
CREATE TABLE tb_orders(
    id INT NOT NULL AUTO_INCREMENT,
    product_id FLOAT NOT NULL,
    price FLOAT NOT NULL,           # Se product_id fosse chave primária, price teria que ser definido em outra tabela
    quantity INT NOT NULL,
    total FLOAT NOT NULL,           # Resultado da multiplicação das colunas price e quantity
    PRIMARY KEY(id)
);
DESC tb_orders;

INSERT INTO tb_orders (product_id, price, quantity, total) VALUES
    (1, 3, 5, 15),
    (2, 2.5, 2, 5),
    (3, 10, 2, 20);
    
SELECT * FROM tb_orders;

# Excluímos a coluna não chave que depende de outras colunas não chave
ALTER TABLE tb_orders DROP COLUMN total;

# "as" significa alias. É o nome que irá aparecer como nome da coluna
SELECT id, product_id as "ID do Produto", price, quantity, price * quantity "Valor total" FROM tb_orders ;

####################################################################################################
# Tipos de relacionamentos

# 3 Tipos de relacionamentos
# 1:1 -> Relacionamento de 1 para 1
# 1:N -> Relacionamento de 1 para muitos
#   Resolvido criando uma chave estrangeira na tabela filha (ou que contém o N)
# users 1: N posts
# N:N -> Relacionamento de muitos para muitos
#  Criamos uma tabela associativa, que irá associar os registros de ambas as tabelas 

CREATE TABLE tb_alunos(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO tb_alunos(nome) VALUES
    ("Amanda"),
    ("Bruna"),
    ("Carla"),
    ("Danielle"),
    ("Elena");

SELECT * FROM tb_alunos;

CREATE TABLE tb_cursos(
    id INT NOT NULL AUTO_INCREMENT,
    nome VARCHAR(200) NOT NULL,
    PRIMARY KEY(id)
);

INSERT INTO tb_cursos(nome) VALUES
    ("Python"),
    ("C#"),
    ("Java"),
    ("Javascript"),
    ("CSS");

SELECT * FROM tb_cursos;

CREATE TABLE tb_turmas(
    id INT NOT NULL AUTO_INCREMENT,
    curso_id INT NOT NULL,
    data_inicio DATE NOT NULL,
    data_fim DATE NULL,
    PRIMARY KEY(id),
    FOREIGN KEY (curso_id) REFERENCES tb_cursos(id)
);

ALTER TABLE tb_turmas ADD COLUMN descricao VARCHAR(200) NOT NULL;

DESC tb_turmas;

INSERT INTO tb_turmas(curso_id, data_inicio, data_fim, descricao) VALUES
    (1, '2022-05-01', '2022-06-01', 'Curso de Python diário (18:15 - 22:15'),
    (1, '2022-06-02', '2022-07-02', 'Curso de Python diário (18:15 - 22:15'),
    (2, '2022-05-01', '2022-06-01', 'Curso de C# diário (18:15 - 22:15'),
    (2, '2022-06-02', '2022-07-02', 'Curso de C# diário (18:15 - 22:15'),
    (5, '2022-05-01', '2022-06-01', 'Curso de CSS diário (18:15 - 22:15');

SELECT * FROM tb_turmas ;

# Selecionando dados de tabelas relacionadas
SELECT c.nome, t.id, tb.data_inicio, t.data_fim
    # c e t são aliases (apelidos) para as tabelas tb_cursos e tb_turmas
    FROM tb_cursos c
    INNER JOIN tb_turmas t ON c.id = t.curso_id;
    
# A relação entre turmas e alunos é de muitos para muitos (N:N)
# Um aluno pode estar matriculado em mais de 1 turma (1:N)
# Uma turma pode conter mais de 1 aluno (1:N)
# Nesse caso, precisamos criar uma tabela associativa, que vai associar um aluno com uma turma, e vice-versa
# Essa tabela associativa será dependente das 2 outroas tabelas


CREATE TABLE tb_turmas_alunos(
    turma_id INT NOT NULL,
    aluno_id INT NOT NULL,
    PRIMARY KEY(turma_id, aluno_id),
    FOREIGN KEY(turma_id) REFERENCES tb_turmas(id),
    FOREIGN KEY(aluno_id) REFERENCES tb_alunos(id)
);
DESC tb_turmas_alunos;

INSERT INTO tb_turmas_alunos(turma_id, aluno_id) VALUES
    (1, 1),
    (1, 2),
    (2, 5),
    (3, 1),
    (3, 2),
    (3, 4),
    (3, 5),
    (4, 2),
    (4, 4),
    (5, 1),
    (5, 2),
    (5, 3),
    (5, 4),
    (5, 5);
    
SELECT * FROM tb_turmas_alunos tta ;

# Selecionar o nome do curso, nome da turma e o nome dos alunos que estão matriculados nas turmas de Python
# tb_cursos c
# tb_alunos a
# tb_turmas t

SELECT t.id, c.nome, a.nome, t.descricao FROM tb_cursos c
    INNER JOIN tb_turmas t
    ON t.curso_id = c.id
    INNER JOIN tb_turmas_alunos tta 
    ON t.id = tta.turma_id 
    INNER JOIN tb_alunos a
    ON tta.aluno_id = a.id
    ORDER BY t.id;
    
    
/*
 * tb_alunos -> tb_turmas_alunos -> tb_turmas
 * 
 */
