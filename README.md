
Jogo de sobrevivência desenvolvido em Python com Pygame para projeto acadêmico. Inclui animações de sprites, música e dificuldade progressiva.
Faz todo sentido, Mylena. No GitHub, o README fica muito melhor quando você usa um bloco de código limpo para as instruções. Fica com cara de documentação oficial.

Aqui está o conteúdo completo para você **copiar e colar** no seu arquivo `README.md`. Ele já está formatado com ícones e os blocos de comando que um QA Engineer usaria:

````markdown
# 🏃‍♂️ Run or Jump

Jogo de sobrevivência arcade desenvolvido em **Python** com a biblioteca **Pygame-ce**. O projeto simula um desafio de desviar de obstáculos (bolas de fogo) com dificuldade progressiva.

---

## 🚀 Tecnologias
* **Linguagem:** Python 3.10+
* **Engine:** Pygame-ce
* **Build:** PyInstaller

---

## 🎮 Como Jogar (Download & Run)

Para rodar o projeto localmente, siga os passos abaixo no seu terminal:

1. **Clonar o Repositório:**
   ```bash
   git clone [https://github.com/arieviloanelym/run-or-jump.git](https://github.com/arieviloanelym/run-or-jump.git)
````

2.  **Instalar Dependências:**

    ```bash
    pip install pygame-ce
    ```

3.  **Executar o Jogo:**

    ```bash
    python jogo.py
    ```

### ⌨️ Comandos

  * `ESPAÇO`: Pular / Iniciar / Reiniciar
  * `M`: Mutar/Desmutar Trilha Sonora

-----

## 📦 Gerar Executável (.exe)

Se desejar compilar o jogo para um arquivo executável único:

1.  Instale o PyInstaller:

    ```bash
    pip install pyinstaller
    ```

2.  Gere o build:

    ```bash
    pyinstaller --onefile --noconsole jogo.py
    ```

*Nota: O executável gerado na pasta `/dist` precisa das imagens e do áudio na mesma raiz para funcionar.*

-----

## 📋 Critérios de Aceite (QA Checklist)

  - [x] **Player Control:** Pulo com gravidade simulada.
  - [x] **Desafio:** Spawn aleatório de obstáculos com aumento de velocidade a cada 10s.
  - [x] **Vitória:** Tela de "Demo Completa" ao atingir 30 segundos de sobrevivência.
  - [x] **Derrota:** Detecção de colisão por máscara de pixels (Pixel Perfect).

-----

**Desenvolvido por:** [Mylena Oliveira](https://www.google.com/search?q=https://github.com/arieviloanelym) 👩‍💻

````


