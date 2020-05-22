import wget as wg
import os

#Links#

#Debug soft
ProcessHackerUrl = 'https://netcologne.dl.sourceforge.net/project/processhacker/processhacker2/processhacker-2.39-bin.zip'
AutorunsUrl = 'http://download.sysinternals.com/files/Autoruns.zip'
UnlockerUrl = 'https://140200.pro/wp-content/uploads/2018/03/Unlocker1.9.2.zip'

#Cleaning and optimization soft
CCleanerUrl = 'https://download.ccleaner.com/ccsetup566.exe'
PrivazerUrl = 'https://privazer.com/PrivaZer.exe'
Win_10_TweakerUrl = 'https://dl7.softportal.org/b5/8/9/04714ef7e11c1cd867e7f04598905cb9/Win_10_Tweaker.exe'

#Needed soft
qBittorentUrl = 'https://download.fosshub.com/Protected/expiretime=1590031500;badurl=aHR0cHM6Ly93d3cuZm9zc2h1Yi5jb20vcUJpdHRvcnJlbnQuaHRtbA==/0886b787f9250127afdaf539596534900c2ae3f43392c43e333d13799c5fb8bc/5b8793a7f9ee5a5c3e97a3b2/5ea3901c069b6080f700f0d2/qbittorrent_4.2.5_x64_setup.exe'
K_Lite_CodecUrl = 'https://files3.codecguide.com/K-Lite_Codec_Pack_1548_Mega.exe'
Zip7Url = 'https://www.7-zip.org/a/7z1900-x64.exe'
WinRarUrl = 'https://www.rarlab.com/rar/winrar-x64-590.exe'

#Hardware debug soft
FurmarkUrl = 'http://www.geeks3d.com/downloads/2018/FurMark_1.20.0.1_Setup.exe'
CpuZUrl = 'https://140200.pro/wp-content/uploads/2018/02/cpu-z_1.83-en.zip'
GpuZUrl = 'https://dl7.softportal.org/b0/5/3/46e611ad793c149e241b77927924974f/GPU-Z.2.31.0.exe'

#Browsers
GoogleUrl = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B01D5ECF0-1C5D-00ED-59C7-6DC9A9C1C228%7D%26lang%3Dru%26browser%3D4%26usagestats%3D0%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'
MozilaUrl = 'https://dl7.softportal.org/b3/0/1/a4bf201c9db4b00fbbbeb7ca93fc1dbd/Firefox_Setup_76.0.1_x64.exe'

#Antiviruses
AvastUrl = 'https://install.avcdn.net/iavs9x/avast_free_antivirus_setup_online.exe'
Dr_webUrl = 'https://dl7.softportal.org/b6/9/0/beffd4064b7b347ada88381d1c02c092/drweb-12.0-av-win.exe'
EsetUrl = 'https://dl7.softportal.org/b3/6/9/8a4b618f5a55b996977b3af2c7af81c1/essf_trial_rus.exe'

#Other
SDIUrl = 'http://sdi-tool.org/releases/SDI_R2000.zip'

#######

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def CreatingDirs():

    try:
        os.makedirs('Installed soft/Debug soft')
        print("Directorys for debug soft created ")
    except FileExistsError:
        print("Directorys for debug soft already exists")

    try:
        os.makedirs('Installed soft/Cleaning and optimization soft')
        print("Directorys for cleaning and optimization soft created ")
    except FileExistsError:
        print("Directorys for cleaning and optimization soft already exists")

    try:
        os.makedirs('Installed soft/Needed soft')
        print("Directorys for needed soft created ")
    except FileExistsError:
        print("Directorys for needed soft already exists")

    try:
        os.makedirs('Installed soft/Hardware debug soft')
        print("Directorys for hardware debug soft created ")
    except FileExistsError:
        print("Directorys for hardware debug soft already exists")

    try:
        os.makedirs('Installed soft/Browsers')
        print("Directorys for browsers created ")
    except FileExistsError:
        print("Directorys for browsers already exists")

    try:
        os.makedirs('Installed soft/Other')
        print("Directorys for other created ")
    except FileExistsError:
        print("Directorys for other already exists")

    try:
        os.makedirs('Installed soft/Antiviruses')
        print("Directorys for antiviruses created ")
    except FileExistsError:
        print("Directorys for antiviruses already exists")



