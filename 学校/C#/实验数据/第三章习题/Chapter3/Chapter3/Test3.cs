//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace Chapter3
//{
//    class student
//    {
//        //字段定义
//        private string name; //姓名
//        private string no; //学号
//        private double engScore; //英语成绩
//        private double cScore; //C++成绩
//        private double mathScore; //数学成绩
//                                  //定义属性,通过属性访问、修改相应字段
//        public string Name
//        {
//            set { name = value; }
//            get { return name; }
//        }
//        public string No
//        {
//            set { no = value; }
//            get { return no; }
//        }
//        public double EngScore
//        {
//            set { engScore = value; }
//            get { return engScore; }
//        }
//        public double CScore
//        {
//            set { cScore = value; }
//            get { return cScore; }
//        }
//        public double MathScore
//        {
//            set { mathScore = value; }
//            get { return mathScore; }
//        }
//        //输入相应的数据
//        public void inputText()
//        {
//            Console.WriteLine("请输入姓名：");
//            Name = Console.ReadLine();
//            Console.WriteLine("请输入学号：");
//            No = Console.ReadLine();
//            Console.WriteLine("请输入英语成绩：");
//            EngScore = double.Parse(Console.ReadLine());
//            Console.WriteLine("请输入C++成绩：");
//            CScore = double.Parse(Console.ReadLine());
//            Console.WriteLine("请输入数学成绩：");
//            MathScore = double.Parse(Console.ReadLine());
//        }
//        //输出相应的数据
//        public void outputText()
//        {
//            Console.WriteLine("姓名为：{0}", Name);
//            Console.WriteLine("学号为：{0}", No);
//            Console.WriteLine("平均成绩为：{0}", avgScoreText());
//            Console.WriteLine("总成绩为：{0}", allScoreText());
//        }
//        //平均成绩
//        private double avgScoreText()
//        {
//            return (EngScore + CScore + MathScore) / 3;
//        }
//        //总成绩
//        private double allScoreText()
//        {
//            return EngScore + CScore + MathScore;
//        }
//    }
//    class Test3
//    {
//        static void Main(string[] args)
//        {
//            try
//            {
//                student t = new student();
//                t.inputText();
//                t.outputText();
//                Console.ReadLine();
//            }
//            catch (Exception ex)
//            {
//                Console.WriteLine(ex.Message.ToString());
//            }
//        }
//    }
//}
