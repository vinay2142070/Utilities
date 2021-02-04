package com.hdfc.utilities.encryption;

import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.Files;
import java.nio.file.Paths;
import java.security.InvalidAlgorithmParameterException;
import java.security.InvalidKeyException;
import java.security.KeyFactory;
import java.security.NoSuchAlgorithmException;
import java.security.PrivateKey;
import java.security.PublicKey;
import java.security.SecureRandom;
import java.security.spec.InvalidKeySpecException;
import java.security.spec.PKCS8EncodedKeySpec;
import java.security.spec.X509EncodedKeySpec;
import java.util.Arrays;
import java.util.HashMap;
import java.util.Map;
import java.util.Map.Entry;
import java.util.Scanner;

import javax.crypto.BadPaddingException;
import javax.crypto.Cipher;
import javax.crypto.IllegalBlockSizeException;
import javax.crypto.KeyGenerator;
import javax.crypto.NoSuchPaddingException;
import javax.crypto.SecretKey;
import javax.crypto.spec.IvParameterSpec;
import javax.crypto.spec.SecretKeySpec;

import org.apache.commons.codec.DecoderException;
import org.apache.commons.codec.binary.Base64;
import org.apache.commons.codec.binary.Hex;
import org.apache.log4j.Logger;

public class EncryptionUtil {

	private static final Logger logger = Logger.getLogger(EncryptionUtil.class);

	public static void main(String[] args) throws Exception {
		Map<String, String> keyPairMap = new HashMap<String, String>();
		Scanner scannerInput = new Scanner(System.in);
		String outputFilePath = null;
		System.out.print("Enter the partner Id: ");
		String partnerId = scannerInput.nextLine();
		System.out.print("Enter the Request/Response file path: ");
		String jsonFilePath = scannerInput.nextLine();
		String plainText = new String(Files.readAllBytes(Paths.get(jsonFilePath)));
		System.out.print("Encryption or Decryption , input either E or D");
		String processToFollow = scannerInput.nextLine();
		keyPairMap.put("api-id", partnerId);
			if (processToFollow.equalsIgnoreCase("E")) {
				System.out.print("Enter the publicKey file path: ");
				String publicKeyJson = scannerInput.nextLine();
				String publickKey = new String(Files.readAllBytes(Paths.get(publicKeyJson)));
				getEncryptedKeyPairMap(publickKey,keyPairMap, plainText, partnerId);
				System.out.print("Enter the output path: ");
				// Sample Path "/apps/group/output/EncryptedDetails.txt"
				String outputPath = scannerInput.nextLine();
				outputFilePath = outputPath;
			} else if (processToFollow.equalsIgnoreCase("D")) {
				System.out.print("Enter the api-id : ");
				String apiId = scannerInput.nextLine();
				System.out.print("Enter the privateKey file path: ");
				String privateKeyJson = scannerInput.nextLine();
				String privateKey = new String(Files.readAllBytes(Paths.get(privateKeyJson)));
				getDecryptedKeyPairMap(privateKey, keyPairMap, plainText, apiId);
				System.out.print("Enter the output path: ");
				// Sample Path "/apps/group/output/EncryptedDetails.txt"
				String outputPath = scannerInput.nextLine();
				outputFilePath = outputPath;
			}
			generateOutputFile(keyPairMap, outputFilePath);
		scannerInput.close();
	}

	public static SecretKey generateAESSecretKey(int keyBitSize) throws NoSuchAlgorithmException {
		logger.info("Inside generateAESSecretKey() in EncryptionUtil");
		KeyGenerator keyGenerator = KeyGenerator.getInstance("AES");
		SecureRandom secureRandom = new SecureRandom();
		keyGenerator.init(keyBitSize, secureRandom);
		return keyGenerator.generateKey();
	}

	public static String bytesToHex(byte[] bytes) {
		logger.info("bytes to hex start");
		final char[] hexaAe = "0123456789ABCDEF".toCharArray();
		char[] hexChars = new char[bytes.length * 2];
		for (int j = 0; j < bytes.length; j++) {
			int v = bytes[j] & 0xFF;
			hexChars[j * 2] = hexaAe[v >>> 4];
			hexChars[j * 2 + 1] = hexaAe[v & 0x0F];
		}
		logger.info("bytes to hex end");
		return new String(hexChars);
	}

