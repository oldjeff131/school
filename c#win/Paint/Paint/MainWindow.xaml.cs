using System;
using System.Windows;
using System.Windows.Controls;
using System.Windows.Data;
using System.Windows.Forms;
using System.Windows.Input;
using System.Windows.Media;
using System.Windows.Media.Imaging;
using System.Windows.Shapes;
namespace Paint
{
    /// <summary>
    /// MainWindow.xaml 的互動邏輯
    /// </summary>
    public partial class MainWindow : Window
    {
        private Color currentStrokeColor, currentFillColor;
        private Brush currentStrokeBrush = new SolidColorBrush(Colors.Red);
        private Brush currentFillBrush = new SolidColorBrush(Colors.Yellow);
        private string currentShape;
        private bool isFill = true;
        private string currentAction;
        private double currentthinkness;
        Point start, end;
        public MainWindow()
        {
            InitializeComponent();
        }

        private void colorbutton_Click(object sender, RoutedEventArgs e) //顏色
        {
            currentStrokeColor = GetDialogColor();
            currentStrokeBrush = new SolidColorBrush(currentStrokeColor); //設定之後的筆色
            colorbutton.Background = currentStrokeBrush; //改變colorbutton的背景顏色
            xylabel.Content = "填滿色彩:" + currentStrokeColor.ToString();
        }

    private void Canvas_MouseDown(object sender, MouseButtonEventArgs e)
    {
        start = e.GetPosition(canvas);//設定開始位子點
        canvas.Cursor = System.Windows.Input.Cursors.Pen; //設定在canvas上移動時，滑鼠會變筆
        xylabel.Content = $"座標點:({start})-({end})";
    }

    private void canvas_MouseMove(object sender, System.Windows.Input.MouseEventArgs e)
    {
        switch (currentAction)
        {
            case "Draw":
                if (e.LeftButton == MouseButtonState.Pressed)
                {
                    end = e.GetPosition(canvas); //設定結束位子點
                    canvas.Cursor = System.Windows.Input.Cursors.Pen;
                    xylabel.Content = $"座標點:({start})-({end})";
                }
                if (currentShape == "Freeline") //自由畫圖
                    DrawFreeline();
                break;
            case "Erase": //橡皮擦
                var selectedShape = e.OriginalSource as Shape;
                canvas.Children.Remove(selectedShape);
                if (canvas.Children.Count == 0) //當canvas上沒有圖時變成箭頭
                canvas.Cursor = System.Windows.Input.Cursors.Arrow;
                break;
        }
    }

    private void canvas_MouseUp(object sender, MouseButtonEventArgs e)
    {
        switch (currentShape) //判斷按鈕的名子
        {
            case "Line": //linebutton 
                Drawline();
                break;
            case "Ellipse": //ellipsebutton 
                DrawEllipse();
                break;
            case "Rectangle": //rectanglebutton 
                DrawRectangle();
                break;
            case "Freeline": //Freelinebutton 
                DrawFreeline();
                break;
        }
    }

    private void DrawFreeline() //自由繪畫
    {
            Drawline();
            start = end;
        }

        private void DrawRectangle() //長方形
        {
            Rectangle newRectangle = new Rectangle()
            {
                Stroke = currentStrokeBrush,
                StrokeThickness = currentthinkness,
                Width = Math.Abs(start.X - end.X), //X的開始值與X的結束值的距離，math.ads是求絕對值
            Height = Math.Abs(start.Y - end.Y) //Y的開始值與Y的結束值的距離，math.ads是求絕對值
            };
            if (isFill) newRectangle.Fill = currentFillBrush;
            Canvas.SetTop(newRectangle, start.Y); //設Y在canvas的頂點位子
        Canvas.SetLeft(newRectangle, start.X); //設X在canvas的頂點位子
        canvas.Children.Add(newRectangle);
            canvas.Cursor = System.Windows.Input.Cursors.Arrow;
        }

        private void DrawEllipse() //橢圓
        {
            Ellipse newEllipse = new Ellipse()
            {
                Stroke = currentStrokeBrush,
                StrokeThickness = currentthinkness,
                Width = Math.Abs(start.X - end.X), //X的開始值與X的結束值的距離，math.ads是求絕對值
                Height = Math.Abs(start.Y - end.Y) //Y的開始值與Y的結束值的距離，math.ads是求絕對值
            };
            if (isFill) newEllipse.Fill = currentFillBrush;
            Canvas.SetTop(newEllipse, start.Y); //設Y在canvas的頂點位子
            Canvas.SetLeft(newEllipse, start.X); //設X在canvas的頂點位子
            canvas.Children.Add(newEllipse);
            canvas.Cursor = System.Windows.Input.Cursors.Arrow;
        }

