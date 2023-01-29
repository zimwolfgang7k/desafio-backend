# Cnab Parser

#### Cnab parser é uma aplicação que transpila um código CNAB para um banco de dados, organizando assim todos os dados.

#### Sua principal funcionalidade é organizar todos os dados passados no código CNAB para um banco de dados e também renderizar todos esses dados em uma outra página.

# Tecnologias utilizadas:

- Python
- Django

# Passos para instalação:

1. Crie seu ambiente virtual:

   ````
   python -m venv venv

   ou

   python3 -m venv venv```
   ````

2. Ative o venv:

   ```
   # linux:

   source venv/bin/activate

   #windows:

   .\venv\Scripts\activate
   ```

3. Instale as dependências:
   ```
   pip install -r requirements.txt
   ```
4. Rode as migrações:

   ```
   python manage.py migrate
   ```

5. Rode a aplicação com o comando:
   ```
   python manage.py runserver
   ```
