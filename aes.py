from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad
import time
output_file = 'enc.bin' # Output file
data = b'This is a super secret message' # Must be a bytes object
key = b'YOURKEY0YOURKEY0' # The key you generated

# Create cipher object and encrypt the data

start = time.process_time()
skipBytes = ""
new_data= ""

for i, v in enumerate(data):
    if(i%4==0):
        skipBytes+=chr(v)
    else:
        new_data +=chr(v)

new_data = str.encode(new_data)
print(new_data)
print(skipBytes)
cipher = AES.new(key, AES.MODE_CBC) # Create a AES cipher object with the key using the mode CBC
ciphered_data = cipher.encrypt(pad(new_data, AES.block_size)) # Pad the input data and then encrypt
print(ciphered_data)
file_out = open(output_file, "wb") # Open file to write bytes
file_out.write(cipher.iv) # Write the iv to the output file (will be required for decryption)


skipBytes = str.encode(skipBytes)
file_out.write(ciphered_data + skipBytes)  # Write the varying length ciphertext to the file (this is the encrypted data)
print(ciphered_data + skipBytes)
file_out.close()








file_in = open(output_file, 'rb') # Open the file to read bytes
iv = file_in.read(16) # Read the iv out - this is 16 bytes long
ciphered_data = file_in.read() # Read the rest of the data
skippedData = ciphered_data[-6:]
print("retruved", skippedData)
file_in.close()
cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
original_data = unpad(cipher.decrypt(ciphered_data[:-8]), AES.block_size) # Decrypt and then up-pad the result
print("decrypted")
print(original_data)
print(time.process_time() - start)




# Read the data from the file
