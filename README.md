# Integral Calculator

O **Integral Calculator** é um sistema simples e funcional que calcula a integral definida de duas funções matemáticas: \(x^2\) e \(\sin(x)\). Ele utiliza uma interface web intuitiva para facilitar a interação com os usuários.

---

## 🧮 Funcionalidades

- Calcula a integral definida da função \(x^2\).
- Calcula a integral definida da função \(\sin(x)\).
- Retorna um gráfico da função selecionada com a área correspondente à integral calculada.

---

## 🛠️ Tecnologias Utilizadas

- **Python**: para a lógica de cálculo e backend.
- **Flask**: para criar e gerenciar a aplicação web.
- **HTML e CSS**: para desenvolver a interface do usuário.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos

Certifique-se de ter instalado em sua máquina:

- Python 3.9 ou superior
- pip (gerenciador de pacotes do Python)

### Passo a Passo

1. Clone este repositório:

   ```bash
   git clone https://github.com/mateusnriiy/integral-calculator.git
   ```

2. Navegue até o diretório do projeto:

   ```bash
   cd integral-calculator
   ```

3. Crie e ative um ambiente virtual (opcional, mas recomendado):

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Linux/Mac
   venv\Scripts\activate     # Para Windows
   ```

4. Instale as dependências necessárias:

   ```bash
   pip install -r requirements.txt
   ```

5. Inicie o servidor Flask:

   ```bash
   python app.py
   ```

---

## 📂 Estrutura do Projeto

```plaintext
integral-calculator/
├── app.py                # Arquivo principal da aplicação Flask
├── templates/            # Arquivos HTML para as páginas da aplicação
├── static/               # Arquivos CSS e outros recursos estáticos
└── README.md             # Documentação do repositório
```

---

## 📈 Exemplos de Uso

1. Insira os limites de integração no formulário da interface.
2. Escolha uma das funções disponíveis (\(x^2\) ou \(\sin(x)\)).
3. Clique em "Calcular" para visualizar o resultado numérico e o gráfico.