def MainMenu():
    cls()
    print("====Extra Soft Downloader====")
    print("==Version 1.1 by SNeicer==")
    print("1. Debug soft")
    print("2. Cleaning and optimization soft")
    print("3. Needed soft")
    print("4. Hardware debug soft")
    print("5. Browsers")
    print("6. Antiviruses")
    print("7. Other")

    UsrAnswMM = input("Enter number of needed category: ")
    if UsrAnswMM == '1':
        DebugSoft()
    elif UsrAnswMM == '2':
        CleaningAndOptimizationSoft()
    elif UsrAnswMM == '3':
        NeededSoft()
    elif UsrAnswMM == '4':
        HardwareDebugSoft()
    elif UsrAnswMM == '5':
        Browsers()
    elif UsrAnswMM == '6':
        Antiviruses()
    elif UsrAnswMM == '7':
        Other()
    else:
        print("Unknown number")
        MainMenu()
        UsrAnswMM = input("Enter number of needed category: ")

def DebugSoft():
    cls()
    print("====Debug soft====")
    print("1. Process hacker")
    print("2. Autoruns")
    print("3. Unlocker")
    print("0. Back to main menu")

    UsrAnswDebugS = input("Enter number of needed programm: ")

    if UsrAnswDebugS == '1':

        print("Downloading process hacker...")

        try:
            os.mkdir('Installed soft/Debug soft/Process hacker')
            print("Directory for process hacker created")
        except FileExistsError:
            print("Directory for process hacker already exists")

        wg.download(ProcessHackerUrl, 'Installed soft/Debug soft/Process hacker/')
        DebugSoft()

    elif UsrAnswDebugS == '2':

        print("Downloading autoruns...")

        try:
            os.mkdir('Installed soft/Debug soft/Autoruns')
            print("Directory for autoruns created")
        except FileExistsError:
            print("Directory for autoruns already exists")

        wg.download(AutorunsUrl, 'Installed soft/Debug soft/Autoruns/')
        DebugSoft()

    elif UsrAnswDebugS == '3':

        print("Downloading unlocker...")

        try:
            os.mkdir('Installed soft/Debug soft/Unlocker')
            print("Directory for unlocker created")
        except FileExistsError:
            print("Directory for unlocker already exists")

        wg.download(UnlockerUrl, 'Installed soft/Debug soft/Unlocker/')
        DebugSoft()

    elif UsrAnswDebugS == '0':
        MainMenu()

    else:
        print('Unknown number')
        DebugSoft()

def CleaningAndOptimizationSoft():
    cls()
    print("====Cleaning and optimization soft====")
    print("1. CCleaner")
    print("2. Privazer")
    print("3. Win 10 Tweaker (Only for windows 10!)")
    print("0. Back to main menu")

    UsrAnswCAOS = input("Enter number of needed programm: ")

    if UsrAnswCAOS == '1':

        print("Downloading CCleaner...")

        try:
            os.mkdir('Installed soft/Cleaning and optimization soft/CCleaner')
            print("Directory for CCleaner created")
        except FileExistsError:
            print("Directory for CCleaner already exists")

        wg.download(CCleanerUrl, 'Installed soft/Cleaning and optimization soft/CCleaner/')
        CleaningAndOptimizationSoft()

    elif UsrAnswCAOS == '2':

        print("Downloading Privazer...")

        try:
            os.mkdir('Installed soft/Cleaning and optimization soft/Privazer')
            print("Directory for Privazer created")
        except FileExistsError:
            print("Directory for Privazer already exists")

        wg.download(PrivazerUrl, 'Installed soft/Cleaning and optimization soft/Privazer/')
        CleaningAndOptimizationSoft()


    elif UsrAnswCAOS == '3':

        print("Downloading Win 10 Tweaker...")

        try:
            os.mkdir('Installed soft/Cleaning and optimization soft/Win 10 Tweaker')
            print("Directory for Win 10 Tweaker created")
        except FileExistsError:
            print("Directory for Win 10 Tweaker already exists")

        wg.download(Win_10_TweakerUrl, 'Installed soft/Cleaning and optimization soft/Win 10 Tweaker/')
        CleaningAndOptimizationSoft()

    elif UsrAnswCAOS == '0':
        MainMenu()

    else:
        print('Unknown number')
        CleaningAndOptimizationSoft()

