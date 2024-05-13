import base64

def get_file_extension(base64_string):
    # Decode the base64 string
    decoded_data = base64.b64decode(base64_string)

    # Common file signatures for various file types
    file_signatures = {
        b'\xFF\xD8\xFF': 'jpg',
        b'\x89\x50\x4E\x47\x0D\x0A\x1A\x0A': 'png',
        b'\x47\x49\x46\x38\x39\x61': 'gif',
        b'%PDF-': 'pdf',
        b'\x25\x50\x44\x46': 'pdf',  # Additional PDF signature
        b'\x1F\x8B\x08': 'gzip',     # GZIP compressed file signature
        # Add more file signatures for other file types as needed
        b'\xFF\xFB': 'mp3',  # MP3 file signature
        b'RIFF': 'wav',       # WAV file signature
        b'ID3': 'mp3',        # MP3 file signature
        # Video file signatures
        b'\x00\x00\x00\x14ftyp': 'mp4',  # MP4 file signature
        b'\x00\x00\x00\x18ftyp': 'mp4',  # Another common MP4 file signature
        b'\x00\x00\x01\x00': 'mpg',      # MPEG file signature
    }

    # Check if the decoded data starts with any of the known file signatures
    for signature, extension in file_signatures.items():
        if decoded_data.startswith(signature):
            return extension
    # If no known file signature matches, assume it's a TXT file
    return 'txt'


# Example usage:
base64_string = "..."  # Your Base64 encoded string
extension = get_file_extension(base64_string)
print("File extension:", extension)