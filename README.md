# Qrcode-Genarator

🐍 1. Install Required Libraries
You'll need pyqrcode and pypng:
(pip install pyqrcode pypng)


2. Write the Code
Here’s a complete working script:
import pyqrcode

# Define the URL (make sure to include 'https://')
url = "paste your link"

# Create QR code
qr_code = pyqrcode.create(url)

# Save as PNG with proper filename and scale
qr_code.png('x.png', scale=5)

3. Run It
- Save your script (e.g., generate_qr.py)
- Run it in your terminal or IDE