def NeededSoft():
    cls()
    print("====Needed soft====")
    print("1. qBittorent")
    print("2. K-Lite Codec")
    print("3. 7 Zip")
    print("4. WinRar")
    print("0. Back to main menu")

    UsrAnswNS = input("Enter number of needed programm: ")

    if UsrAnswNS == '1':

        print("Downloading qBittorent...")

        try:
            os.mkdir('Installed soft/Needed soft/qBittorent')
            print("Directory for qBittorent created")
        except FileExistsError:
            print("Directory for qBittorent already exists")

        wg.download(qBittorentUrl, 'Installed soft/Needed soft/qBittorent/')
        NeededSoft()

    elif UsrAnswNS == '2':

        print("Downloading K-Lite Codec...")

        try:
            os.mkdir('Installed soft/Needed soft/K-Lite Codec')
            print("Directory for K-Lite Codec created")
        except FileExistsError:
            print("Directory for K-Lite Codec already exists")

        wg.download(K_Lite_CodecUrl, 'Installed soft/Needed soft/K-Lite Codec/')
        NeededSoft()


    elif UsrAnswNS == '3':

        print("Downloading 7 Zip...")

        try:
            os.mkdir('Installed soft/Needed soft/7 Zip')
            print("Directory for 7 Zip created")
        except FileExistsError:
            print("Directory for 7 Zip already exists")

        wg.download(Zip7Url, 'Installed soft/Needed soft/7 Zip/')
        NeededSoft()

    elif UsrAnswNS == '4':

        print("Downloading WinRar...")

        try:
            os.mkdir('Installed soft/Needed soft/WinRar')
            print("Directory for WinRar created")
        except FileExistsError:
            print("Directory for WinRar already exists")

        wg.download(WinRarUrl, 'Installed soft/Needed soft/WinRar/')
        NeededSoft()

    elif UsrAnswNS == '0':
        MainMenu()

    else:
        print('Unknown number')
        NeededSoft()

def HardwareDebugSoft():
    cls()
    print("====Needed soft====")
    print("1. Furmark")
    print("2. CpuZ")
    print("3. GpuZ")
    print("0. Back to main menu")

    UsrAnswHDu = input("Enter number of needed programm: ")

    if UsrAnswHDu == '1':

        print("Downloading Furmark...")

        try:
            os.mkdir('Installed soft/Hardware debug soft/Furmark')
            print("Directory for Furmark created")
        except FileExistsError:
            print("Directory for Furmark already exists")

        wg.download(FurmarkUrl, 'Installed soft/Hardware debug soft/Furmark/')
        HardwareDebugSoft()

    elif UsrAnswHDu == '2':

        print("Downloading CpuZ...")

        try:
            os.mkdir('Installed soft/Hardware debug soft/CpuZ')
            print("Directory for CpuZ created")
        except FileExistsError:
            print("Directory for CpuZ already exists")

        wg.download(CpuZUrl, 'Installed soft/Hardware debug soft/CpuZ/')
        HardwareDebugSoft()

    elif UsrAnswHDu == '3':

        print("Downloading GpuZ...")

        try:
            os.mkdir('Installed soft/Hardware debug soft/GpuZ')
            print("Directory for GpuZ created")
        except FileExistsError:
            print("Directory for GpuZ already exists")

        wg.download(GpuZUrl, 'Installed soft/Hardware debug soft/GpuZ/')
        HardwareDebugSoft()

    elif UsrAnswHDu == '0':
        MainMenu()

    else:
        print('Unknown number')
        HardwareDebugSoft()

