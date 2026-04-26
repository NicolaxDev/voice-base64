# 🎤 Speech-to-Text CLI with Base64 Output

This project is a simple Python tool that captures audio from your microphone, converts speech to text, prints the result to the console, and saves it both as plain text and Base64-encoded text.

## 🚀 Features

* Lists available microphone devices
* Lets you select the input device
* Converts speech to text using Google Speech Recognition
* Saves output in:

  * `transcription.txt` (plain text)
  * `transcription64.txt` (Base64 encoded)
* Runs continuously until you press `q`

---

## ▶️ Usage

1. Run the script:

```bash
python main.py
```

2. You will see a list of available audio devices:

```
Available devices:
0: Microphone 1
1: Microphone 2
...
```

3. Enter the index of the microphone you want to use.

4. The program will start listening and transcribing automatically.

5. Press `q` at any time to exit.

---

## 📁 Output Files

* **transcription.txt**
  Stores recognized speech as plain text.

* **transcription64.txt**
  Stores the same content encoded in Base64.

---

## 🧠 How It Works

* Uses `speech_recognition` to capture and process audio
* Sends audio to Google Speech Recognition for transcription
* Encodes the result using Python’s `base64` module
* Uses `keyboard` to detect the exit key (`q`)

---

## ⚠️ Notes

* Requires an active internet connection (Google Speech API)
* Accuracy may vary depending on audio quality and background noise
* The `keyboard` library may require administrator privileges on some systems

---

## 📄 License

This project is open for use, modification, and distribution.

Contributions are welcome! If you have improvements, fixes, or ideas, feel free to open an issue or submit a pull request.

---

## 🙌 Author

Built as a lightweight speech recognition utility in Python.
