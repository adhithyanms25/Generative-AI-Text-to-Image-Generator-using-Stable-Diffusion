import streamlit as st
from diffusers import StableDiffusionPipeline
import torch

# Page Config
st.set_page_config(
    page_title="AI Image Generator",
    page_icon="🎨",
    layout="wide"
)

# Title
st.title("🎨 Generative AI Text-to-Image Generator")
st.markdown(
    "Generate stunning AI images from text prompts using Stable Diffusion."
)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")

    width = st.selectbox(
        "Image Width",
        [512, 768],
        index=0
    )

    height = st.selectbox(
        "Image Height",
        [512, 768],
        index=0
    )

    st.markdown("---")

    st.subheader("💡 Example Prompts")

    st.write("• Futuristic city at sunset")
    st.write("• Astronaut riding a horse")
    st.write("• Cyberpunk Kerala street")
    st.write("• Flying car above ocean")

# Load Model
@st.cache_resource
def load_model():
    pipe = StableDiffusionPipeline.from_pretrained(
        "runwayml/stable-diffusion-v1-5"
    )
    pipe = pipe.to("cpu")
    return pipe

pipe = load_model()

# Prompt Input
prompt = st.text_area(
    "Enter your prompt",
    placeholder="Example: A futuristic city with flying cars and neon lights"
)

# Generate Button
if st.button("🚀 Generate Image"):

    if prompt.strip() == "":
        st.warning("Please enter a prompt.")
    else:

        with st.spinner("Generating image... Please wait ⏳"):

            image = pipe(
                prompt,
                height=height,
                width=width
            ).images[0]

        st.success("Image Generated Successfully!")

        st.image(
            image,
            caption=prompt,
            use_container_width=True
        )

        image.save("generated_image.png")

        with open("generated_image.png", "rb") as file:
            st.download_button(
                label="📥 Download Image",
                data=file,
                file_name="generated_image.png",
                mime="image/png"
            )

# Footer
st.markdown("---")
st.caption(
    "Built using Streamlit, Stable Diffusion, Diffusers and PyTorch"
)