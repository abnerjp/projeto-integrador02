# Intruções para executar projeto localmente

### Obter projeto
- ###### Clonar repositório
    ```
    git clone https://github.com/abnerjp/projeto-integrador02.git
    ```

---

### Configurar projeto
#### 1. Criar ambiente virtual para o projeto
- ###### IDE PyCharm
    
![01-interpreter](https://user-images.githubusercontent.com/45899438/176082334-1a5cc5e0-0f99-4a5a-bccb-b63bdda87b3c.png)

![02-add-interpreter](https://user-images.githubusercontent.com/45899438/176082640-15f10fc3-748b-43e5-9f0a-8e94a08375c5.png)

![03-add-interpreter](https://user-images.githubusercontent.com/45899438/176082612-c7fc6ff5-ecb1-47f2-a3c2-04787e5696be.png)

#### 2. Instalar dependências
- ###### Atualizar pip
    ```
    python -m pip install --upgrade pip 
    ```

- ###### Instalar Django ao projeto
    ```
    pip install django
    ```

- ###### Instalar Twilio ao projeto
    ```
    pip install twilio
    ```

#### 3. Executar as migrações
- ###### Windows
    ```
    python .\manage.py migrate
    ```
- ###### GNU/Linux
  ```
  python manage.py migrate
  ```

---

### Seção Admin
#### Para acessar a seção de administração do Django, é necessário ter um usuário criado
- ###### Windows
    ```
    python .\manage.py createsuperuser
    ```
- ###### GNU/Linux
    ```
    python manage.py createsuperuser
    ```

---

### Executar a aplicação
- ###### Windows
    ```
    python .\manage.py runserver
    ```
- ###### GNU/Linux
    ```
    python manage.py runserver
    ```