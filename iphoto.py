
# -*- coding: utf-8 -*-


import os
import tkinter
# from tkinter import ttk
import tkinter.filedialog
from PIL import Image
from PIL import ImageTk
import message


fonts = '微软雅黑', 10
window = tkinter.Tk()

menumodel = 'normal'
filename = ''
_fullsize = ''


def NewFolder():
	folder = './Photos'
	os.mkdir(folder,)


def windowSize():
	window.title(' ')
	window.geometry('680x500')
	window.geometry('+400+150')
	# window.attributes('-alpha', 0.9)
	window.iconbitmap('./iphoto_icon.ico')


def fullScreen():
	global _rawphoto
	window.attributes('-toolwindow', False, 
					  '-alpha', 1.0, 
					  '-fullscreen', True, 
					  '-topmost', True)

	rawphoto = Image.open(filename, 'r')

	_rawphoto = ImageTk.PhotoImage(rawphoto)
	box.config(image=_rawphoto)


def imageBox():
	global box
	box = tkinter.Label(window, text='Photos', 
						anchor='center',width=1920, 
						height=1080, bg='#d3d3d3',
						fg='gray', font=('Arial', 40),  
						image=None)
	box.pack()


class MenuBar(object):
	def __init__(self, menubar=None, _window=None):       
		self.menubar = tkinter.Menu(window)
		self._window = window.config(menu=self.menubar)

	def photoBar(self):
		photo = tkinter.Menu(self.menubar, tearoff=0)
		photo.add_command(label='About...', 
						  command=message.MessageBox.aboutPhotos,
						  font=(fonts))
		self.menubar.add_cascade(label=' Photos ', 
								 menu=photo)
	def fileBar(self):
		fileoption = tkinter.Menu(self.menubar, 
								  tearoff=0)
		
		fileoption.add_command(label=' 新建文件 ', 
							   accelerator='Ctrl+N',
							   command=newImage,
							   font=(fonts))

		fileoption.add_command(label=' 打开图片... ', 
							   accelerator='Ctrl+O', 
							   command=openDialog, 
							   font=(fonts))

		fileoption.add_command(label=' 保存图片 ', 
							   accelerator='Ctrl+S',
							   command=saveAsPhoto,
							   state=menumodel, 
							   font=(fonts))
		fileoption.add_separator()
		fileoption.add_command(label=' 退出 ', 
							   command=quit, 
							   font=(fonts))

		self.menubar.add_cascade(label=' 文件 ', 
								 menu=fileoption)
	def editBar(self):
		editoption = tkinter.Menu(self.menubar, tearoff=0)
		editoption.add_command(label=' 撤销 ', 
							   accelerator='Ctrl+Z',
							   state=menumodel, 
							   font=(fonts))

		editoption.add_command(label=' 重做 ', 
							   accelerator='Ctrl+Y',
							   state=menumodel, 
							   font=(fonts))

		editoption.add_separator()
		editoption.add_command(label=' 剪切 ', 
							   accelerator='Ctrl+X',
							   state=menumodel, 
							   font=(fonts))

		editoption.add_command(label=' 复制 ', 
							   accelerator='Ctrl+C',
							   state=menumodel, 
							   font=(fonts))
		
		editoption.add_command(label=' 粘贴 ', 
							   accelerator='Ctrl+V',
							   state=menumodel, 
							   font=(fonts))

		self.menubar.add_cascade(label=' 编辑 ', 
								 menu=editoption)
	def imageBar(self):
		image = tkinter.Menu(self.menubar, tearoff=0)

		_filter = tkinter.Menu(image, tearoff=0)
		_filter.add_command(label=' 自然 ',
							command=natureImage,  
							font=(fonts))
		_filter.add_command(label=' 高斯模糊 ',  
							font=(fonts))

		_filter.add_command(label=' 查找边缘 ', 
							font=(fonts))
		_filter.add_separator()
		_filter.add_command(label=' 边缘增强 ',  
							font=(fonts))

		_filter.add_command(label=' 锐化 ',  
							font=(fonts))
		image.add_cascade(label=' 图像滤镜... ', 
						  font=(fonts),
						  menu=_filter)

		_color = tkinter.Menu(image, tearoff=0)
		_color.add_command(label=' 自然 ',
							command=natureImage, 
							font=(fonts))
		_color.add_command(label=' 变暗 ',  
						   font=(fonts))
		_color.add_command(label=' 变亮 ', 
						   font=(fonts))
		_color.add_separator()
		_color.add_command(label=' 反色 ',  
						   font=(fonts))

		_color.add_command(label=' 灰度填充 ',
						   command=photoGray,  
						   font=(fonts))
		image.add_cascade(label=' 图像色彩... ',
						  font=(fonts), 
						  menu=_color)
		self.menubar.add_cascade(label=' 图像 ', menu=image)

	def viewBar(self):
		view = tkinter.Menu(self.menubar, tearoff=0)
		view.add_command(label=' 图片放大 ', 
						 command=Zoom.zoomIn,
						 font=(fonts))
		view.add_command(label=' 图片缩小 ',
						 command=Zoom.zoomOut,
						 font=(fonts))
		view.add_command(label=' 实际大小 ',
						 command=Zoom.fullSize,  
						 font=(fonts))
		self.menubar.add_cascade(label=' 查看 ', 
								 menu=view)
	def windowBar(self):
		_window = tkinter.Menu(self.menubar, tearoff=0)
		_window.add_command(label=' 800x600 ',
							font=(fonts))
		_window.add_command(label=' 1200x800 ', 
							font=(fonts))
		_window.add_command(label=' 1920x1080 ', 
							font=(fonts))
		_window.add_command(label=' 全屏 ', 
							command=fullScreen,
							font=(fonts))
		self.menubar.add_cascade(label=' 窗口 ', 
								 menu=_window)
	def helpBar(self):
		_window = tkinter.Menu(self.menubar, tearoff=0)
		_window.add_command(label=' Help... ', 
							font=(fonts))
		self.menubar.add_cascade(label=' 帮助 ', 
								 menu=_window)
