def convert_image_to_bytes():
    with open('logo.png', 'rb') as f:
        bytes_data = f.read()
    
    print("EMBEDDED_ICON = ", bytes_data)

if __name__ == '__main__':
    convert_image_to_bytes() 