# Barcode-Scanner

# Using python packages:

1. cv2 for camera use - real time frame processing and reading and processing barcodes
2. zxing, which was used for decoding 1D and 2D barcodes, such as UPC, EAN and QR Codes from images and real time streams.
3. requests for querying an API Service for the information on the barcode.

# How can you use:

1. Use Camera - which will ask for camera permissions and use your camera to look for barcodes
2. Upload Image - save an image in the same path as the python file or retreive the path to the image and input to lookup barcode from the image
3. Manual - Enter the barcode number directly to get information about it

# Current Disadvantages and issues:

1. Barcodes in images and camera mode, should be shown horizontaly, to be detected.
2. Web Interface is not made, I might plan to make one and integrate this.

# Services Used:

Barcode Lookup - https://www.barcodelookup.com/api
