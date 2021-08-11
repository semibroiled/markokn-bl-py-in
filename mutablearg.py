def listing (formats = ('gif', 'jpg', 'png')):
    if 'jpg' in formats:
        print('True')
        formats.append('jpeg')
    print(formats)
    return formats
listing()
print(listing())
listing()
