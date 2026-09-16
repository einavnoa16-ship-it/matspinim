import streamlit as st
from subprocess import check_output

st.markdown(
    """
    <style>
    .stApp {
        background-color: #c8f6f7;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.set_page_config(page_title="מצפינים",layout="centered")

# Main title
st.image("images/logo_real.png")



#text
# st.markdown(
#     """
#     <div style="text-align: center; font-size: 20px; line-height: 1.8;>
#         אתר מצפינים נוצר להביע תמיכה בצפון ולהכיר מקרוב את כל הדברים היפים שיש לו להציע לנו.
#         מהנופים היפים , המסעדות ועגלות הקפה שנמצאות שם ,
#         טיולים, מצפים והתנדבויות שמתאימות לאיזור .
#         <br><br>
#         בואו איתנו לטייל בצפון ,לתמוך בעסקים המקומיים וליהנות .
#     </div>
#     """,
#     unsafe_allow_html=True
# )

#----

st.markdown(
    """
    <div style="text-align: center; direction: rtl;">
         אתר מצפינים נוצר להביע תמיכה בצפון ולהכיר מקרוב את כל הדברים היפים שיש לו להציע לנו.
         מהנופים היפים , המסעדות ועגלות הקפה שנמצאות שם ,
         טיולים, מצפים והתנדבויות שמתאימות לאיזור .
         <br><br>
         בואו איתנו לטייל בצפון ,לתמוך בעסקים המקומיים וליהנות .       
    </div>
    """,
    unsafe_allow_html=True
)
#-----
st.divider()

#  menu title
st.markdown(
    """
    <h2 style="text-align: center; direction: rtl;">
        בחרו קטגוריה?
    </h2>
    """,
    unsafe_allow_html=True
)

# Right-to-left text
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

# Center links
left, center, right = st.columns([1, 2, 1])

with center:
    st.page_link(
         "pages/restaurants.py",
        icon="🍽",
         label="מסעדות ועגלות קפה",
         use_container_width=True
    )

    st.page_link(
        "pages/volunteering.py",
        icon="🧑‍🌾",
        label="התנדבויות",
        use_container_width=True
    )

    st.page_link(
        "pages/trips.py",
        icon="🗺️",
        label="טיולים ומצפים",
        use_container_width=True
    )

    st.page_link(
             "pages/planner.py",
             icon="📆",
             label="תכנן את היום המושלם בצפון!",
             use_container_width=True
    )

    st.page_link(
        "pages/about_us.py",
        icon= "💌",
        label="אודותינו",
        use_container_width=True
    )

    st.page_link(
        "pages/activities.py",
        label="אטרקציות",
        use_container_width=True
)

for i in range (20):
    st.markdown("")


if st.button('אם בחרתם חוויה מהאתר שלנו, אתם מוזמנים ללחוץ ממש פה ולהיכנס אל פלייליסט הנסיעה שלכם בספוטיפיי'):
    file_name = 'https://open.spotify.com/playlist/3f8ThidoZ5UP14eyX0jY77?si=c__dx6QuRl6RmZqAibvq_Q'
    check_output("start " + file_name, shell=True)
