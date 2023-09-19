
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WAV_Validator
{
    public partial class Form1 : Form
    {
        Stream buffer = null;
        BinaryReader wav_file;
        bool is_wav = false;

        public Form1()
        {
            InitializeComponent();
        }

        private void button_open_file_Click(object sender, EventArgs e)
        {

            OpenFileDialog openFileDialog;
            byte[] bytes_read;

            openFileDialog = new OpenFileDialog();
            openFileDialog.InitialDirectory = "c:\\";
            openFileDialog.Filter = "All files (*.*)|*.*";
            openFileDialog.FilterIndex = 2;
            openFileDialog.RestoreDirectory = true;
            if (openFileDialog.ShowDialog() == DialogResult.OK)
            {
                //Read the contents of the file into a stream
                buffer = openFileDialog.OpenFile();
            }

            //Read the file
            wav_file = new BinaryReader(buffer);
            wav_file.BaseStream.Seek(0, SeekOrigin.Begin);//seek byte 0

            bytes_read = wav_file.ReadBytes(4); //reads 4 bytes
            String string_read_reef = ASCIIEncoding.ASCII.GetString(bytes_read);//Decode the bytes and reads "RIFF"

            wav_file.BaseStream.Seek(4, SeekOrigin.Current);
            bytes_read = wav_file.ReadBytes(4); //reads "WAVE"
            String string_read_wave = ASCIIEncoding.ASCII.GetString(bytes_read);

            bytes_read = wav_file.ReadBytes(4);//reads "fmt "
            String string_read_fmt = ASCIIEncoding.ASCII.GetString(bytes_read);

            wav_file.BaseStream.Seek(20, SeekOrigin.Current);
            bytes_read = wav_file.ReadBytes(4); //reads "data"
            String string_read_data = ASCIIEncoding.ASCII.GetString(bytes_read);

            if ((string_read_reef == "RIFF") && (string_read_wave == "WAVE") && (string_read_fmt == "fmt ") && (string_read_data == "data"))
            {
                MessageBox.Show("Elemental, mi querido Watson, SI es un WAV");
                is_wav = true;
            }
            else
            {
                MessageBox.Show("Elemental, mi querido Watson, NO es un WAV");
                is_wav = false;
            }
        }

        private void button_show_header_Click(object sender, EventArgs e)
        {
            byte[] bytes_read;
            string final_string = "Header";
            int number;

            if (is_wav)
            {
                //reads the header
                wav_file.BaseStream.Seek(0, SeekOrigin.Begin);
                //wave
                wav_file.BaseStream.Seek(8, SeekOrigin.Current);
                bytes_read = wav_file.ReadBytes(4);
                final_string += "\r\n Format: " + ASCIIEncoding.ASCII.GetString(bytes_read);
                //audio format
                wav_file.BaseStream.Seek(8, SeekOrigin.Current);
                number = wav_file.ReadInt16(); //reads a 2 bytes integer
                if (number == 1)
                    final_string += "\r\n Audio Format: " + "PCM ";
                else
                    final_string += "\r\n Audio Format: " + number.ToString();

                //num channels
                number = wav_file.ReadInt16();
                if (number == 1)
                    final_string += "\r\n Number of channels: " + "Mono";
                else
                    final_string += "\r\n Number of channels: " + "Stereo";


                //sample rate
                number = wav_file.ReadInt32();
                final_string += "\r\n Sample rate: " + number.ToString() + " bits";

                //bits per sample
                wav_file.BaseStream.Seek(6, SeekOrigin.Current);
                number = wav_file.ReadInt16();
                final_string += "\r\n Bits per sample: " + number.ToString() + " ";

                text_header.Text = final_string;
            }
        }

        private void button_exit_Click(object sender, EventArgs e)
        {
            buffer.Close(); //close the file
            Application.Exit();
        }
    }

}

