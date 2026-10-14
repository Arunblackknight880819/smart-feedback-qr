import numpy as np
import qrcode
import cv2
import os


# --------------------------------------------------
# 1. CREATE NUMPY ARRAY
# --------------------------------------------------

feedback_data = np.array([
    ["101", "Amazon", "https://www.amazon.com/gp/buyagain"],
    ["102", "Flipkart", "https://www.flipkart.com/"],
    ["103", "Swiggy", "https://www.swiggy.com/"],
    ["104", "Zomato", "https://www.zomato.com/"],
    ["105", "Netflix", "https://www.netflix.com/"]
])


# --------------------------------------------------
# 2. DISPLAY AVAILABLE RECORDS
# --------------------------------------------------

def display_records():

    print("\nAvailable Feedback Records")
    print("-" * 60)

    for record in feedback_data:
        print(
            f"ID: {record[0]} | "
            f"Business: {record[1]} | "
            f"URL: {record[2]}"
        )


# --------------------------------------------------
# 3. FIND RECORD BY ID
# --------------------------------------------------

def find_feedback_record(feedback_id):

    for record in feedback_data:

        if record[0] == feedback_id:
            return record

    return None


# --------------------------------------------------
# 4. GENERATE QR CODE
# --------------------------------------------------

def generate_qr(feedback_id):

    record = find_feedback_record(feedback_id)

    if record is None:

        print("\n❌ Invalid Feedback ID.")

        return

    business = record[1]
    feedback_url = record[2]

    # QR contains ID + URL
    qr_data = f"{feedback_id}|{feedback_url}"

    qr = qrcode.QRCode(
        version=1,
        box_size=10,
        border=5
    )

    qr.add_data(qr_data)
    qr.make(fit=True)

    image = qr.make_image(fill_color="black", back_color="white")

    filename = f"feedback_{feedback_id}.png"

    image.save(filename)

    print("\n✅ QR Code Generated")
    print(f"Business : {business}")
    print(f"Feedback ID : {feedback_id}")
    print(f"URL : {feedback_url}")
    print(f"QR File : {filename}")


# --------------------------------------------------
# 5. SCAN QR CODE
# --------------------------------------------------

def scan_qr():

    filename = input(
        "\nEnter QR image filename "
        "(example: feedback_101.png): "
    )

    if not os.path.exists(filename):

        print("\n❌ QR image does not exist.")

        return

    image = cv2.imread(filename)

    detector = cv2.QRCodeDetector()

    data, points, _ = detector.detectAndDecode(image)

    if not data:

        print("\n❌ Could not decode QR code.")

        return

    print("\n✅ QR Code Successfully Decoded")
    print(f"Decoded Data: {data}")

    # Expected format:
    # 101|https://example.com

    try:

        feedback_id, scanned_url = data.split("|", 1)

    except ValueError:

        print("\n❌ Invalid QR data format.")

        return

    # --------------------------------------------------
    # 6. RETRIEVE RECORD FROM NUMPY ARRAY
    # --------------------------------------------------

    record = find_feedback_record(feedback_id)

    if record is None:

        print("\n❌ Invalid Feedback ID.")
        print("No matching record exists.")

        return

    print("\n========== FEEDBACK RECORD ==========")

    print(f"Feedback ID : {record[0]}")
    print(f"Business    : {record[1]}")
    print(f"Feedback URL: {record[2]}")

    print("=====================================")


# --------------------------------------------------
# 7. MAIN MENU
# --------------------------------------------------

def main():

    while True:

        print("\n")
        print("=" * 50)
        print("       SMART FEEDBACK QR SYSTEM")
        print("=" * 50)

        print("1. Display Feedback Records")
        print("2. Generate QR Code")
        print("3. Scan QR Code")
        print("4. Exit")

        choice = input("\nEnter your choice: ")

        # ------------------------------------------
        # OPTION 1
        # ------------------------------------------

        if choice == "1":

            display_records()

        # ------------------------------------------
        # OPTION 2
        # ------------------------------------------

        elif choice == "2":

            feedback_id = input(
                "\nEnter Feedback ID: "
            )

            generate_qr(feedback_id)

        # ------------------------------------------
        # OPTION 3
        # ------------------------------------------

        elif choice == "3":

            scan_qr()

        # ------------------------------------------
        # OPTION 4
        # ------------------------------------------

        elif choice == "4":

            print("\nThank you for using Smart Feedback QR System.")

            break

        # ------------------------------------------
        # INVALID MENU OPTION
        # ------------------------------------------

        else:

            print("\n❌ Invalid menu choice.")


# --------------------------------------------------
# PROGRAM ENTRY POINT
# --------------------------------------------------

if __name__ == "__main__":

    main()