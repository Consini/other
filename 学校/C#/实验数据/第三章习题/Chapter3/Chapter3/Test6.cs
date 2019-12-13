//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace Chapter3
//{
//    class CPerson
//    {
//        public string sName;
//        public string sNumber;
//        public string Sex;
//        public void Set()
//        {
//            Console.Write("姓名:");
//            this.sName = Console.ReadLine();
//            Console.Write("编号:");
//            this.sNumber = Console.ReadLine();
//            Console.Write("性别:");
//            this.Sex = Console.ReadLine();
//        }
//        public void Get()
//        {
//            Console.WriteLine();
//            Console.Write("姓名为:" + sName);
//            Console.Write("，编号为:" + sNumber);
//            Console.Write("，性别为:" + Sex);
//        }
//    }
//    class CStudent : CPerson
//    {
//        public float Score;
//        public new void Set()
//        {
//            Console.WriteLine("这是学生类！");
//            base.Set();
//            Console.Write("成绩为");
//            this.Score = Convert.ToInt32(Console.ReadLine());
//        }
//        public new void Get()
//        {
//            base.Get();
//            Console.WriteLine("，成绩为：" + Score);
//        }
//    }
//    class CTeacher : CPerson
//    {
//        public int age;
//        public new void Set()
//        {
//            Console.WriteLine("这是教师类!");
//            base.Set();
//            Console.Write("教龄为：");
//            this.age = Convert.ToInt32(Console.ReadLine());
//        }
//        public new void Get()
//        {
//            base.Get();
//            Console.WriteLine("，教龄为：" + age);
//        }
//    }
//    class Test6
//    {
//        static void Main(string[] args)
//        {
//            CStudent stu = new CStudent();
//            CTeacher tea = new CTeacher();
//            stu.Set();
//            stu.Get();
//            Console.WriteLine();
//            tea.Set();
//            tea.Get();
//            Console.ReadLine();
//        }
//    }
//}
