using System.Collections.Generic;
using System.Globalization;
using System.IO;
using System.Linq;
using System.Text;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Controls.Primitives;
using System.Windows.Data;
using System.Windows.Documents;
using System.Windows.Media;
using CsvHelper;
using Microsoft.Win32;

namespace Drinks_order
{
    /// <summary>
    /// MainWindow.xaml 的互動邏輯
    /// </summary>
    public partial class MainWindow : Window
    {
        private string takeout = "";
        List<Drink> drinks = new List<Drink>(); //建立 List 
        List<OrderItem> Order = new List<OrderItem>();
        List<person> Person = new List<person>();
        public MainWindow()
        {
            InitializeComponent();
        }
        private void windows1_Loaded(object sender, RoutedEventArgs e)
        {
            OpenFileDialog openFileDialog = new OpenFileDialog();
            openFileDialog.DefaultExt = ".csv"; //設定要取得的資料副檔名
            openFileDialog.Filter = "CSV files|*.csv|HTML Files|*.html|Text Flies | *.txt | All Files | *.* "; //決定出現在找尋欄中[另存檔案類型]或[檔案類型] 方塊的選項
            if (openFileDialog.ShowDialog() == true)
            {
                string path = openFileDialog.FileName;
                using (var reader = new StreamReader(path, Encoding.Default))
                using (var csv = new CsvReader(reader,CultureInfo.InvariantCulture))
                {
                    drinks = csv.GetRecords<Drink>().ToList(); //將檔案轉成drinks list 的資料
                }
            }
            GenerateMenu(drinks);//建立
        }
        private void RB_Checked(object sender, RoutedEventArgs e)//確認是否要內用與外帶
        {
            RadioButton rb = sender as RadioButton;
            if (rb.IsChecked == true)
                takeout = rb.Content.ToString();
            if (RB1.IsChecked == true)
                textblock.Background = Brushes.Orange;
            else if (RB2.IsChecked == true)
                textblock.Background = Brushes.YellowGreen;
        }
        private void GenerateMenu(List<Drink> mydrink) //建立slider
        {
            foreach (Drink d in mydrink)
            {
                var sp = new StackPanel();
                var cb = new CheckBox();
                var sl = new Slider();
                var lb = new Label();
                cb.Content = d.Name + d.Size + d.Price; //設定label的文字
                sl.Minimum = 0; //設定slider資料
                sl.Maximum = 10;
                sl.Width = 250;
                sl.TickPlacement = TickPlacement.BottomRight;
                sl.IsSnapToTickEnabled = true;
                sl.Value = 1;
                lb.Width = 30;
                sp.Orientation = Orientation.Horizontal;
                sp.Children.Add(cb);
                sp.Children.Add(sl);
                sp.Children.Add(lb);
                sp_menu.Children.Add(sp);
                Binding mybinding = new Binding("Value");
                mybinding.Source = sl;
                BindingOperations.SetBinding(lb, ContentProperty, mybinding);
            }
        }
        private void Button_Click(object sender, RoutedEventArgs e)
        {
            int total = 0;
            double selltotal = 0.0;
            string sellinfo = "";
            Order.Clear();
            textblock.Text = "";
            for (int i = 0; i < sp_menu.Children.Count; i++)
            {
                var sp = sp_menu.Children[i] as StackPanel;
                var cb = sp.Children[0] as CheckBox;
                var sl = sp.Children[1] as Slider;
                int quantity = (int)sl.Value;
                if ((cb.IsChecked == true) && (quantity != 0))
                {
                    int index = i;
                    var drink = drinks[i];
                    Order.Add(new OrderItem()
                    {
                        Index = index,Quantity = quantity,
                        SubTotal = drink.Price * quantity
                    });//將勾選資料放進Order list
                }
            }
            if (Order.Count == 00)//判斷是否有訂購
                textblock.Inlines.Add("請繼續訂購!");
            else
            {
                textblock.Inlines.Add("你要 ");
                textblock.Inlines.Add(new Run(takeout)
                {
                    Foreground = Brushes.Red
                });
                textblock.Inlines.Add("飲料，訂單清單如下：\n");
                for (int i = 0; i < Order.Count; i++) //列印有勾選的飲品訂單在textblock裡
                {
                    var orderitem = Order[i];
                    var drink = drinks[orderitem.Index];
                    total += orderitem.SubTotal;
                    textblock.Inlines.Add($"第{i + 1}項：{drink.Name + drink.Size}{ orderitem.Quantity}杯，每杯{ drink.Price}元，總共{ orderitem.SubTotal}元\n");
                    Person.Add(new person() { Name = drinks[Order[i].Index].Name, Size = drinks[Order[i].Index].Size, Num = Order[i].Quantity, Price = drinks[Order[i].Index].Price, total = Order[i].SubTotal });
                }
            }
            if (total >= 500) //檢查是否有打折
            {
                selltotal = total * 0.8;
                sellinfo = "超過500元打8折，";
            }
            else if (total >= 300)
            {
                selltotal = total * 0.85;
                sellinfo = "超過300元打85折，";
            }
            else if (total >= 200)
            {
                selltotal = total * 0.9;
                sellinfo = "超過200元打9折，";
            }
            else selltotal = total;
            textblock.Inlines.Add($"總價{total}元，{sellinfo}售價");
            textblock.Inlines.Add(new Run(selltotal.ToString())
            {
                FontSize = 14,
                FontWeight = FontWeights.Bold
            });
            textblock.Inlines.Add(" 元。");
            using (var writer = new StreamWriter("F:\\4a830212.txt")) //把訂單資料儲存到指定的位子跟.txt檔
            using (var csv = new CsvWriter(writer, CultureInfo.InvariantCulture))
            {
                csv.WriteRecords(Person);//檔案內容
            }
        }
        class person //建檔的list
        {
            public string Name { get; set; }
            public string Size { get; set; }
            public int Num { get; set; }
            public int Price { get; set; }
            public int total { get; set; }
        }

    }
}



