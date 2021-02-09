using System;
using System.Collections.Generic;
using System.Text;
using System.IO;
using System.Security.Cryptography;

namespace Aes_Example
{
    class EncryptionUtil
    {
       public static byte[] AESEncrypt(string text, byte[] key, byte[] IV)
        {
            byte[] encrypted;
            using (AesManaged aes = new AesManaged())
            {
                aes.Mode = CipherMode.CBC;
                aes.Padding = PaddingMode.PKCS7;
                // aes.Padding = PaddingMode.None;
                aes.BlockSize = 128;
                aes.KeySize = 128;

                ICryptoTransform encryptor = aes.CreateEncryptor(key, IV);
                using (MemoryStream ms = new MemoryStream())
                {
                    using (CryptoStream cs = new CryptoStream(ms, encryptor, CryptoStreamMode.Write))
                    {
                        using (StreamWriter sw = new StreamWriter(cs))
                            sw.Write(text);
                        encrypted = ms.ToArray();
                    }
                }
            }
            return encrypted;
        }

       public static string AESDecrypt(string hexText, byte[] key, byte[] IV)
        {
            byte[] text = HexadecimalStringToByteArray(hexText);
            string plainText = null;
            using (AesManaged aes = new AesManaged())
            {
                aes.Mode = CipherMode.CBC;
                aes.Padding = PaddingMode.PKCS7;
                // aes.Padding = PaddingMode.None;
                aes.BlockSize = 128;
                aes.KeySize = 128;

                ICryptoTransform decryptor = aes.CreateDecryptor(key, IV);
                using (MemoryStream ms = new MemoryStream(text))
                {
                    using (CryptoStream cs = new CryptoStream(ms, decryptor, CryptoStreamMode.Read))
                    {
                        using (StreamReader reader = new StreamReader(cs))
                        {
                            plainText = reader.ReadToEnd();
                        }
                    }
                }
            }
            return plainText;
        }

        public static byte[] HexadecimalStringToByteArray(string input)
        {
            var outputLength = input.Length / 2;
            var output = new byte[outputLength];
            using (var sr = new StringReader(input))
            {
                for (var i = 0; i < outputLength; i++)
                    output[i] = Convert.ToByte(new string(new char[2] { (char)sr.Read(), (char)sr.Read() }), 16);
            }
            return output;
        }

        public static byte[] copyOfRange(byte[] original, int from, int to)
        {
            int newLength = to - from;
            byte[] copy = new byte[newLength];
            Array.Copy(original, from, copy, 0,
                             Math.Min(original.Length - from, newLength));
           return copy;
        }

        public static string RSAPublicKeyEncrypt(string publickey, string aesHexKey, string partnerID)
        {

             string tobeEncryptedString = partnerID + ";;" + aesHexKey;
            var csp = new RSACryptoServiceProvider(2048);
            csp.FromXmlString(publickey);

            //for encryption, always handle bytes...
            var bytesPlainTextData = Encoding.UTF8.GetBytes(tobeEncryptedString);

            //apply pkcs#1.5 padding and encrypt our data 
            var bytesEncryptedText = csp.Encrypt(bytesPlainTextData, RSAEncryptionPadding.Pkcs1);

            //we might want a string representation of our cypher text... base64 will do
            var encryptedText = Convert.ToBase64String(bytesEncryptedText);

            return encryptedText;
        }

        public static string  RSAPrivateKeyDecrypt(string privatekey, string apiId)
        {
            //Console.WriteLine("entered APIID : " + apiId);
            var bytesEncryptedText = Convert.FromBase64String(apiId);

            //we want to decrypt, therefore we need a csp and load our private key
            var csp = new RSACryptoServiceProvider(2048);
            csp.FromXmlString(privatekey);

            //decrypt and strip pkcs#1.5 padding
            byte[] bytesPlainTextData = csp.Decrypt(bytesEncryptedText, RSAEncryptionPadding.Pkcs1);

            //get our original plainText back...
            var plainTextData = Encoding.UTF8.GetString(bytesPlainTextData);
            return plainTextData;
        }
        public static void generateOutputFile(IDictionary<string, string> keyPairMap, string outputFilePath)
        {
            string filepath = outputFilePath;
            using (StreamWriter file = new StreamWriter(filepath))
                foreach (var entry in keyPairMap)
                    file.WriteLine("[{0} {1}]", entry.Key, entry.Value);
        }
    }
}
