using System;
using System.Collections.Generic;
using System.Text;

namespace DBMS_Lab.Models
{
    public class Client
    {
        public int CID { get; set; }
        public string Name { get; set; }
        public string PhoneNumber { get; set; }
        public int Points { get; set; }
        public int AssignedAdmin { get; set; }

        public Client(int cid, string name, string phoneNumber, int points, int admin)
        {
            CID = cid;
            Name = name;
            PhoneNumber = phoneNumber;
            Points = points;
            AssignedAdmin = admin;
            
        }
    }
}
