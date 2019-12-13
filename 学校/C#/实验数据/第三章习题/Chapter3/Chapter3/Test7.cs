//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;
//namespace Chapter3
//{
//    public class CStrOne
//    {
//        protected string m_str1 = string.Empty;
//        public CStrOne(string str1)
//        {
//            this.m_str1 = str1;
//        }
//        public void ShowStringOne()
//        {
//            Console.WriteLine(m_str1);
//        }
//    }
//    public class CStrTwo : CStrOne
//    {
//        private string m_str2 = string.Empty;
//        public CStrTwo(string str, string str2) : base(str)
//        {
//            this.m_str2 = str2;
//        }
//        public void ShowStringTwo()
//        {
//            Console.WriteLine("{0}{1}", m_str1, m_str2);
//        }
//    }
//    class Test7
//    {
//        static void Main(string[] args)
//        {
//            CStrOne cs1 = new CStrOne("we need to ");
//            cs1.ShowStringOne();
//            CStrTwo cs2 = new CStrTwo("we need to ", "change our world.");
//            cs2.ShowStringTwo();
//            Console.Read();
//        }
//    }
//}
