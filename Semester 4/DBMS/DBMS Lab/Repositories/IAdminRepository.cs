using DBMS_Lab.Models;
using System;
using System.Collections.Generic;
using System.Data;
using System.Text;

namespace DBMS_Lab.Repositories
{
    public interface IAdminRepository
    {
        public DataTable GetAllAdmins();
        //public void AddAdmin(string name, int releaseYear, float price, int tid, int pid);
        //public void RemoveAdmin(int aid);


    }
}
