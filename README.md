# 🎨 Generative AI Text-to-Image Generator

## Overview

This project is a Generative AI application that converts natural language prompts into high-quality images using Stable Diffusion. The application provides an interactive Streamlit-based user interface where users can enter text descriptions and generate AI-created images in real time.

The project demonstrates practical implementation of diffusion models, prompt engineering, and AI-powered image synthesis.

---

## Features

* 🎨 Text-to-image generation using Stable Diffusion
* 🖥️ Interactive Streamlit web interface
* ⚙️ Customizable image dimensions
* 📥 Download generated images
* ⏳ Real-time image generation with loading indicators
* 💡 Example prompts for inspiration
* 🔄 Cached model loading for improved performance

---

## Technologies Used

* Python
* Streamlit
* Stable Diffusion
* Hugging Face Diffusers
* PyTorch
* Transformers
* Pillow

---

## Project Structure

```text
Generative-AI-Text-to-Image-Generator/

├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── generated_images/
├── screenshots/
│   ├── home.png
│   ├── prompt.png
│   └── result.png
└── sample_prompts.txt
```

---

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/adhithyanms25/Generative-AI-Text-to-Image-Generator-using-Stable-Diffusion.git

cd Generative-AI-Text-to-Image-Generator-using-Stable-Diffusion

### 2. Create Virtual Environment

```bash
python -m venv myenv
```

### 3. Activate Virtual Environment

Windows:

```bash
myenv\Scripts\activate
```

Linux/Mac:

```bash
source myenv/bin/activate
```

### 4. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Run the Application

```bash
streamlit run app.py
```

Open your browser and navigate to:

```text
http://localhost:8501
```

---

## How It Works

1. User enters a text prompt.
2. Stable Diffusion processes the prompt.
3. The model generates a corresponding image.
4. The generated image is displayed in the Streamlit interface.
5. Users can download the generated image.

---

## Example Prompts

* A futuristic city with flying cars at sunset
* Astronaut riding a horse on Mars
* Cyberpunk street in Kerala during rain
* Ancient temple floating above the clouds
* Realistic tiger wearing a royal crown

---

## Screenshots

### Home Screen

<img width="1920" height="1008" alt="home" src="https://github.com/user-attachments/assets/d8dd54a2-36d9-4b83-aa5a-e48666f0b35b" />


### Prompt Input

<img width="1920" height="1008" alt="prompt" src="https://github.com/user-attachments/assets/abc78de0-f963-44a6-b033-c9829088afb6" />


### Generated Output

<img width="1920" height="1008" alt="result" src="https://github.com/user-attachments/assets/a978ddfe-0c2c-41bb-a98c-faf9bd603b3d" />


---

## Future Enhancements

* Multiple image generation
* Style selection (Anime, Realistic, Cartoon, Sketch)
* Negative prompt support
* Image-to-image generation
* Cloud deployment
* Prompt history management
* High-resolution image generation

---

## Skills Demonstrated

* Generative AI
* Diffusion Models
* Prompt Engineering
* Python Development
* Streamlit Application Development
* Hugging Face Ecosystem
* Deep Learning Fundamentals

---

## Author

Adhithyan M S

---

## License

This project is intended for educational and learning purposes.
