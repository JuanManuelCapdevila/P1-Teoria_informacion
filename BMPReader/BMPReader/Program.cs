using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.IO;

namespace BMPReader
{
	class Program
	{
		static void Main(string[] args)
		{
			String rutaArchivo = null, SignatureDecoded = null;
			byte[] Signature;
			int FileSize = 0, DataOffset = 0;
			try
			{
				Console.Write("Ingrese ruta del archivo .bmp: ");
				rutaArchivo = Console.ReadLine();
				BinaryReader bmpFile = new BinaryReader(File.OpenRead(rutaArchivo));
				bmpFile.BaseStream.Seek(0, SeekOrigin.Begin);   //Se posiciona el lector en el comienzo del archivo
				Signature = bmpFile.ReadBytes(2);       //Se leen los primero 2 Bytes del archivo
				SignatureDecoded = ASCIIEncoding.ASCII.GetString(Signature);    //Decodificación de los primeros 2 Bytes obtenidos
				if (SignatureDecoded.ToUpper() == "BM")            //Nos indica que el archivo es de formato BMP
				{
					FileSize = bmpFile.ReadInt32();         //Se leen los siguientes 4 Bytes referidos al tamño del archivo
					bmpFile.BaseStream.Seek(4, SeekOrigin.Current); //Se saltean los siguientes 4 bytes ya que no se utilizan
					DataOffset = bmpFile.ReadInt32();       //Se leen 4 bytes que indican donde comienzan los datos de la imagen
					bmpFile.Close();
					Console.WriteLine("\nSignature: " + SignatureDecoded +
										"\nFileSize: " + FileSize + " Bytes" +
										"\nDataOffset: " + DataOffset);
				}
				else Console.WriteLine("La ruta especificada no conduce a un archivo .bmp");
				
				
			}
			catch(IOException e)
			{
				Console.Error.WriteLine(e.Message);
			}
			catch(Exception e)
			{
				Console.Error.WriteLine(e.Message);
			}
			Console.ReadKey();
		}
	}
}
