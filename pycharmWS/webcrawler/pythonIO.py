import os

fopen = 'F:/pythonTest/Hello.txt'
f = open(fopen)
print(f.read())                                                                                                 # 直接读取，这样其实不太好，如果文件大小为 10G ，那内存就爆了

print(os.name)                                                                                              # nt 为 Window 系统，posix 为 Linux、OS 操作系统
# print(os.uname())  os.uname()在 window 系统上不存在
print(os.environ)
# environ({'C_EM64T_REDIST11': 'C:\\Program Files (x86)\\Common Files\\Intel\\Shared Files\\cpp\\',
#  'HOMEPATH': '\\Users\\Administrator',
#  'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', '
# PROGRAMFILES(X86)': 'C:\\Program Files (x86)',
# 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files',
#  'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 58 Stepping 9, GenuineIntel',
#  'MGLS_LICENSE_FILE': 'D:\\MentorGraphics\\LICENSE.TXT',
#  'PYTHONUNBUFFERED': '1',
#  'SDD_DOC_UTILS': 'doc_utils',
#  'SDD_VLPERL_BIN': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\perl\\bin',
# 'SDD_DX': 'dx',
# 'SDD_WDBSERVER_HOME': 'd:\\MentorGraphics\\9.5PADS\\MGC_HOME.ixn\\lib',
# 'SDD_MGC_HOME': '..\\MGC_HOME.ixn',
#  'PATH': 'F:\\Python27\\;F:\\Python27\\Scripts;C:\\Program Files (x86)\\Common Files\\Intel\\Shared Files\\cpp\\bin\\Intel64;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Program Files\\Java\\jdk1.8.0_91\\\\lib;C:\\Program Files\\Java\\jdk1.8.0_91\\\\bin;d:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\bin;d:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\lib;d:\\MentorGraphics\\9.5PADS\\MGC_HOME.ixn\\bin;d:\\MentorGraphics\\9.5PADS\\MGC_HOME.ixn\\lib;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;d:\\MentorGraphics\\9.5PADS\\SDD_HOME\\CAMCAD;C:\\Cadence\\Orcad_9.2.3\\tools\\Capture;C:\\Cadence\\Orcad_9.2.3\\tools\\bin;C:\\Cadence\\Orcad_9.2.3\\tools\\jre\\bin;C:\\Cadence\\Orcad_9.2.3\\tools\\fet\\bin;C:\\Cadence\\Orcad_9.2.3\\tools\\specctra\\bin;F:\\android-ndk64-r10b-windows-x86_64\\android-ndk-r10b;F:\\Python27;F:\\python35;F:\\python35\\Scripts;D:\\android-ndk-r10;F:\\xpl_err\\mysql-5.6.30-winx64\\mysql-5.6.30-winx64\\bin;F:\\python35\\Scripts\\;F:\\python35\\', 'SDD_LOCAL': 'C:\\ProgramData\\mgc\\win32\\9.5PADS', 'SDD_TRN': 'translators', 'SDD_ICDB': 'iCDB', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'PADS_ROOT': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME',
#  'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files',
# 'NUMBER_OF_PROCESSORS': '4',
# 'DX_ROOT': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\sim\\DxSim\\',
# 'SDD_START': 'start',
# 'NDK_ROOT': 'F:\\android-ndk64-r10b-windows-x86_64\\android-ndk-r10b', 'SDD_WV': 'wv', 'SDD_CES': 'ces', 'PROCESSOR_LEVEL': '6', 'SDD_LM': 'lm', 'USERPROFILE': 'C:\\Users\\Administrator', 'PADS_PROGRAMS': 'Programs', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'MGC_IO_DESIGNER_HOME': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\IODesigner', 'SDD_HOME': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME', 'SDD_HLX': 'hlx', 'PYTHONPATH': 'F:\\pycharmWS', 'ALLUSERSPROFILE': 'C:\\ProgramData', 'COMPUTERNAME': 'MY8866', 'WINDIR': 'C:\\Windows', 'TOMCAT_HOME': 'E:\\xpl\\apache-tomcat-7.0.69-windows-x64\\apache-tomcat-7.0.69', 'JAVA_HOME': 'C:\\Program Files\\Java\\jdk1.8.0_91\\', 'OS': 'Windows_NT', 'SDD_IOD': 'IODesigner', 'VBOX_MSI_INSTALL_PATH': 'D:\\Program Files\\Oracle\\VirtualBox\\', 'SDD_HLT': 'hlt', 'SDD_STARTBAT': 'start /b /wait', 'USERDOMAIN': 'MY8866', 'HYP_HOME': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\hyperlynx', 'WF_CLASSPATH': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\lib', 'SDD_VERSION': '9.5PADS', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_HOSTED': '1', 'PROCESSOR_REVISION': '3a09', 'SDD_SIM': 'sim', 'ELDO_FLOW': 'sim', 'SDD_COMMON_BIN': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\bin', 'WDIR': 'd:\\PADS Projects;d:\\MentorGraphics\\9.5PADS\\SDD_HOME\\standard', 'SDD_DXSIM': 'dxsim', 'PYTHONIOENCODING': 'UTF-8', 'CDS_LIC_FILE': 'C:\\Cadence\\Orcad_9.2.3\\tools\\license.dat', 'SESSIONNAME': 'Console', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'SDD_VIEWER_HOME': 'd:\\MentorGraphics\\9.5PADS\\MGC_HOME.ixn\\lib', 'SDD_JAVA_HOME': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\jre\\default\\bin\\javaw.exe', 'CLASSPATH': '.;C:\\Program Files\\Java\\jdk1.8.0_91\\\\lib;C:\\Program Files\\Java\\jdk1.8.0_91\\\\lib\\dt.jar;C:\\Program Files\\Java\\jdk1.8.0_91\\\\lib\\tools.jar;C:\\Program Files\\Java\\jdk1.8.0_91\\\\lib\\tools.jar;', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'CDSROOT': 'C:\\Cadence\\Orcad_9.2.3', 'PROGRAMW6432': 'C:\\Program Files', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'MGC_HOME': 'd:\\MentorGraphics\\9.5PADS\\MGC_HOME.ixn', 'SDD_PADS': 'pads', 'MYSQL_HOME': 'F:\\xpl_err\\mysql-5.6.30-winx64\\mysql-5.6.30-winx64', 'LOGONSERVER': '\\\\MY8866', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'SDD_LM_BIN': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\lm\\win32\\bin', 'SDD_HSSD': 'hssd', 'PROGRAMFILES': 'C:\\Program Files', 'HOMEDRIVE': 'C:', 'PERLINTERP': 'd:\\MentorGraphics\\9.5PADS\\SDD_HOME\\common\\win32\\perl\\bin\\perl', 'SDD_PLATFORM': 'win32', 'FP_NO_HOST_CHECK': 'NO', 'SDD_WG': 'wg', 'ASL.LOG': 'Destination=file', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'LANG': 'zh_CN', 'SDD_VCD': 'camcad', 'USERNAME': 'Administrator', 'PROGRAMDATA': 'C:\\ProgramData', 'SYSTEMDRIVE': 'C:', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local'})
print(os.environ.get('PATH'))

print(os.path.abspath('.'))
print(os.path.join("F:/pycharmWS/webcrawler","testdir"))
# os.mkdir("F:/pycharmWS/webcrawler/testdir/file.txt")                          # F:/pycharmWS/webcrawler/testdir/file.txt

print([ x for x in os.listdir("F:/") if os.path.isfile(x) and os.path.splitext(x)[1]=='.py'])
L = []
def findAllFile(file):
     dir = os.listdir(file)
     print(dir)
     for x in dir :
          x = os.path.join(file,x)
          print(x)
          if os.path.isfile(x) :
               L.append(x)
          elif os.path.isdir(x):
               findAllFile(x)
          else:
               print('Sb')
findAllFile("F:/HQS/236")

for s in L:
     print(s)

