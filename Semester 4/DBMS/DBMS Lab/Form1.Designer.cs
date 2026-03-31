namespace DBMS_Lab
{
    partial class Form1
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            AdminsDataGridView = new DataGridView();
            ConnectToDBButton = new Button();
            ClientsDataGridView = new DataGridView();
            ((System.ComponentModel.ISupportInitialize)AdminsDataGridView).BeginInit();
            ((System.ComponentModel.ISupportInitialize)ClientsDataGridView).BeginInit();
            SuspendLayout();
            // 
            // AdminsDataGridView
            // 
            AdminsDataGridView.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            AdminsDataGridView.Location = new Point(55, 136);
            AdminsDataGridView.Name = "AdminsDataGridView";
            AdminsDataGridView.RowHeadersWidth = 82;
            AdminsDataGridView.Size = new Size(751, 485);
            AdminsDataGridView.TabIndex = 0;
            // 
            // ConnectToDBButton
            // 
            ConnectToDBButton.Location = new Point(55, 52);
            ConnectToDBButton.Name = "ConnectToDBButton";
            ConnectToDBButton.Size = new Size(296, 46);
            ConnectToDBButton.TabIndex = 1;
            ConnectToDBButton.Text = "Connect to Database";
            ConnectToDBButton.UseVisualStyleBackColor = true;
            ConnectToDBButton.Click += connectToDatabaseButton_Click;
            // 
            // ClientsDataGridView
            // 
            ClientsDataGridView.ColumnHeadersHeightSizeMode = DataGridViewColumnHeadersHeightSizeMode.AutoSize;
            ClientsDataGridView.Location = new Point(876, 136);
            ClientsDataGridView.Name = "ClientsDataGridView";
            ClientsDataGridView.RowHeadersWidth = 82;
            ClientsDataGridView.Size = new Size(834, 485);
            ClientsDataGridView.TabIndex = 2;
            ClientsDataGridView.CellContentClick += ClientsDataGridView_CellContentClick;
            // 
            // Form1
            // 
            AutoScaleDimensions = new SizeF(13F, 32F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(2174, 698);
            Controls.Add(ClientsDataGridView);
            Controls.Add(ConnectToDBButton);
            Controls.Add(AdminsDataGridView);
            Name = "Form1";
            Text = "Form1";
            Load += Form1_Load;
            ((System.ComponentModel.ISupportInitialize)AdminsDataGridView).EndInit();
            ((System.ComponentModel.ISupportInitialize)ClientsDataGridView).EndInit();
            ResumeLayout(false);
        }

        #endregion

        private DataGridView AdminsDataGridView;
        private Button ConnectToDBButton;
        private DataGridView ClientsDataGridView;
    }
}
