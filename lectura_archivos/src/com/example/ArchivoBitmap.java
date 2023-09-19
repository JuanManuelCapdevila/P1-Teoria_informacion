package com.example;

import java.io.FileInputStream;
import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;

public class ArchivoBitmap {
    private static final HashMap<String, Integer> formatoBMP=new HashMap<String,Integer>(15);
    public static void main(String[] args) {
        FileInputStream fs = null;
        inicializarFormatoBMP();
        try{
            if(validarBMP())
            {
                fs = new FileInputStream("src\\Datos\\example_small.bmp");
                char c;
                //StringBuilder strCampo= new StringBuilder();

                for (String key : formatoBMP.keySet()) {
                    /*int i=0;
                    while(i < formatoBMP.get(key))
                    {
                        c=(char) fs.read();
                        strCampo.append(c);
                        i++;
                    }
                    System.out.println("\n"+key+": "+ strCampo);
                    strCampo.setLength(0); //Limpiamos el StringBuilder
                    */
                    byte[] bytes=fs.readNBytes(formatoBMP.get(key));

                    System.out.println("\n"+key+": "+ new String(bytes, StandardCharsets.US_ASCII));
                }
            }
            else{
                System.out.println("Este no es un archivo BMP");
            }

        }
        catch(IOException e){
            e.printStackTrace();
        }
        finally{
            try{
                if(fs!=null)
                    fs.close();
            }
            catch (IOException e){
                e.printStackTrace();
            }
        }
    }
    public static void inicializarFormatoBMP(){
        formatoBMP.put("Signature",2);
        formatoBMP.put("FileSize",4);
        formatoBMP.put("Reserved",4);
        formatoBMP.put("Dataoffset",4);
        formatoBMP.put("Size",4);
        formatoBMP.put("Width",4);
        formatoBMP.put("Height",4);
        formatoBMP.put("Planes",2);
        formatoBMP.put("BitCount",2);
        formatoBMP.put("Compression",4);
        formatoBMP.put("ImageSize",4);
        formatoBMP.put("YPixelsPerM",4);
        formatoBMP.put("XPixelsPerM",4);
        formatoBMP.put("ColorsUsed",4);
        formatoBMP.put("ColorsImportant",4);
    }
    public static boolean validarBMP() throws IOException {
        FileInputStream fs = null;
        StringBuilder strCampo= new StringBuilder();
        try{
            fs = new FileInputStream("src\\Datos\\example_small.bmp");
            int i=0;
            char c;
            while(i < formatoBMP.get("Signature"))
            {
                c=(char) fs.read();
                strCampo.append(c);
                i++;
            }
        }
        catch (IOException e){
            e.printStackTrace();
        }
        finally {
            if(fs!=null)
                fs.close();
        }
        return strCampo.toString().equals("BM");
    }
}
