import streamlit as st

# Configure the page
st.set_page_config(
    page_title="מצפינים",
    page_icon="",
    layout="centered"
)

# Main title
st.image("images/logo2.png")
#st.title("בואו לצפון")
#st.image("images/logo2.png")
# Subtitle
#st.subheader("בואו לצפון")


#------------

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

#-----
st.divider()

# Navigation menu title
st.markdown(
    """
    <h2 style="text-align: center; direction: rtl;">
        לאן תרצו להמשיך?
    </h2>
    """,
    unsafe_allow_html=True
)

# Right-to-left text inside page links
st.markdown(
    """
    <style>
    [data-testid="stPageLink"] a {
        direction: rtl !important;
        text-align: right !important;
        justify-content: center !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Center the navigation links
left, center, right = st.columns([1, 2, 1])

with center:
    st.page_link(
        "pages/restaurants.py",
        label="מסעדות ועגלות קפה",
        use_container_width=True
    )

    st.page_link(
        "pages/volunteering.py",
        label="התנדבויות",
        use_container_width=True
    )

    st.page_link(
        "pages/trips.py",
        label="טיולים ומצפים",
        use_container_width=True
    )
