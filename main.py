def save_html(html, path): #local save
    with open(path,'wb') as f: #wb 'write bytes', avoid encoding issues #same as file opening and closing + exception handling
        f.write(html)

def open_html(path) #open/read HTML from local file
    with open(path,'rb') as f:
        return f.read