def Browsers():
    cls()
    print("====Needed soft====")
    print("1. Google Chrome")
    print("2. Mozila Fire Fox")
    print("0. Back to main menu")

    UsrAnswBrow = input("Enter number of needed programm: ")

    if UsrAnswBrow == '1':

        print("Downloading Google Chrome...")

        try:
            os.mkdir('Installed soft/Browsers/Google Chrome')
            print("Directory for Google Chrome created")
        except FileExistsError:
            print("Directory for Google Chrome already exists")

        wg.download(GoogleUrl, 'Installed soft/Browsers/Google Chrome/')
        Browsers()

    elif UsrAnswBrow == '2':

        print("Downloading Mozila Fire Fox...")

        try:
            os.mkdir('Installed soft/Browsers/Mozila Fire Fox')
            print("Directory for Mozila Fire Fox created")
        except FileExistsError:
            print("Directory for Mozila Fire Fox already exists")

        wg.download(MozilaUrl, 'Installed soft/Browsers/Mozila Fire Fox/')
        Browsers()

    elif UsrAnswBrow == '0':
        MainMenu()

    else:
        print('Unknown number')
        Browsers()

def Antiviruses():
    cls()
    print("====Other====")
    print("1. Avast")
    print("2. Dr.Web")
    print("3. Eset Smart Security")
    print("0. Back to main menu")

    UsrAnswAnt = input("Enter number of needed programm: ")

    if UsrAnswAnt == '1':

        print("Downloading Avast...")

        try:
            os.mkdir('Installed soft/Antiviruses/Avast')
            print("Directory for Avast created")
        except FileExistsError:
            print("Directory for Avast already exists")

        wg.download(AvastUrl, 'Installed soft/Antiviruses/Avast/')
        Antiviruses()

    elif UsrAnswAnt == '2':

        print("Downloading Dr.web...")

        try:
            os.mkdir('Installed soft/Antiviruses/Dr.web')
            print("Directory for Dr.web created")
        except FileExistsError:
            print("Directory for Dr.web already exists")

        wg.download(Dr_webUrl, 'Installed soft/Antiviruses/Dr.web/')
        Antiviruses()

    elif UsrAnswAnt == '3':

        print("Downloading Eset Smart Security...")

        try:
            os.mkdir('Installed soft/Antiviruses/Eset Smart Security')
            print("Directory for Eset Smart Security created")
        except FileExistsError:
            print("Directory for Eset Smart Security already exists")

        wg.download(EsetUrl, 'Installed soft/Antiviruses/Eset Smart Security/')
        Antiviruses()

    elif UsrAnswAnt == '0':
        MainMenu()

def Other():
    cls()
    print("====Other====")
    print("1. SDI Driver pack")
    print("0. Back to main menu")

    UsrAnswOth = input("Enter number of needed programm: ")

    if UsrAnswOth == '1':

        print("Downloading SDI Driver pack...")

        try:
            os.mkdir('Installed soft/Other/SDI Driver pack')
            print("Directory for SDI Driver pack created")
        except FileExistsError:
            print("Directory for SDI Driver pack already exists")

        wg.download(SDIUrl, 'Installed soft/Other/SDI Driver pack/')
        Other()

    elif UsrAnswOth == '0':
        MainMenu()

    else:
        print('Unknown number')
        Other()

CreatingDirs()
MainMenu()



