import tkinter as tk
from tkinter import filedialog, messagebox
import cv2 as cv
from PIL import Image, ImageTk

class App:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.window.geometry('1000x600')
        # Add a menubar
        self.main_menu = tk.Menu(window)
        # Add file submenu
        self.file_menu = tk.Menu(self.main_menu, tearoff=0)
        self.file_menu.add_command(label='開啟檔案', command=self.open_file)
        self.file_menu.add_command(label='儲存檔案', command=self.save_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label='離開程式', command=window.quit)
        # Add operation submenu
        self.operation_menu = tk.Menu(self.main_menu, tearoff=0)
        # Add submenu to mainmenu
        self.main_menu.add_cascade(label='檔案', menu=self.file_menu)
        self.main_menu.add_cascade(label='功能', menu=self.operation_menu)
        # display menu
        self.window.config(menu=self.main_menu, cursor='circle')
        # add a video source
        self.video_source = video_source
        # open video source
        self.vid = MyVideoCapture(self.video_source)
        # create a canvas to display the video content
        self.canvas = tk.Canvas(window, width=self.vid.width, height=self.vid.height)
        self.canvas.pack()
        # create a button to capture the frame
        self.btn_snapshot = tk.Button(window, text='snapshot', width='50', command=self.snapshot)
        self.btn_snapshot.pack(anchor=tk.CENTER, expand=True)
        self.delay = 15
        self.update()
        self.window.mainloop()
    def open_file(self):
        filetypes = (
            ('jpg files', '*.jpg'),
            ('png files', '*.png'),
            ('All files', '*.*')
        )
        filename = filedialog.askopenfilename(
            title='Open a file',
            initialdir='/',
            filetypes=filetypes
        )
        # messagebox.showinfo(title='Selected file', message=filename)
        img = cv.imread(filename)
        cv.imshow(filename, img)
        cv.waitKey()
    def save_file(self):
        pass
    def update(self):
        # get a frame from the video source
        ret, frame = self.vid.get_frame()
        if ret:
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame))
            self.canvas.create_image(0, 0, image=self.photo, anchor=tk.NW)
        self.window.after(self.delay, self.update)
    def snapshot(self):
        # get a frame from video source
        ret, frame = self.vid.get_frame()
        if ret:
            cv.imwrite('test.jpg', cv.cvtColor(frame, cv.COLOR_RGB2BGR))

class MyVideoCapture:
    def __init__(self, video_source=0):
        self.vid = cv.VideoCapture(video_source)
        if not self.vid.isOpened():
            raise ValueError('Unable to open video source', video_source)
        self.width = self.vid.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv.CAP_PROP_FRAME_HEIGHT)
    def get_frame(self):
        if self.vid.isOpened():
            ret, frame = self.vid.read()
            if ret:
                return ret, cv.cvtColor(frame, cv.COLOR_BGR2RGB)
            else:
                return ret, None

App(tk.Tk(), 'OpenCv with Tkinter GUI')