def openDialog():
	menumodel = 'normal'
	global filename
	filename = tkinter.filedialog.askopenfilename(title='Open Photos',
												  filetypes=[
												  ('All Files', '*'),
												  ('Photos', '*.jpg *.png')])

	openPhoto(filename)


def saveAsDialog():
	global filename
	saveasimage = tkinter.filedialog.asksaveasfilename(title='Mojave 图片保存为', 
													   initialdir=r'C:\ Mojave', 
													   filetypes=[('All Files', '*'), 
													   ('Photos', '*.jpg *.png')], 
													   initialfile='', 
													   defaultextension='.jpg')

	filename = saveasimage


def openPhoto(photoname):
	global _photo

	if photoname == '':
		photoname = None
	else:
		photo = Image.open(photoname, 'r')
		photo_width, photo_height = photo.size
		
		if photo_height > 500:
			newsize = photo.\
			resize(PhotoResize(photo_width, 
				   photo_height, 680, 500))
			_photo = ImageTk.PhotoImage(newsize)
		else:
			_photo = ImageTk.PhotoImage(photo)

		box.config(image=_photo)
		# photo.show()


def saveAsPhoto():
	saveAsDialog()


def PhotoResize(photo_width, photo_height, 
				box_width, box_height):

	box_width = box_width / photo_width
	box_height = box_height / photo_height
	min_size = min(box_width, box_height)
	_width = int(min_size * photo_width)
	_height = int(min_size * photo_height)

	return _width, _height


class Zoom(object):
	def fullSize(self): 
		global _fullsize
		if filename != '':
			fullphoto = Image.open(filename, 'r')
			actualw, actualh = fullphoto.size
			_fullsize = ImageTk.PhotoImage(fullphoto)
			box.config(image=_fullsize)

	def zoomIn(self):
		global zoomin
		if filename != '':
			former = Image.open(filename, 'r')
			width, height = former.size
			if _fullsize != '':
				enlarge = former.resize((int(width / 0.9), 
								   		 int(height / 0.9)))

				zoomin = ImageTk.PhotoImage(enlarge)
				box.config(image=zoomin)
			else:
				enlarge = former.resize((int(width / 1.5), 
								   		 int(height / 1.5)))

				zoomin = ImageTk.PhotoImage(enlarge)
				box.config(image=zoomin)

	def zoomOut(self):
		global zoomout
		if filename != '':
			unmodify = Image.open(filename, 'r')
			width, height = unmodify.size
			narrow = unmodify.resize((int(width / 2.4), 
								 	  int(height / 2.4)))

			zoomout = ImageTk.PhotoImage(narrow)
			box.config(image=zoomout)


def photoGray():
	global _grayphoto  
	grayphoto = Image.open(filename, 'r').convert('L')
	photo_width, photo_height = grayphoto.size
	# grayphoto.save(filename)
	graysize = grayphoto.resize(PhotoResize(photo_width, 
					   			photo_height, 680, 500))
	_grayphoto = ImageTk.PhotoImage(graysize)
	box.config(image=_grayphoto)
	# grayphoto.show()


def natureImage():
	global nature
	photo = Image.open(filename, 'r')
	photo_width, photo_height = photo.size

	newsize = photo.resize(PhotoResize(
						   photo_width, 
						   photo_height, 
						   680, 500))

	nature = ImageTk.PhotoImage(newsize)
	box.config(image=nature)


def newImage(red=255, green=200, blue=100):
	global _new
	newimage = Image.new('RGB', (1920, 1080),(red, green, blue))   
	_new = ImageTk.PhotoImage(newimage)
	box.config(image=_new)
	# newimage.show()


if __name__ == '__main__':
	windowSize()
	imageBox()
	MenuBar = MenuBar()
	Zoom = Zoom()
	MenuBar.photoBar()
	MenuBar.fileBar()
	MenuBar.editBar()
	MenuBar.imageBar()
	MenuBar.viewBar()
	MenuBar.windowBar()
	MenuBar.helpBar()

	window.mainloop()

