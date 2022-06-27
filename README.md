# projeto-integrador02

Clonar o repositório:
```
git clone https://github.com/abnerjp/projeto-integrador02.git
```

---

## Configurar projeto localmente
### 1. Criar ambiente virtual para o projeto
- #### IDE Pycharm
    ...
### 2. Instalar dependências
- #### Atualizar pip
    ``` 
    python -m pip install --upgrade pip 
    ```


- #### Instalar Django ao projeto
    ```
    pip install django
    ```

- #### Instalar Twilio ao projeto
    ```
    pip install twilio
    ```

### 3. Executar as migrações
- #### Windows
    ```
    python .\manage.py migrate
    ```
- #### Linux
  ```
  python manage.py migrate
  ```

---

## Seção Admin
#### Para acessar a seção de administração do Django, é necessário ter um usuário criado
- #### Windows
    ```
    python .\manage.py createsuperuser
    ```
- #### Linux
    ```
    python manage.py createsuperuser
    ```

---

## Executar a aplicação
- #### Windows
    ```
    python .\manage.py runserver
    ```
- #### Linux
    ```
    python manage.py runserver
    ```