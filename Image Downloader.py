
import urllib.request
imgURL = "https://images.unsplash.com/photo-1531804055935-76f44d7c3621?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=388&q=80.jpg"

urllib.request.urlretrieve(imgURL, "D:/python/DownloadedByPython.jpg")
