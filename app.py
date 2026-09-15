import streamlit as st

# Configure the page
st.set_page_config(
    page_title="מצפינים",
    page_icon="🌿",
    layout="centered"
)

# Main title
st.title("מצפינים")

# Subtitle
st.subheader("בואו איתנו לצפון")

# Main text
st.markdown(
    """
    <div style="text-align: center; font-size: 20px; line-height: 1.8;">
        אתר מצפינים נועד להביע תמיכה בצפון ולהכיר מקרוב את כל הדברים היפים שיש לו להציע לנו.
        מהנופים המיוחדים והמרהיבים, דרך המסעדות ועגלות הקפה המקומיות,
        ועד לטיולים, מצפים והתנדבויות שמחברות אותנו לאזור ולאנשים שחיים בו.
        <br><br>
        בואו איתנו לגלות את הצפון, לתמוך בעסקים המקומיים וליהנות מכל מה שיש לו להציע.
    </div>
    """,
    unsafe_allow_html=True
)

st.divider()

# Navigation menu
st.header("לאן תרצו להמשיך?")

# st.page_link("pages/1_restaurants.py", label="☕ מסעדות ועגלות קפה")
#
# st.page_link("pages/2_volunteering.py", label="🤝 התנדבויות")
#
# st.page_link("pages/3_trips.py", label="🌄 טיולים ומצפים")