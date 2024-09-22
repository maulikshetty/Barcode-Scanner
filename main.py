import cv2
import zxing
import requests

# barcodelookup api key - readme file has link and details
API_KEY = 'API_key_here'  # Replace with your actual API key


def decode_barcode(image_path):
    reader = zxing.BarCodeReader()
    barcode = reader.decode(image_path)

    if barcode:
        print(f"Detected barcode: {barcode.parsed}")
        lookup_item(barcode.parsed)
        return barcode.parsed
    else:
        print("No barcode detected")
        return None

# Function to capture barcode from camera
def capture_from_camera():
    cap = cv2.VideoCapture(0)  # 0 means default camera
    if not cap.isOpened():
        print("Unable to access the camera")
        return None

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to grab frame")
            break

        # Save the frame temporarily to decode
        temp_image_path = "temp_barcode.jpg"
        cv2.imwrite(temp_image_path, frame)


        barcode_data = decode_barcode(temp_image_path)

        if barcode_data:
            print(f"Barcode Detected: {barcode_data}")
            break

        cv2.imshow('Barcode Scanner (Press "q" to quit)', frame)

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()


def lookup_item(barcode):
    url = f"https://api.barcodelookup.com/v3/products?barcode={barcode}&formatted=y&key={API_KEY}"

    headers = {
        'Content-Type': 'application/json',
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        if 'products' in data and len(data['products']) > 0:
            item = data['products'][0]
            print(f"Item found: {item['title']}")
            print(f"Brand: {item['brand']}")
            print(f"Category: {item['category']}")
        else:
            print("Item not found.")
    else:
        print(f"Error: {response.status_code}")

# Main function to choose between camera or image file
def main():
    print("Choose an option:")
    print("1. Use Camera")
    print("2. Upload Image")
    print("3. Enter number")

    choice = input("Enter choice (1 or 2 or 3): ")

    if choice == '1':
        print("Starting camera...")
        capture_from_camera()
    elif choice == '2':
        image_path = input("Enter the path of the image file: ")
        decode_barcode(image_path)
    elif choice == '3': 
        barcode = int(input("Enter the barcode: "))
        lookup_item(barcode)    
    else:
        print("Invalid choice. Please select 1 or 2 or 3.")

if __name__ == "__main__":
    main()