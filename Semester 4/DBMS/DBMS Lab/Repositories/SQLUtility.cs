using System;
using System.Collections.Generic;
using System.Text;

namespace DBMS_Lab.Repositories
{
    public static class SQLUtility
    {
        public static string GetConnectionString()
        {
            return "Data Source=" + Environment.MachineName + "\\SQLEXPRESS;Initial Catalog=GameStore;Integrated Security=true;TrustServerCertificate=true;";
        }
    }
}
