package com.unam.ciencias.mx.myp;

import com.google.zxing.BarcodeFormat;
import com.google.zxing.WriterException;
import com.google.zxing.client.j2se.MatrixToImageWriter;
import com.google.zxing.common.BitMatrix;
import com.google.zxing.qrcode.QRCodeWriter;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) {
        QRCodeWriter writer = new QRCodeWriter();
        Scanner in = new Scanner(System.in);
        System.out.println("Ingrese el nombre para guardar como imagen su QR Code:");
        String name = in.nextLine();
        try {
            BitMatrix qrCode = writer.encode("https://web.fciencias.unam.mx/acceder", BarcodeFormat.QR_CODE, 800, 800);
            BufferedImage qrCodeBuffered = MatrixToImageWriter.toBufferedImage(qrCode);
            File qrCodeImage = new File(name+".png");
            ImageIO.write(qrCodeBuffered, "png", qrCodeImage);
        } catch (WriterException | IOException we) {
            System.err.println(we.getMessage());
        }
    }
}
