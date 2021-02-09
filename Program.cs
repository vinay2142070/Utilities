using System;
using System.Collections.Generic;
using System.Diagnostics;
using System.IO;
using System.Security.Cryptography;

namespace Aes_Example
{
    class AesExample
    {
        public static void Main()
        {
            IDictionary<string, string> keyPairMap = new Dictionary<string, string>();
            string outputFilePath = null;

            Console.Write("Please enter the PartnerID : ");
            string partnerID = Console.ReadLine();
            keyPairMap.Add("api-id", partnerID);

            Console.Write("Please enter the Request/Response file path : ");
            string jsonFilePath = Console.ReadLine();
            string plainText = File.ReadAllText(jsonFilePath);

            Console.Write("Encryption or Decryption , input either E or D : ");
            string processToFollow = Console.ReadLine();

            Console.Write("Please enter the outputfile path : ");
            outputFilePath = Console.ReadLine();

            if (processToFollow.Trim() == "E")
            {
                Console.Write("Please enter the public key file path: ");
                string publicKeyxmlpath = Console.ReadLine();
                string publickey = File.ReadAllText(publicKeyxmlpath);

                using (AesManaged aes = new AesManaged())
                {
                    aes.Mode = CipherMode.CBC;
                    aes.Padding = PaddingMode.PKCS7;
                    aes.BlockSize = 128;
                    aes.KeySize = 128;
                    aes.IV = EncryptionUtil.copyOfRange(aes.Key, 0, 16);

                    // Encrypt string    
                    byte[] encryptedBytes = EncryptionUtil.AESEncrypt(plainText, aes.Key, aes.IV);
                    string aesHexKey = BitConverter.ToString(aes.Key).Replace("-", string.Empty);
                    //Console.WriteLine("AES Hex Key: " + aesHexKey);

                    var hexEncryptedBody = BitConverter.ToString(encryptedBytes).Replace("-", string.Empty);
                    Debug.WriteLine("Encrypted Data Hex: \n" + hexEncryptedBody);
                    keyPairMap.Add("EncodedJsonBody", hexEncryptedBody);

                    string RSAEncryptedKey = EncryptionUtil.RSAPublicKeyEncrypt(publickey, aesHexKey, partnerID);
                    Debug.WriteLine("API Key : \n" + RSAEncryptedKey);
                    keyPairMap.Add("api-key", RSAEncryptedKey);

                }
            }
            else if (processToFollow == "D")
            {
                Console.SetIn(new StreamReader(Console.OpenStandardInput(8192)));
                Console.Write("Please enter the api-key : ");
                string apiId = Console.ReadLine();
                keyPairMap.Add("api-key", apiId);

                Console.Write("Please enter the private key file path : ");
                string privateKeyxmlpath = Console.ReadLine();
                string privateKey = File.ReadAllText(privateKeyxmlpath);

                string decryptedText =  EncryptionUtil.RSAPrivateKeyDecrypt(privateKey, apiId);
                string hexKey = decryptedText; //decryptedText.Replace(";;",";").Split(';')[1];
                Debug.WriteLine("Decrypted Hex AES Key : " + hexKey);

                byte[] byteKey = EncryptionUtil.HexadecimalStringToByteArray(hexKey);

                string decrypted = EncryptionUtil.AESDecrypt(plainText, byteKey, EncryptionUtil.copyOfRange(byteKey, 0, 16));
                Debug.WriteLine("Decrypted data : {decrypted} " + decrypted);
                keyPairMap.Add("Decrypted data", decrypted);
            }
            EncryptionUtil.generateOutputFile(keyPairMap, outputFilePath);
            Console.WriteLine("Please check the outputfile");
            Console.ReadLine();
        }
    }

   

}

