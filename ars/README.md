# Sistema ARS

## Etapas - commits

- Apresentação da estrutura de arquivos e diretórios (commit inicial)
- Autenticação
- Cadastro de usuários
- Cadastro de Unidades


## Estrutura de pastas e arquivos projeto

```
.
├── ars
│   ├── asgi.py
│   ├── core
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── forms.py
│   │   ├── __init__.py
│   │   ├── migrations
│   │   │   └── __init__.py
│   │   ├── models.py
│   │   ├── static
│   │   │   └── css
│   │   │       └── stylesheet.css
│   │   ├── templates
│   │   │   ├── base.html
│   │   │   └── core
│   │   │       └── index.html
│   │   ├── tests
│   │   │   └── __init__.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── manage.py
├── README.md
├── requirements-dev.txt
├── requirements.txt
└── runtime.txt
```


## Funcionalidades
- Autenticação
- Cadastro de usuários
- Cadastro de Unidades


## Requisitos do negócio

### Cadastro de usuários

- Campos: nome, sobrenome, email, senha, confirmação de senha (ainda estou avaliando se haverá um campo tipo)
- Cadastro feito pelo Administrador
- Tipos: Administrador, Auditor, visitante, fornecedor, funcionário (gerente, analista, assistente, etc.)

### Autenticação

- após cadastro do cliente, o mesmo recebe os dados de acesso por email
- login com email e senha
- login, logout, troca de senha, reset de senha (esqueci a senha)

### Cadastro de Unidades


### Requisitos do projeto

- versão do python (pode ser a mais recente - 3.10.5 ?)
- versão do django (pode ser a mais recente - 4.0.5 ?)
- Vamos usar HTMX, certo?
