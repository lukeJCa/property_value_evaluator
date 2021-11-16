import os
import boto3
import base64
from botocore.client import ClientError

ROOT_DIR = 'rootdir'
ROOT_S3_DIR = '22110274-cloudstorage'
bucket_config = {'LocationConstraint':'ap-southeast-2'}
password = 'kitty and the kat'

def encrypt_file(password, in_filename, out_filename):

    key = hashlib.sha256(password.encode("utf-8")).digest()

    iv = Random.new().read(AES.block_size)
    encryptor = AES.new(key, AES.MODE_CBC, iv)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(iv)

            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += ' '.encode("utf-8") * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


def decrypt_file(password, in_filename, out_filename):

    key = hashlib.sha256(password.encode("utf-8")).digest()

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(CHUNK_SIZE)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)
    
    
def main(initialize = True):
  if initialize == True:
    s3 = boto3.resource('s3')
    try:
      s3.meta.client.head_bucket(Bucket= ROOT_S3_DIR)
    except ClientError:
      bucket = s3.create_bucket(Bucket= ROOT_S3_DIR, CreateBucketConfiguration = bucket_config)
  s3 = boto3.client('s3')
  
  for dir_name, subdir_list, file_list in os.walk(ROOT_DIR, topdown=True):
    if dir_name != ROOT_DIR:
      for fname in file_list:
        encrypt_file(password,"%s/" % dir_name + fname, out_filename="afile1_dec.txt.enc")
        decrypt_file(password, "%s/" % dir_name + fname, out_filename="afilenew_dec.txt") 
        s3.upload_file("%s/" % dir_name + fname, ROOT_S3_DIR , fname)
  print("done")
if __name__ == "__main__":
  main()