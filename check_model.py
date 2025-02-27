import google.generativeai as genai

API_KEY = "AIzaSyATGkJSFBhy-p5_E45oSSOPs8cwvSPJ3aE"  
genai.configure(api_key=API_KEY)

try:
    models = genai.list_models()
    print("Available Models:")
    for model in models:
        print(f"- {model.name}")
except Exception as e:
    print(f"Error: {e}")