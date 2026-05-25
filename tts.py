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
