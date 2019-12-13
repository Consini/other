//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace Chapter3
//{
//    class Cpoint
//    {
//        private double x;//坐标x轴的值
//        public double X
//        {
//            get { return x; }
//            set { x = value; }
//        }
//        private double y;//坐标y轴的值
//        public double Y
//        {
//            get { return y; }
//            set { y = value; }
//        }
//        public Cpoint()
//        {
//            this.X = 0;
//            this.Y = 0;
//        }
//        public Cpoint(double x, double y)
//        {
//            this.X = x;
//            this.Y = y;
//        }
//    }
//    class Cline : Cpoint
//    {
//        private Cpoint a = new Cpoint();//直线的一个端点
//        public Cpoint A
//        {
//            get { return a; }
//            set { a = value; }
//        }
//        private Cpoint b = new Cpoint();//直线的另一个端点
//        public Cpoint B
//        {
//            get { return b; }
//            set { b = value; }
//        }
//        public Cline(double a1, double a2, double b1, double b2)
//        {
//            A.X = a1;
//            A.Y = a2;
//            B.X = b1;
//            B.Y = b2;
//        }
//        //求直线长度
//        public double GetLength()
//        {
//            double m = A.X - B.X;
//            double n = A.Y - B.Y;
//            return Math.Sqrt(Math.Pow(m, 2) + Math.Pow(n, 2));
//        }
//    }
//    class Crect : Cpoint
//    {
//        private Cpoint a = new Cpoint();//矩形的一个端点
//        public Cpoint A
//        {
//            get { return a; }
//            set { a = value; }
//        }
//        private Cpoint b = new Cpoint();//与a为对角的点
//        public Cpoint B
//        {
//            get { return b; }
//            set { b = value; }
//        }
//        public Crect(double a1, double a2, double b1, double b2)
//        {
//            A.X = a1;
//            A.Y = a2;
//            B.X = b1;
//            B.Y = b2;
//        }
//        //求周长
//        public double GetLength()
//        {
//            double m = Math.Abs(A.X - B.X);
//            double n = Math.Abs(A.Y - B.Y);
//            return 2.0 * (m + n);
//        }
//        //求面积
//        public double GetArea()
//        {
//            double m = Math.Abs(A.X - B.X);
//            double n = Math.Abs(A.Y - B.Y);
//            return m * n;
//        }
//    }
//    class Test5
//    {
//        static void Main(string[] args)
//        {
//            Cpoint cpoint = new Cpoint(3, 9);
//            Console.WriteLine("点的坐标为 ({0},{1})", cpoint.X, cpoint.Y);
//            //定义一条直线
//            Cline cline = new Cline(1,1,5,5);
//            Console.WriteLine("直线的长度为 {0}", cline.GetLength());
//            //定义一个矩形
//            Crect crect = new Crect(1,2,4,4);
//            Console.WriteLine("矩形的周长为 {0},面积为 {1}", crect.GetLength(), crect.GetArea());
//            Console.ReadLine();
//        }
//    }
//}
