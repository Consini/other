using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Chapter3
{
    public class Complex
    {
        private double real;
        private double image;
        public Complex(double real, double image)
        {
            this.real = real;
            this.image = image;
        }
        public double Real
        {
            get
            {
                return real;
            }
            set
            {
                real = value;
            }
        }
        public double Image
        {
            get
            {
                return image;
            }
            set
            {
                image = value;
            }
        }
        public static Complex add(Complex c1, Complex c2)
        {
            return new Complex(c1.real + c2.real, c1.image + c2.image);
        }
        public static Complex sub(Complex c1, Complex c2)
        {
            return new Complex(c1.real - c2.real, c1.image - c2.image);
        }
        public static Complex mul(Complex c1, Complex c2)
        {
            return new Complex(c1.real * c2.real - c1.image * c2.image, c1.image * c2.real + c1.real * c2.image);
        }
        public static void print(Complex c)
        {
            Console.WriteLine("结果为： "+c.real + " + " + c.image + " i");
        }
    }
    class test1
    {
        static void Main(string[] args)
        {
            while (true)
            {
                Console.Write("输入<1>计算加法,<2>计算减法,<3>计算乘法,<0>退出：>>");             
                int i = int.Parse(Console.ReadLine());
                if(i == 0)
                {
                    Console.WriteLine("退出程序！");
                    break;                    
                }
                Console.Write("请输入第一个复数的实部：");
                double a = double.Parse(Console.ReadLine());
                Console.Write("请输入第一个复数的虚部：");
                double b = double.Parse(Console.ReadLine());
                Console.Write("请输入第二个复数的实部：");
                double c = double.Parse(Console.ReadLine());
                Console.Write("请输入第二个复数的虚部：");
                double d = double.Parse(Console.ReadLine());
                Complex m = new Complex(a, b);
                Complex n = new Complex(c, d);
                switch (i)
                {
                    case 1: Complex.print(Complex.add(m, n)); break;
                    case 2: Complex.print(Complex.sub(m, n)); break;
                    case 3: Complex.print(Complex.mul(m, n)); break;
                }               
            }
            Console.Read();
        }
    }
}
