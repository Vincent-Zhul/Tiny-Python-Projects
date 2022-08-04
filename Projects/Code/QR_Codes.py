import pyqrcode

# Set QR code information
s = "https://github.com/"

# Generate QR code
url = pyqrcode.create(s)

# Save QR code
url.svg("Github.svg", scale=8)