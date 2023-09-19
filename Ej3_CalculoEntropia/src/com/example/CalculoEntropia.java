package com.example;

import java.io.*;
import java.nio.charset.StandardCharsets;
import java.util.Scanner;
import java.util.zip.ZipEntry;
import java.util.zip.ZipInputStream;
import java.util.HashMap;

public class CalculoEntropia {
    public static void main(String[] args) {
        Scanner scan=new Scanner(System.in);
        int opcion;
        int longitudCadena=0;
        float entropia=0;
        HashMap<Character,Integer> apariciones=new HashMap<>();
        try{

            System.out.print("\n\tQue desea leer? \n\t(1) .txt\n\t(2) .zip\n\tIngrese una opcion: ");
            opcion=scan.nextInt();
            if(opcion==1)
            {
                FileInputStream fs_txt= new FileInputStream("src\\data\\TXT.txt");
                longitudCadena=lecturaArchivo(apariciones,fs_txt);
                entropia=calcularEntropia(apariciones,longitudCadena);
                System.out.println("La entropia viendo los simbolos de la fuente en \"forma independiente\" es de: " + entropia+" bits");
            }
            else if(opcion==2)
            {
                unZip("src\\data\\TXT.zip","src\\data\\TxtUnzip");
                FileInputStream fs_zip=new FileInputStream("src\\data\\TxtUnzip\\TXT.txt");
                longitudCadena=lecturaArchivo(apariciones,fs_zip);
                entropia=calcularEntropia(apariciones,longitudCadena);
                System.out.println("\nLa entropia viendo los simbolos de la fuente en \"forma independiente\" es de: " + entropia+" bits");
            }
            else
                System.out.println("Haga las cosas bien! :p");

            System.out.println("\nLa entropia maxima es: "+entropiaMaxima(apariciones)+" bits");
            System.out.println("\nLa redundancia es: "+ (1 - entropia/entropiaMaxima(apariciones))+" bits");

        }
        catch(FileNotFoundException e){
            e.printStackTrace();
        }
        catch(IOException e){
            e.printStackTrace();
        }
    }
    public static void unZip(String path_zip, String path_unzip_txt){
        byte[] buffer = new byte[1024];
        try {
            File folder = new File(path_unzip_txt);
            if (!folder.exists()) {
                folder.mkdir();
            }
            ZipInputStream zis = new ZipInputStream(new FileInputStream(path_zip));
            ZipEntry ze = zis.getNextEntry();
            while (ze != null) {
                String nombreArchivo = ze.getName();
                File archivoNuevo = new File(path_unzip_txt + File.separator + nombreArchivo);
                System.out.println("archivo descomprimido : " + archivoNuevo.getAbsoluteFile());
                new File(archivoNuevo.getParent()).mkdirs();
                FileOutputStream fos = new FileOutputStream(archivoNuevo);
                int len;
                while ((len = zis.read(buffer)) > 0) {
                    fos.write(buffer, 0, len);
                }
                fos.close();
                ze = zis.getNextEntry();
            }
            zis.closeEntry();
            zis.close();
            System.out.println("Listo");
        } catch (IOException ex) {
            ex.printStackTrace();
        }
    }
    public static int lecturaArchivo(HashMap<Character,Integer> apariciones,FileInputStream fs_txt) throws IOException{

        byte[] bytes=fs_txt.readAllBytes();
        int cantSimbolos=0;
        String str=new String(bytes, StandardCharsets.US_ASCII);
        System.out.println("\n\n"+str);

        for(char c: str.toCharArray()){
            cantSimbolos++;
            if(!apariciones.containsKey(c))
            {
                apariciones.put(c,1);
            }
            else{
                apariciones.put(c,apariciones.get(c)+1);
            }
        }

        for(Character c: apariciones.keySet()){
            System.out.println("\n"+c+": "+apariciones.get(c));
        }

        return cantSimbolos;
    }
    public static int entropiaMaxima(HashMap<Character,Integer> apariciones){
        return (int)(Math.log10(apariciones.size())/Math.log10(2));
    }
    public static float calcularEntropia(HashMap<Character,Integer> apariciones,int longitudCadena){
        float entropia=0;
        float valor;
        for (Character c: apariciones.keySet()){
            valor=apariciones.get(c);
            entropia-= valor/longitudCadena*
                    (Math.log10(1/(1/(valor/longitudCadena)))/Math.log10(2));
        }

        return entropia;
    }
}
