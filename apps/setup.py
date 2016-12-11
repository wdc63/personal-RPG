from distutils.core import setup
import py2exe
setup(windows=[{"script":"D:\MyRpg3\good\zhuchuangkou.py","icon_resources":[(1,"D:\MyRpg3\good\ico.ico")]}], options={"py2exe":{"includes":["sip","ftputil"]}})


###C:\Python34\dist下增加文件夹platforms，拷入qwindows.dll
###CMD在C:\python34目录运行 cd c:\python34
###然后运行python D:\MyRpg3\good\setup.py py2exe
###最终生成目录拷入msvcr100.dll和msvcp100.dll两个文件