        private void Drawline() //直線
        {
            Line newLine = new Line()
            {
                Stroke = currentStrokeBrush,
                StrokeThickness = currentthinkness,
                X1 = start.X, //設定開始的X值
                Y1 = start.Y, //設定開始的Y值
                X2 = end.X, //設定結束的X值
                Y2 = end.Y //設定結束的Y值
            };
            canvas.Children.Add(newLine);
            canvas.Cursor = System.Windows.Input.Cursors.Arrow;
        }

        private void clearbutton_Click(object sender, RoutedEventArgs e)
        {
            canvas.Children.Clear(); //清除畫面所有的圖畫
        }

        private void Fillcolorbutton_Click(object sender, RoutedEventArgs e) //填滿色彩
        {
            isFill = !isFill;
            if (isFill)
            {
                Fillcolorbutton.Content = "填滿色彩";
                currentFillColor = GetDialogColor();
                currentFillBrush = new SolidColorBrush(currentFillColor); //紀錄填滿色彩的顏色代號
            Fillcolorbutton.Background = currentFillBrush; //改變button的顏色
            xylabel.Content = "填滿色彩:" + currentFillColor.ToString(); //顯示顏色代號
            }
            else //當不填滿色彩
            {
                Fillcolorbutton.Content = "不填滿色彩";
                Fillcolorbutton.Background = new SolidColorBrush
               (Colors.LightGray); //不顯示顏色
                xylabel.Content = "不填滿色彩";
            }

        }

        private Color GetDialogColor()
        {
            ColorDialog colorDialog = new ColorDialog();
            colorDialog.ShowDialog();
            System.Drawing.Color dlgColor = colorDialog.Color;
            return Color.FromArgb(dlgColor.A, dlgColor.R, dlgColor.G,dlgColor.B);//建立color結構
        }

        private void erasebutton_Click(object sender, RoutedEventArgs e) //抹去團案
        {
            currentAction = "Erase";
            if (canvas.Children.Count != 0)
                canvas.Cursor = System.Windows.Input.Cursors.Hand;
            xylabel.Content = "抹去繪圖物件";
        }
        private void Window_Loaded(object sender, RoutedEventArgs e)
        {
            sl2.Minimum = 0; //設定slider資料
            sl2.Maximum = 20;
            sl2.Width = 100;
            sl2.IsSnapToTickEnabled = true;
            sl2.Value = 1;
            var mybinding = new System.Windows.Data.Binding("Value");
            mybinding.Source = sl2;
            BindingOperations.SetBinding(lb2, ContentProperty, mybinding);
            sl1.Minimum = 0; //建立於menu上的slider資料
            sl1.Maximum = 20;
            sl1.Width = 100;
            sl1.IsSnapToTickEnabled = true;
            sl1.Value = 1;
            var hebinding = new System.Windows.Data.Binding("Value");
            hebinding.Source = sl1;
            BindingOperations.SetBinding(lb1, ContentProperty, hebinding);
            sl3.Minimum = 0; //建立於右鍵的slider資料
            sl3.Maximum = 20;
            sl3.Width = 100;
            sl3.IsSnapToTickEnabled = true;
            sl3.Value = 1;
            var shebinding = new System.Windows.Data.Binding("Value");
            shebinding.Source = sl3;
            BindingOperations.SetBinding(lb3, ContentProperty, shebinding);
        }

        private void sliderthinkness_ValueChanged(object sender,RoutedPropertyChangedEventArgs<double> e) //讀取所有slider的資料
        {
            var btn = sender as System.Windows.Controls.Slider;
            currentthinkness = Convert.ToInt32(btn.Value);
        }

        private void MenuItem_Click(object sender, RoutedEventArgs e)
        {
            RenderTargetBitmap rtb = new RenderTargetBitmap((int)
            canvas.RenderSize.Width, (int)canvas.RenderSize.Height, 96d, 65d, System.Windows.Media.PixelFormats.Default);
            rtb.Render(canvas);
            var crop = new CroppedBitmap(rtb, new Int32Rect(0, 0, 1240,570));//設定列印尺寸
            BitmapEncoder pngEncoder = new PngBitmapEncoder();
            pngEncoder.Frames.Add(BitmapFrame.Create(crop));
            using (var fs = System.IO.File.OpenWrite("4a830212hw6.png")) //建立檔案以及存檔名
            {
                pngEncoder.Save(fs);
            }
        }

        private void shapebutton_Chick(object sender, RoutedEventArgs e)
        {
            var btn = sender as System.Windows.Controls.RadioButton;
            currentShape = btn.Content.ToString(); //將按鈕的名子帶入currentshape變數裡
            currentAction = "Draw";
            xylabel.Content = "畫" + currentShape;
        }
    }
}