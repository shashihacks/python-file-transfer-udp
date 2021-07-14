from huffman import HuffmanCoding
import sys
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from Crypto.Util.Padding import unpad

import csv

path = "a.txt"

h = HuffmanCoding(path)
output_path = h.compress()
print("Compressed file path: " )
print( output_path)

#ncrypt here
data = b'Your data....' 
data = open('a.bin', 'rb').read()
key = b'YOURKEY0YOURKEY0' 
output_file="enc.bin"
cipher = AES.new(key, AES.MODE_CBC) 
ciphered_data = cipher.encrypt(pad(data, AES.block_size)) 
# print(ciphered_data)

file_out = open(output_file, "wb")
file_out.write(cipher.iv) 
file_out.write(ciphered_data) 
file_out.close()




# decrypt

file_in = open(output_file, 'rb')
iv = file_in.read(16) # Read the iv out - this is 16 bytes long
ciphered_data = file_in.read() 
file_in.close()
cipher = AES.new(key, AES.MODE_CBC, iv=iv)  # Setup cipher
original_data = unpad(cipher.decrypt(ciphered_data), AES.block_size) # Decrypt and then up-pad the result
print("decrypted")
print(original_data)
newFileByteArray = bytearray(original_data)
newFile = open("dec.bin", "wb")
newFile.write(newFileByteArray)
newFile.close()
#decmpress

# f = open("decrypted.bin", "wb")
# f.write(original_data)
# f.close()

decom_path = h.decompress('dec.bin')
print("Decompressed file path: " + decom_path)




