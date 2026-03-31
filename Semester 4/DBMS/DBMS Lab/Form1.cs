using DBMS_Lab.Repositories;

namespace DBMS_Lab
{
    public partial class Form1 : Form
    {
        private IAdminRepository AdminRepository { get; set; }
        public Form1()
        {
            AdminRepository = new SQLAdminRepository();
            InitializeComponent();
        }

        private void Form1_Load(object sender, EventArgs e)
        {

        }

        private void connectToDatabaseButton_Click(object sender, EventArgs e)
        {
            AdminsDataGridView.DataSource = AdminRepository.GetAllAdmins();
        }

        private void ClientsDataGridView_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }
    }
}
