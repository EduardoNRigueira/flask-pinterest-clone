# 📌 FakePinterest

Aplicação web inspirada no Pinterest, desenvolvida com Flask, permitindo que usuários criem contas, façam login e compartilhem imagens. Este projeto foi desenvolvido durante um curso da Hashtag Treinamentos.

---

## 🚀 Funcionalidades

- 🔐 Cadastro e login de usuários
- 📸 Upload de imagens
- 📰 Feed com fotos ordenadas por data
- 👤 Página de perfil com fotos do usuário
- 🔒 Senhas criptografadas
- ✅ Validação de formulários

---

## 🛠️ Tecnologias utilizadas

- Python
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-WTF
- Flask-Bcrypt
- HTML / CSS

---

## 📂 Estrutura do projeto
flask-pinterest-clone/
│── main.py
│── FakePinterest/
│ ├── init.py
│ ├── routes.py
│ ├── models.py
│ ├── forms.py
│ ├──static/
| │ ├── css/
│ │ ├── fotos_post/
│ │ └── fotos_site/
│── templates/

---

## ▶️ Como executar o projeto

```bash
# Clone o repositório
git clone https://github.com/seu-usuario/fakepinterest.git

# Acesse a pasta
cd fakepinterest

# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente
venv\Scripts\activate

# Instale as dependências
pip install -r requirements.txt

# Execute o projeto
python main.py