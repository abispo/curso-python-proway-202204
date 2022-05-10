# Curso Django

### Criar um novo projeto
``django-admin startproject <nome_do_projeto> .``

O ponto no final serve pra gerarmos o projeto definindo como diretório raiz o diretório atual. Se não colocarmos o ponto, será criada uma pasta com o nome do projeto, e dentro dela será o diretório raiz da aplicação.

### Criar um novo app
`python manage.py startapp <nome_do_app>`

### Rodar o projeto
`python manage.py runserver`

### Registrar o app no `settings.py`
Adicionar a linha `<nome_do_app>.apps.<NomeDoApp>` em `INSTALLED_APPS`

### Gerar uma nova migration
`python manage.py makemigrations <nome_do_app>`

### Aplicar a(s) migration(s) gerada(s)
`python manage.py migrate`
