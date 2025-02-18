import streamlit as st
from backend import generate_image
import io

st.title("AI image generator")
st.write("Enter prompt and AI will generate you an Image")

prompt = st.text_input("Enter your prompt: ","Create an image of baby Elephant")

if st.button("Generate Image"):
    try:
        with st.spinner("Generating image.......Please wait!"):
            image = generate_image(prompt)
            st.image(image, caption="Generated Image", use_container_width=True)

            img_bytes = io.BytesIO()
            image.save(img_bytes, "PNG")
            img_bytes = img_bytes.getvalue()

            st.download_button(label="Download Image",  data= img_bytes, file_name= "generated_img.png")
    except Exception as e:
        st.error(f"Error: {e}")

