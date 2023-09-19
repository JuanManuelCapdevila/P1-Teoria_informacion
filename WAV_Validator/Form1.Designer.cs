namespace WAV_Validator
{
    partial class Form1
    {
        /// <summary>
        /// Variable del diseñador necesaria.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Limpiar los recursos que se estén usando.
        /// </summary>
        /// <param name="disposing">true si los recursos administrados se deben desechar; false en caso contrario.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Código generado por el Diseñador de Windows Forms

        /// <summary>
        /// Método necesario para admitir el Diseñador. No se puede modificar
        /// el contenido de este método con el editor de código.
        /// </summary>
        private void InitializeComponent()
        {
            this.button_open_file = new System.Windows.Forms.Button();
            this.text_header = new System.Windows.Forms.TextBox();
            this.button_show_header = new System.Windows.Forms.Button();
            this.label1 = new System.Windows.Forms.Label();
            this.button_exit = new System.Windows.Forms.Button();
            this.SuspendLayout();
            // 
            // button_open_file
            // 
            this.button_open_file.Location = new System.Drawing.Point(85, 87);
            this.button_open_file.Name = "button_open_file";
            this.button_open_file.Size = new System.Drawing.Size(75, 23);
            this.button_open_file.TabIndex = 1;
            this.button_open_file.Text = "Validar";
            this.button_open_file.UseVisualStyleBackColor = true;
            this.button_open_file.Click += new System.EventHandler(this.button_open_file_Click);
            // 
            // text_header
            // 
            this.text_header.Location = new System.Drawing.Point(240, 87);
            this.text_header.Multiline = true;
            this.text_header.Name = "text_header";
            this.text_header.ReadOnly = true;
            this.text_header.Size = new System.Drawing.Size(160, 157);
            this.text_header.TabIndex = 5;
            // 
            // button_show_header
            // 
            this.button_show_header.Location = new System.Drawing.Point(70, 145);
            this.button_show_header.Name = "button_show_header";
            this.button_show_header.Size = new System.Drawing.Size(105, 23);
            this.button_show_header.TabIndex = 6;
            this.button_show_header.Text = "Mostrar Cabecera";
            this.button_show_header.UseVisualStyleBackColor = true;
            this.button_show_header.Click += new System.EventHandler(this.button_show_header_Click);
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Location = new System.Drawing.Point(167, 28);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(76, 13);
            this.label1.TabIndex = 0;
            this.label1.Text = "WAV Validator";
            // 
            // button_exit
            // 
            this.button_exit.Location = new System.Drawing.Point(85, 204);
            this.button_exit.Name = "button_exit";
            this.button_exit.Size = new System.Drawing.Size(75, 23);
            this.button_exit.TabIndex = 8;
            this.button_exit.Text = "Salir";
            this.button_exit.UseVisualStyleBackColor = true;
            this.button_exit.Click += new System.EventHandler(this.button_exit_Click);
            // 
            // Form1
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(6F, 13F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(481, 307);
            this.Controls.Add(this.button_exit);
            this.Controls.Add(this.button_show_header);
            this.Controls.Add(this.text_header);
            this.Controls.Add(this.button_open_file);
            this.Controls.Add(this.label1);
            this.MaximizeBox = false;
            this.Name = "Form1";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "WAV Validator";
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion
        private System.Windows.Forms.Button button_open_file;
        private System.Windows.Forms.TextBox text_header;
        private System.Windows.Forms.Button button_show_header;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Button button_exit;
    }
}