	public static String encryptRequestUsingAES(String hexKey, String responseBody, byte[] raw)
			throws NoSuchAlgorithmException, NoSuchPaddingException, InvalidKeyException,
			InvalidAlgorithmParameterException, IllegalBlockSizeException, BadPaddingException, DecoderException {
		logger.info("Inside encryptResponseUsingAES() in EncryptionUtil");
		logger.info("HexKey" + hexKey);
		byte[] iv = Arrays.copyOfRange(raw, 0, 16);
		String encyptedResponse = "";
		SecretKeySpec skeySpec = new SecretKeySpec(raw, "AES");
		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
		cipher.init(Cipher.ENCRYPT_MODE, skeySpec, new IvParameterSpec(iv));
		encyptedResponse = bytesToHex(cipher.doFinal(responseBody.getBytes(StandardCharsets.UTF_8)));
		logger.info("Exiting encryptResponseUsingAES() in EncryptionUtil");
		logger.info("Exiting encryptResponseUsingAES() in EncryptionUtil " + encyptedResponse);
		return encyptedResponse;
	}

	public static String encryptSecretKeyUsingRSA(String publicKey, String hexKey)
			throws InvalidKeySpecException, NoSuchAlgorithmException, DecoderException {
		logger.info("Inside encryptSecretKeyUsingRSA() in EncryptionUtil1");
		String encryptedSecretKey = "";
		byte[] resPublic = Hex.decodeHex(publicKey.toCharArray());
		PublicKey publicKeySec = KeyFactory.getInstance("RSA").generatePublic(new X509EncodedKeySpec(resPublic));
		logger.info("before encrypting complete request");
		encryptedSecretKey = encryptOTK(publicKeySec, hexKey);
		logger.info("after encrypting complete request");
		logger.info("Exiting encryptSecretKeyUsingRSA() in EncryptionUtil " + encryptedSecretKey);
		return encryptedSecretKey;
	}

	private static String encryptOTK(PublicKey publicKey, String secretKeyString) {
		logger.info("Inside encryptOTK() in EncryptionUtil");
		String encodeedString = null;
		try {
			Cipher cipher = Cipher.getInstance("RSA");
			cipher.init(Cipher.ENCRYPT_MODE, publicKey);
			encodeedString = Base64
					.encodeBase64String(cipher.doFinal(secretKeyString.getBytes(StandardCharsets.UTF_8)));
		} catch (Exception exp) {
			logger.info("Exception in encryptOTK in EncryptionUtil " + exp);
		}
		logger.info("Inside encryptOTK() in EncryptionUtil");
		return encodeedString;
	}

	public static String decryptSecretKeyUsingRSA(String privateKeySec, String encyptedSecretKey)
			throws DecoderException, InvalidKeySpecException, NoSuchAlgorithmException, IllegalBlockSizeException,
			BadPaddingException, NoSuchPaddingException, InvalidKeyException {
		logger.debug("Entering decryptSecretKeyUsingRSA() in EncriptionFilter");
		String decryptedApiRequest = "";
		byte[] resPrivate = Hex.decodeHex(privateKeySec.toCharArray());
		PrivateKey privateKey = KeyFactory.getInstance("RSA").generatePrivate(new PKCS8EncodedKeySpec(resPrivate));
		logger.debug("before decrypting complete request");
		Cipher cipher = Cipher.getInstance("RSA");
		cipher.init(Cipher.DECRYPT_MODE, privateKey);
		decryptedApiRequest = new String(cipher.doFinal(Base64.decodeBase64(encyptedSecretKey)),
				StandardCharsets.UTF_8);
		logger.debug("after decrypting complete request");
		logger.debug("Exiting decryptSecretKeyUsingRSA() in EncriptionFilter");
		return decryptedApiRequest;
	}

