//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace Test
//{
//    interface I1
//    {
//        void MyFunction1();
//    }
//    interface I2
//    {
//        void MyFunction2();
//    }
//    class Test : I1, I2
//    {
//        public void MyFunction1()
//        {
//            Console.WriteLine("Now I can say this here is I1 implemented!");
//        }
//        public void MyFunction2()
//        {
//            Console.WriteLine("Now I can say this here is I2 implemented!");
//        }
//    }
//    class PavelTeskov
//    {
//        static void Main(string[] args)
//        {
//            Test t = new Test();
//            t.MyFunction1();
//            t.MyFunction2();
//            Console.Read();
//        }
//    }
//}
