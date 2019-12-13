//using System;
//using System.Collections.Generic;
//using System.Linq;
//using System.Text;
//using System.Threading.Tasks;

//namespace Test
//{
//    public class Digit
//    {
//        byte value;
//        public Digit(byte value)
//        {
//            if (value < 0 || value > 9)
//                throw new ArgumentException();
//            this.value = value;
//        }
//        //用户自定义从 Digit 到 byte 的转换 
//        public static implicit operator byte(Digit d)
//        {
//            return d.value;
//        }
//    }

//    class Digit
//    {
//    }
//}
