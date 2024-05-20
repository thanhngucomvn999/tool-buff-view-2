import webbrowser, time
url = input("link video: ")

duration = input("số lần: ")
for i in range(5):
    webbrowser.open_new(url)
    time.sleep(int(duration))
