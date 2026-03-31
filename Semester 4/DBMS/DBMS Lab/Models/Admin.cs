using System;
using System.Collections.Generic;
using System.Text;

namespace DBMS_Lab.Models
{
    public class Admin
    {
        public int AID { get; set; }
        public string Name { get; set; }
        public string Email { get; set; }

        public Admin(int aid, string name, string email)
        {
            AID = aid;
            Name = name;
            Email = email;
        }


    }
}
