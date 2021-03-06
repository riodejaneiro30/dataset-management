def drive_url_converter(url):
    list_url = url.split('/')
    file_id = list_url[5]
    return f'https://drive.google.com/uc?id={file_id}'