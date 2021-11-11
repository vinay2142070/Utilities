import subprocess
compressor = subprocess.Popen(
     ['zip', '-9','test.zip', 'test.txt'], stdout=subprocess.PIPE)
subprocess.Popen(
        "openssl enc -e -aes-256-cbc -md sha256 -in  test.zip -out myenc.enc -pass pass:123456".split(), stdin=compressor.stdout)
