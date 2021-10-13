using Microsoft.VisualBasic;
using System;
using System.Collections;
using System.Collections.Generic;
//using System.Data;
using System.Diagnostics;
using System.Security;
using System.Security.Cryptography;
using System.Text;
using System.IO;



public class Test
{
    public static void Main()
    {
         try
        {
            DESCryptoServiceProvider myDESProvider = new DESCryptoServiceProvider();
             myDESProvider.Key = ASCIIEncoding.ASCII.GetBytes("12345678");
            myDESProvider.IV = ASCIIEncoding.ASCII.GetBytes("12345678");

            ICryptoTransform myICryptoTransform = myDESProvider.CreateEncryptor(myDESProvider.Key, myDESProvider.IV);

            FileStream ProcessFileStream = new FileStream("testmd.txt", FileMode.Open, FileAccess.Read);
            FileStream ResultFileStream = new FileStream("testenc.txt", FileMode.Create, FileAccess.Write);
            CryptoStream myCryptoStream = new CryptoStream(ResultFileStream, myICryptoTransform, CryptoStreamMode.Write);
             byte[] bytearrayinput = new byte[ProcessFileStream.Length];
             ProcessFileStream.Read(bytearrayinput, 0, bytearrayinput.Length);
            myCryptoStream.Write(bytearrayinput, 0, bytearrayinput.Length);
             myCryptoStream.Close();
            ProcessFileStream.Close();
            ResultFileStream.Close();
            
            myDESProvider.IV = ASCIIEncoding.ASCII.GetBytes("12345677");
             FileStream DecryptedFile = new FileStream("testenc.txt", FileMode.Open, FileAccess.Read);

             myICryptoTransform = myDESProvider.CreateDecryptor(myDESProvider.Key, myDESProvider.IV);

             myCryptoStream = new CryptoStream(DecryptedFile, myICryptoTransform, CryptoStreamMode.Read);

             StreamReader myDecStreamReader = new StreamReader(myCryptoStream);

            StreamWriter myDecStreamWriter = new StreamWriter("testdec.txt");

             myDecStreamWriter.Write(myDecStreamReader.ReadToEnd());

             myCryptoStream.Close();

            myDecStreamReader.Close();

            myDecStreamWriter.Close();
        }
        catch (Exception ex)
        {
           Console.WriteLine(ex.ToString());
        }
    }
}
