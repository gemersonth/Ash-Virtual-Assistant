# Ash - Assistente Virtual

Ash é um assistente virtual desenvolvido com **Python**, criado como projeto de aprendizado. Ele utiliza **reconhecimento de voz offline**, possui função de fala (speaker) e pode ser expandido com um simples **banco de comandos** em `.json` ou `.txt` para executar funções específicas.

---

## 🔹 Bibliotecas Usadas

- `SpeechRecognition`
- `Vosk`
- `PyAudio`
- `os`
- `sys`
- `pyttsx3`
- `json`

---

## 🔹 Modelo de Reconhecimento de Voz

Para o reconhecimento de voz funcionar, é necessário o modelo **vosk_model_br** (Português do Brasil).  
Você pode usar outro modelo em outra língua, mas para PT-BR recomendamos esse modelo.

---

## 🔹 Instalação de Dependências

Execute o comando abaixo para instalar todas as dependências do projeto:


    python3 -m pip install -r requirements.txt
