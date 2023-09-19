package com.example;
import java.io.FileInputStream;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.charset.StandardCharsets;
import java.util.HashMap;

public class ArchivoWav {
    private static final HashMap<String, Integer> formatoWav=new HashMap<String,Integer>(13);
    //Big endian "b", Little endian "l"
    private static final char[] endian={'b','l','l','b','l','l','l','l','l','l','l','b','l','l'};
    public static void main(String[] args) {
        FileInputStream fs = null;
        inicializarFormatoWav();
        try {
            if(validarWav())
            {
                fs = new FileInputStream("src\\Datos\\gt40takingOff.wav");
                char c;
                //StringBuilder strCampo= new StringBuilder();

                int pos = 0;

                for (String key : formatoWav.keySet()) {
                    /*int i=0;
                    while(i < formatoWav.get(key))
                    {
                        c=(char) fs.read();
                        strCampo.append(c);
                        i++;
                    }*/

                    byte[] bytes=fs.readNBytes(formatoWav.get(key));

                    //mostrarDatos(strCampo, key, pos);
                    mostrarDatos(new String(bytes, StandardCharsets.US_ASCII), key, pos);
                    pos++;
                    //strCampo.setLength(0); //Limpiamos el StringBuilder
                }
            }
            else{
                System.out.println("Este no es un archivo WAV");
            }

        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try{
                if(fs!=null)
                    fs.close();
            }
            catch(IOException e){
                e.printStackTrace();
            }
        }
    }

    /**
     * El valor es la cantidad de Bytes del campo
     */
    public static void inicializarFormatoWav(){
        formatoWav.put("ChunkID",4);
        formatoWav.put("ChunkSize",4);
        formatoWav.put("Format",4);
        formatoWav.put("Subchunk1ID",4);
        formatoWav.put("Subchunk1Size",4);
        formatoWav.put("AudioFormat",2);
        formatoWav.put("NumChannels",2);
        formatoWav.put("SampleRate",4);
        formatoWav.put("ByteRate",4);
        formatoWav.put("BlockAlign",2);
        formatoWav.put("BitsPerSample",2);
        formatoWav.put("Subchunk2ID",4);
        formatoWav.put("Subchunk2Size",4);
    }
    /*public static void mostrarDatos(StringBuilder strCampo, String nombre,int pos){

        if(endian[pos]=='b')
            System.out.println("\n"+nombre+": "+ strCampo);
        else
            System.out.println("\n"+nombre+": "+strCampo.reverse());
    }*/
    public static void mostrarDatos(String strCampo, String nombre,int pos){

        if(endian[pos]=='b')
            System.out.println("\n"+nombre+": "+ strCampo);
        else
        {
            StringBuilder str= new StringBuilder(strCampo);
            System.out.println("\n"+nombre+": "+str.reverse());
        }
    }
    public static boolean validarWav() throws IOException {
        FileInputStream fs = null;
        StringBuilder strCampo= new StringBuilder();
        try{
            fs = new FileInputStream("C:\\Users\\users\\IdeaProjects\\PROGRAMACIÓN JAVA\\CódigoGENERAL\\lectura_archivos\\src\\Datos\\gt40takingOff.wav");
            int i=0;
            char c;
            while(i < formatoWav.get("ChunkID"))
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
        return strCampo.toString().equals("RIFF");
    }
}