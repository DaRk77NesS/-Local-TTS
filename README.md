# 🎙️ Interactive Multilingual Text-to-Speech (TTS) Dashboard

An elegant, zero-configuration Text-to-Speech (TTS) engine built directly for Jupyter Notebooks and interactive Python environments. This application provides an intuitive UI dashboard allowing users to dynamically type text, select from multiple global languages, toggle speech speed, and immediately stream or download the synthesized high-quality MP3 audio.

[![Python Version](https://img.shields.io/badge/python-3.7+-blue.svg?style=for-the-badge&logo=python)](https://www.python.org)
[![Jupyter](https://img.shields.io/badge/Jupyter-Notebook-orange?style=for-the-badge&logo=jupyter)](https://jupyter.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg?style=for-the-badge)](https://opensource.org/licenses/MIT)

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

## 💻 Code Usage

```python
import sys
import os
import subprocess

# ==============================================================================
# SELF-SUSTAINED RUNTIME DEPENDENCY CHECK
# ==============================================================================
print("="*20, "INITIALIZING SYSTEM ENVIRONMENTS", "="*20)
required_packages = {
    "gtts": "gTTS",
    "ipywidgets": "ipywidgets"
}

for import_name, pip_name in required_packages.items():
    try:
        __import__(import_name)
    except ImportError:
        print(f"Dependency '{pip_name}' missing. Injecting directly into active workspace kernel...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", pip_name, "--quiet"])
        print(f"✓ {pip_name} successfully linked.")

# Explicitly import verified modules
from gtts import gTTS
import ipywidgets as widgets
from IPython.display import Audio, display, clear_output, HTML

# ==============================================================================
# UI COMPONENTS SETUP
# ==============================================================================
language_options = {
    "🇺🇸 English (US)": "en",
    "🇲🇽 Spanish": "es",
    "🇫🇷 French": "fr",
    "🇯🇵 Japanese": "ja",
    "🇩🇪 German": "de",
    "🇮🇳 Hindi": "hi",
    "🇸🇦 Arabic": "ar",
    "🇮🇹 Italian": "it",
    "🇨🇳 Chinese": "zh-CN",
    "🇧🇷 Portuguese": "pt"
}

text_input = widgets.Text(
    value='',
    placeholder='Type your prompt here...',
    description='Text Input:',
    layout=widgets.Layout(width='50%')
)

language_dropdown = widgets.Dropdown(
    options=language_options,
    value='en',
    description='Language:',
    layout=widgets.Layout(width='25%')
)

speed_toggle = widgets.RadioButtons(
    options=[('Normal 🏃', False), ('Slow 🐢', True)],
    value=False,
    description='Speed:',
    layout=widgets.Layout(width='20%')
)

ui_layout = widgets.HBox([text_input, language_dropdown, speed_toggle])

# ==============================================================================
# CORE AUDIO INFERENCE AND EXPORT ENGINE
# ==============================================================================
def process_and_export_voice(sender):
    user_text = text_input.value.strip()
    selected_lang = language_dropdown.value
    is_slow = speed_toggle.value
    
    if not user_text:
        return
        
    clear_output(wait=True)
    display(ui_layout) 
    
    print(f"\nProcessing audio frames on CPU...")
    
    try:
        # Generate the voice model array
        tts = gTTS(text=user_text, lang=selected_lang, slow=is_slow)
        output_file = "downloadable_speech.mp3"
        tts.save(output_file)
        
        print("✓ Synthesis complete!")
        print("="*60)
        
        # 1. Render the native Jupyter playback player
        display(Audio(output_file, autoplay=True))
        
        # 2. Inject a clean HTML browser link snippet to trigger a browser download element
        download_html = f'''
        <div style="margin-top: 15px;">
            <a href="{output_file}" download="ai_generated_speech.mp3" 
               style="background-color: #4CAF50; color: white; padding: 10px 20px; 
                      text-decoration: none; font-weight: bold; border-radius: 5px; 
                      display: inline-block; box-shadow: 2px 2px 5px rgba(0,0,0,0.2);">
                📥 Download MP3 File to Computer
            </a>
        </div>
        '''
        display(HTML(download_html))
        
    except Exception as e:
        print(f"\n❌ Execution failure: {e}")

# Bind submission key hook listener
text_input.on_submit(process_and_export_voice)

# Clean launch screen view
clear_output()
print("="*20, "ADVANCED MULTILINGUAL VOICE DASHBOARD", "="*20)
print("Adjust settings, enter your message, and hit ENTER:\n")
display(ui_layout)

```


## 🎯 How To Use

1. **Configure Parameters:** Select your target language from the dropdown menu and set your speech tempo rate (Normal or Slow).
2. **Type your Prompt:** Click inside the text input field box and write your sentence.
3. **Generate:** Press `ENTER` on your keyboard.
4. **Listen & Save:** Listen to the live audio playback render instantly or click the **Download MP3 File** button to save it locally.

---

## ⚙️ How It Works Behind the Scenes
[User Text Input] + [Language Selection]
                │
                ▼
      [Google TTS Engine] ──(Processes Frames)──> [Generates .mp3 File]
                                                         │
                                        ┌────────────────┴────────────────┐
                                        ▼                                 ▼
                             [IPython HTML Audio]               [Custom Action Component]
                             (Instant UI Playback)              (Download Button Triggers)