	public static String decryptAESRequest(String encriptedAESRequest, String secretKeyString)
			throws InvalidKeyException, InvalidAlgorithmParameterException, IllegalBlockSizeException,
			BadPaddingException, NoSuchAlgorithmException, NoSuchPaddingException {
		logger.debug("Inside decryptAESRequest() in EncriptionFilter2");
		String decrytRequest = "";
		byte[] keyBytes = hexStringToByteArray(secretKeyString);
		byte[] iv = Arrays.copyOfRange(keyBytes, 0, 16);
		Cipher cipher = Cipher.getInstance("AES/CBC/PKCS5Padding");
		cipher.init(Cipher.DECRYPT_MODE, new SecretKeySpec(keyBytes, "AES"), new IvParameterSpec(iv));
		byte[] recoveredPlaintextBytes = cipher.doFinal(hexStringToByteArray(encriptedAESRequest));
		decrytRequest = new String(recoveredPlaintextBytes);
		logger.debug("Exiting decryptAESRequest() in EncriptionFilter");
		return decrytRequest;
	}

	public static byte[] hexStringToByteArray(String s) {
		int len = s.length();
		byte[] data = new byte[len / 2];
		for (int i = 0; i < len; i += 2) {
			data[i / 2] = (byte) ((Character.digit(s.charAt(i), 16) << 4) + Character.digit(s.charAt(i + 1), 16));
		}
		return data;
	}

	private static void generateOutputFile(Map<String, String> keyPairMap, String outputFilePath) throws IOException {
		File file = new File(outputFilePath);
		try (BufferedWriter bufferedWriter = new BufferedWriter(new FileWriter(file))) {
			// create new BufferedWriter for the output file
			// iterate map entries
			for (Entry<String, String> entry : keyPairMap.entrySet()) {
				// put key and value separated by a colon
				bufferedWriter.write(entry.getKey() + ":" + entry.getValue());
				// new line
				bufferedWriter.newLine();
			}
			bufferedWriter.flush();
		}
	}

	private static void getEncryptedKeyPairMap(String publicKey, Map<String, String> keyPairMap,
			String plainText, String partnerId) throws NoSuchAlgorithmException, InvalidKeyException, NoSuchPaddingException,
			InvalidAlgorithmParameterException, IllegalBlockSizeException, BadPaddingException, InvalidKeySpecException, DecoderException {
		logger.info("------------- AES Encryption Started");
		String encryptedBody = null;
		String encryptedKey = null;
		SecretKey secretKey = generateAESSecretKey(128);
		byte[] bytes = secretKey.getEncoded();
		String hexKey = bytesToHex(bytes);
		keyPairMap.put("EncryptedAESKey", hexKey);
		logger.info("Inside generateAESSecretKey() in EncryptionUtil " + hexKey);
		encryptedBody = encryptRequestUsingAES(hexKey, plainText, bytes);
		keyPairMap.put("EncryptedRequestBody", encryptedBody);
		encryptedKey = encryptSecretKeyUsingRSA(publicKey, partnerId+";;"+hexKey);
		keyPairMap.put("api-key", encryptedKey);
		logger.info("-------------AES Encryption Completed : " + encryptedBody);
	}

	private static void getDecryptedKeyPairMap(String privateKey, Map<String, String> keyPairMap,
			String plainText, String apiId)
			throws NoSuchAlgorithmException, InvalidKeySpecException, DecoderException, InvalidKeyException,
			IllegalBlockSizeException, BadPaddingException, NoSuchPaddingException, InvalidAlgorithmParameterException {
		logger.info("-------------RSA Decryption Started");
		String secretKeyString = decryptSecretKeyUsingRSA(privateKey, apiId);
		keyPairMap.put("secretKeyString", secretKeyString);
		logger.info("-------------RSA Decryption Completed");
		logger.info("-------------AES Decryption Started");
		logger.info("decrepted Key" + secretKeyString);
		String decryptedResponseBody = decryptAESRequest(plainText, secretKeyString);
		keyPairMap.put("decryptedResponseBody", decryptedResponseBody);
		logger.info("-------------AES Decryption Completed : " + decryptedResponseBody);
	}
}