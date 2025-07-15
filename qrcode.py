import pyqrcode
url = ""
n = pyqrcode.create (url)
n.png ('Natheer.png', scale=5)
