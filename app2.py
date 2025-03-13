import streamlit as st

# Set page title and favicon
st.set_page_config(page_title="My Second App", page_icon="🚀")

# Custom CSS for styling
st.markdown("""
    <style>
        .main-header {
            font-size: 32px;
            font-weight: bold;
            text-align: center;
            margin-bottom: 20px;
        }
        .content {
            text-align: center;
            font-size: 18px;
        }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='main-header'>Welcome to My Second App</div>", unsafe_allow_html=True)

# Main Content
st.markdown("<div class='content'>This is another Streamlit app with a different page.</div>", unsafe_allow_html=True)

# Add an input field
user_input = st.text_input("Enter something:")
st.write("You entered:", user_input)

# Add a button
if st.button("Click Me"):
    st.success("Button Clicked! 🎉")
