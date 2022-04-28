# Comentário de uma linha só
-- Comentário de uma linha só
/*
	Comentário de
	múltiplas linhas
*/

# Criando uma base de dados
# SQL é case-insensitive
# De preferência sempre colocar ; no final da instrução SQL

# Usando o comando CREATE, criamos bases de dados, tabelas, etc
# Colocando a cláusula IF NOT EXISTS, o banco de dados será criado se não existir. Se existir,
# será mostrada uma mensagem de aviso
CREATE DATABASE IF NOT EXISTS 20220426_aula01;

# Apagamos bases de dados, tabelas, etc
# DROP DATABASE 20220426_aula01;

# Definimos o banco de dados padrão utilizando o comando USE
USE 20220426_aula01;

# tb_users
CREATE TABLE IF NOT EXISTS tb_users(
	id INT NOT NULL, email VARCHAR(200), is_active BOOLEAN
);


# DROP TABLE tb_users;

# Inserindo dados na tabela tb_users
INSERT INTO tb_users(id, email, is_active) VALUES (1000, "john@email.com", true);

# Selecionando os dados da tabela
# O asterisco significa "todas as colunas"
SELECT * FROM tb_users;

# Podemos inserir múltiplos valores de uma vez utilizando INSERT
INSERT INTO tb_users(id, email, is_active) VALUES
(1001, 'joana@mail.com', true),
(1002, 'bete@mail.com', true),
(1003, 'amanda@mail.com', false);

# Com o comando UPDATE atualizamos os dados da tabela
# É sempre importante se atentar a cláusula WHERE. Comandos UPDATE e DELETE vão alterar TODAS as linhas
# da tabela, se não for colocada uma cláusula WHERE
UPDATE tb_users SET is_active = true WHERE email='amanda@mail.com' ;

# Com o comando DELETE, apagamos linhas da tabela
DELETE FROM tb_users WHERE email='amanda@mail.com';

# Chave primária
# Chave primária é uma coluna de uma tabela que serve como identificador único daquele registro(ou daquela linha)
# Ou seja, os valores de uma coluna do tipo chave primária NUNCA se repetem.
# Uma chave primária pode ser composta ou não

/*
 * Chave primária simples
 * id sendo a coluna chave primária
 * 
 * id	email	password
 * 1	john@mail.com	123
 * 2 	maria@mail.com	123
 * 3	joca@mail.com	123
 */

/*
 * Chave primária composta
 * tb_instrutores
 * id	nome
 * 1	alessandro
 * 2	barbara
 * 3	walber
 * 
 * tb_turmas
 * id_turma e id_instrutor sendo chave primária composta
 * id_turma		id_instrutor	nome
 * 1			1				Python
 * 2			1				Java
 * 3			1				CSS
 * 2			2
 * 
 */

# Chave estrangeira
# É uma coluna em uma tabela filha que referencia uma outra coluna na tabela pai

/*
 * tb_users
 * 
 * id é a chave primária da tabela
 * 
 * id	nome
 * 1	bruna
 * 2	jackson
 * 3	zuleide
 * 
 * tb_posts
 * id é a chave primária da tabela
 * id_user é a chave estrangeira da tabela
 * 
 * id	id_user	titulo	corpo
 * 1	3		sd		dfgfdg
 * 2    3       dsfsd   sdgfdg
 * 3    2      sdfsdf   sdfsdf
*/

DROP TABLE tb_users ;

# AUTO_INCREMENT gera um novo id sempre que um registro é inserido
CREATE TABLE IF NOT EXISTS tb_users (
	id INT NOT NULL AUTO_INCREMENT,
	email VARCHAR(200) NOT NULL,
	is_active BOOLEAN DEFAULT true,
	PRIMARY KEY(id)
);

INSERT INTO tb_users (email, is_active) VALUES ('rebecca@mail.com', false);
INSERT INTO tb_users (email) VALUES ('zuleide@mail.com');
INSERT INTO tb_users (id, email) VALUES (5,'maria@mail.com');

SELECT * FROM tb_users tu ;

CREATE TABLE tb_posts (
    id INT NOT NULL AUTO_INCREMENT,
    user_id INT NOT NULL,
    title VARCHAR(100),
    body TEXT,
    PRIMARY KEY(id),
    FOREIGN KEY(user_id) REFERENCES tb_users(id)
);

SELECT * FROM tb_posts;

# O comando abaixo vai falhar, pois não existe na tabela tb_users um usuário de id 100
INSERT INTO tb_posts (user_id, title, body) VALUES (100, "A linguagem Python", "Python é muito legal.");
INSERT INTO tb_posts (user_id, title, body) VALUES (1, "A Linguagem C++", "C++ é muito poderoso, porém complexo.");
INSERT INTO tb_posts (user_id, title, body) VALUES (1, "A Linguagem Haskell", "Haskell é coisa de doido.");
INSERT INTO tb_posts (user_id, title, body) VALUES (6, "CSS", "Eu não sei CSS.");

SELECT * FROM tb_posts;

DELETE FROM tb_users WHERE 
