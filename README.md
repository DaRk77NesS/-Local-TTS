# 🎙️ Interactive Multilingual Text-to-Speech (TTS) Dashboard

An elegant, zero-configuration Text-to-Speech (TTS) engine built directly for Jupyter Notebooks and interactive Python environments. This application provides an intuitive UI dashboard allowing users to dynamically type text, select from multiple global languages, toggle speech speed, and immediately stream or download the synthesized high-quality MP3 audio.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)](https://jupyter.org)

---

## ✨ Features

* **Self-Sustaining Runtime:** Automatically detects, installs, and links missing external dependencies (`gTTS`, `ipywidgets`) right inside your active workspace kernel upon launch.
* **Interactive UI Controls:** Native, responsive `ipywidgets` dashboard layout featuring text inputs, language selection dropdowns, and speed toggle buttons.
* **Multilingual Support:** Seamlessly supports 10 global languages out of the box with built-in flags for visual clarity.
* **Instant Audio Playback:** Renders a native browser audio player within the workspace for immediate, high-fidelity testing.
* **Direct-to-Local Export:** Dynamically injects a beautiful HTML button to instantly download your generated MP3 directly to your computer.

---

## 🛠️ Supported Languages & Locales

| Language | Code | Language | Code |
| :--- | :---: | :--- | :---: |
| 🇺🇸 English (US) | `en` | 🇮🇳 Hindi | `hi` |
| 🇲🇽 Spanish | `es` | 🇸🇦 Arabic | `ar` |
| 🇫🇷 French | `fr` | 🇮🇹 Italian | `it` |
| 🇯🇵 Japanese | `ja` | 🇨🇳 Chinese | `zh-CN` |
| 🇩🇪 German | `de` | 🇧🇷 Portuguese | `pt` |

---

## 🚀 Quick Start & Installation

Because this script includes a **Self-Sustained Runtime Check**, you don't even need to run a manual `pip install` command. The script handles dependencies automatically.

### Prerequisites
Ensure you are running the code inside an interactive environment such as **Jupyter Notebook**, **JupyterLab**, or **VS Code (with Jupyter Extension)**.

### Running the App
1. Create a new notebook cell.
2. Paste the provided Python code.
3. Run the cell. 

---

## 🎯 How To Use

1. **Configure Parameters:** Select your target language from the dropdown menu and set your speech tempo rate (Normal or Slow).
2. **Type your Prompt:** Click inside the text input field box and write your sentence.
3. **Generate:** Press `ENTER` on your keyboard.
4. **Listen & Save:** Listen to the live audio playback render instantly or click the **Download MP3 File** button to save it locally.

---

## ⚙️ How It Works Behind the Scenes
```text
[User Text Input] + [Language Selection]
                │
                ▼
      [Google TTS Engine] ──(Processes Frames)──> [Generates .mp3 File]
                                                         │
                                        ┌────────────────┴────────────────┐
                                        ▼                                 ▼
                             [IPython HTML Audio]               [Custom Action Component]
                             (Instant UI Playback)              (Download Button Triggers)


