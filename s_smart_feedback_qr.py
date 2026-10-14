import streamlit as st
import numpy as np
import qrcode
import cv2

from PIL import Image
from io import BytesIO



# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="Smart Feedback QR System",
    page_icon="📱",
    layout="wide"
)


# ============================================================
# FEEDBACK DATA - NUMPY ARRAY
# ============================================================

feedback_data = np.array([
    ["FB001", "ABC Restaurant", "https://example.com/abc-feedback"],
    ["FB002", "XYZ Hotel", "https://example.com/xyz-feedback"],
    ["FB003", "Tech Store", "https://example.com/tech-feedback"],
    ["FB004", "Coffee House", "https://example.com/coffee-feedback"],
    ["FB005", "Fashion Store", "https://example.com/fashion-feedback"]
])


# ============================================================
# FIND FEEDBACK RECORD
# ============================================================

def find_feedback(feedback_id):

    feedback_id = feedback_id.strip().upper()

    matches = feedback_data[
        feedback_data[:, 0] == feedback_id
    ]

    if len(matches) == 0:
        return None

    return matches[0]


# ============================================================
# GENERATE QR CODE
# ============================================================

def generate_qr(feedback_id): 
    # Step 1: Create a QR code object
    qr = qrcode.QRCode( 
        version=1, 
        box_size=10, 
        border=4 
        ) 

    # Step 2: Add the feedback ID
    qr.add_data(feedback_id) 

    # Step 3: Generate the QR pattern
    qr.make(fit=True) 
    
    # Step 4: Convert the QR pattern into a Pillow image

    qr_image = qr.make_image( 
        fill_color="black", 
        back_color="white" )
    
    # Step 5: Create an in-memory buffer
    
    buffer = BytesIO() 

    # Step 6: Save the image as PNG bytes
    qr_image.save(buffer, format="PNG") 
    
    # Step 7: Return the PNG data 
    
    return buffer.getvalue()


# ============================================================
# CONVERT QR IMAGE TO BYTES
# ============================================================

def qr_to_bytes(qr_image):

    buffer = BytesIO()

    qr_image.save(buffer, format="PNG")

    return buffer.getvalue()


# ============================================================
# DECODE QR CODE
# ============================================================

def decode_qr(uploaded_file):

    try:

        image = Image.open(uploaded_file)

        image_array = np.array(image)

        detector = cv2.QRCodeDetector()

        data, points, _ = detector.detectAndDecode(
            image_array
        )

        if data:

            return data.strip()

        return None

    except Exception:

        return None


# ============================================================
# APPLICATION HEADER
# ============================================================

st.title("📱 Smart Feedback QR System")

st.write(
    """
    Generate QR codes for feedback records, scan QR codes,
    and retrieve the corresponding feedback URL from a NumPy array.
    """
)

st.divider()


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
    "Select an operation",
    [
        "🏠 Dashboard",
        "🔲 Generate QR",
        "📷 Scan QR",
        "📋 View Records"
    ]
)


# ============================================================
# DASHBOARD
# ============================================================

if page == "🏠 Dashboard":

    st.header("Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Feedback Records",
            len(feedback_data)
        )

    with col2:

        st.metric(
            "QR Enabled",
            len(feedback_data)
        )

    with col3:

        st.metric(
            "Storage",
            "NumPy Array"
        )

    st.info(
        "Use the sidebar to generate or scan a feedback QR code."
    )


# ============================================================
# GENERATE QR
# ============================================================

elif page == "🔲 Generate QR":

    st.header("Generate Feedback QR Code")

    feedback_id = st.selectbox(
        "Select Feedback ID",
        feedback_data[:, 0]
    )

    record = find_feedback(feedback_id)

    if record is not None:

        st.subheader("Feedback Information")

        col1, col2 = st.columns(2)

        with col1:
            st.write("**Feedback ID:**")
            st.code(record[0])

            st.write("**Business:**")
            st.write(record[1])

        with col2:
            st.write("**Feedback URL:**")
            st.write(record[2])

        st.divider()

        # Generate QR code as PNG bytes
        qr_image = generate_qr(record[0])

        # Display QR code
        st.image(
            qr_image,
            caption=f"QR Code for {record[0]}",
            width=300
        )

        # Download QR code directly as PNG bytes
        st.download_button(
            label="⬇️ Download QR Code",
            data=qr_image,
            file_name=f"{record[0]}_feedback_qr.png",
            mime="image/png"
        )

# ============================================================
# VIEW RECORDS
# ============================================================

elif page == "📋 View Records":

    st.header("Feedback Records")

    st.dataframe(
        feedback_data,
        column_config={
            0: "Feedback ID",
            1: "Business",
            2: "Feedback URL"
        },
        width="stretch"
    )

    st.info(
        "The records displayed above are stored in a NumPy array."
    )