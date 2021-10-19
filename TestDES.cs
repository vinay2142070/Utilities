/******************************************************************************

                            Online C# Compiler.
                Code, Compile, Run and Debug C# program online.
Write your code in this editor and press "Run" button to execute it.

*******************************************************************************/

using System;
using System.Collections;
using System.Collections.Generic;
//using System.Data;
using System.Diagnostics;
using System.Security;
using System.Security.Cryptography;
using System.Text;
using System.IO;


class HelloWorld {
  static void Main() {
    Console.WriteLine(Decrypt2("l5ducOfM1vQUfA6/K/bf23+GVWAl64i0","false"));
  }
  
  public static void PrintByteArray(byte[] bytes)
{
    var sb = new StringBuilder("new byte[] { ");
    foreach (var b in bytes)
    {
        sb.Append(b + ", ");
    }
    sb.Append("}");
    Console.WriteLine(sb.ToString());
}
   
  public static string Encrypt2(string clearText,string key)
{
    try
    {
        string encryptedText = "";
        MD5 md5 = new MD5CryptoServiceProvider();
        TripleDES des = new TripleDESCryptoServiceProvider();
       // des.KeySize = 192;
        des.Mode = CipherMode.ECB;
        des.Padding = PaddingMode.PKCS7;

       // byte[] md5Bytes = md5.ComputeHash(Encoding.Unicode.GetBytes(key));

        //byte[] ivBytes = new byte[8];

       byte[] readText = File.ReadAllBytes(@"encryptkey.dat");
      
      sbyte[] signed = {-2, 69, -63, -110, -128, -2, -5, 28, 104, 87, -111, 64, 1, -26, -105, 4, -110, -113, -14, 73, -63, -75, -65, -39};
        byte[] unsigned = (byte[]) (Array)signed;
        PrintByteArray(readText);
         Console.WriteLine("length:"+readText.Length);
         
        
      
        des.Key = unsigned;

      //  des.IV = ivBytes;

        byte[] clearBytes = Encoding.Unicode.GetBytes(clearText);

        ICryptoTransform ct = des.CreateEncryptor();
        using (MemoryStream ms = new MemoryStream())
        {
            using (CryptoStream cs = new CryptoStream(ms, des.CreateEncryptor(), CryptoStreamMode.Write))
            {
                cs.Write(clearBytes, 0, clearBytes.Length);
                cs.Close();
            }
            encryptedText = Convert.ToBase64String(ms.ToArray());
        }
        return encryptedText;
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.ToString());
    }
    return "";
}

public static string Decrypt2(string cipher,string key)
{
    try
    {
        byte[] clearBytes = Convert.FromBase64String(cipher);
        MD5 md5 = new MD5CryptoServiceProvider();
        byte[] md5Bytes = md5.ComputeHash(Encoding.Unicode.GetBytes(key));
        string encryptedText = "";
        TripleDES des = new TripleDESCryptoServiceProvider();
       //des.KeySize = 192;
        des.Mode = CipherMode.ECB;
        des.Padding = PaddingMode.PKCS7;
        byte[] ivBytes = new byte[8];
      byte[] readText = File.ReadAllBytes(@"encryptkey.dat");
      sbyte[] signed = {-2, 69, -63, -110, -128, -2, -5, 28, 104, 87, -111, 64, 1, -26, -105, 4, -110, -113, -14, 73, -63, -75, -65, -39};
        byte[] unsigned = (byte[]) (Array)signed;
       // Console.WriteLine("key size in bytes"+Convert.FromBase64String("AAECAwQFBgcICQoLDA0ODw=="));
        des.Key = unsigned;
       // des.IV = ivBytes;
        ICryptoTransform ct = des.CreateDecryptor();
        byte[] resultArray = ct.TransformFinalBlock(clearBytes, 0, clearBytes.Length);
        encryptedText = Encoding.Default.GetString(resultArray);
        return encryptedText;
    }
    catch (Exception ex)
    {
        Console.WriteLine(ex.ToString());
    }
     return "";
}
}
