using DBMS_Lab.Models;
using Microsoft.Data.SqlClient;
using System;
using System.Collections.Generic;
using System.Data;
using System.Text;

namespace DBMS_Lab.Repositories
{
    public class SQLAdminRepository : IAdminRepository
    {
        public DataTable GetAllAdmins()
        {
            string connString = SQLUtility.GetConnectionString();
            string selectAdminsString = $"SELECT * FROM Admins";

            using SqlConnection conn = new SqlConnection(connString);

            SqlDataAdapter selectUsersAdapter = new SqlDataAdapter(selectAdminsString, conn);

            DataSet adminsDataFromDB = new DataSet(); // all the tables will be put in this DataSet

            conn.Open();

            selectUsersAdapter.Fill(adminsDataFromDB, "Admins"); // fill data from DB and load it into the internal table "Admins"

            return adminsDataFromDB.Tables["Admins"];
        }
    }
}