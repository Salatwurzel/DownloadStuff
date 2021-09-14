import os

Sysupdate = False
GnomeSoftware = False
Mausbeschleunigung = False
DashToPanel = False
GoogleChrome = False
Piper = False
Steam = False
Lutris = False
GnomeTweaks = False
DevZeug = False

os.system("gsettings set org.gnome.shell.extensions.dash-to-dock click-action 'minimize'")

def ClearScreen():
    os.system("clear")

    print()
    print("####################")
    print("- Wurzelscript yo! -")
    print("####################")
    if Sysupdate == True:
        print ("Erfolg: Systemupdate komplett!")
    if GnomeSoftware == True:
        print ("Erfolg: Gnome-Software installiert!")
    if Mausbeschleunigung == True:
        print ("Erfolg: Mausbeschleunigung deaktiviert!")
    if DashToPanel == True:
        print ("Erfolg: Bessere Taskbar installiert!")
    if GoogleChrome == True:
        print ("Erfolg: Google-Chrome installiert!")
    if Piper == True:
        print ("Erfolg: Piper installiert!")
    if Steam == True:
        print("Erfolg: Steam installiert!")
    if Lutris == True:
        print ("Erfolg: Lutris installiert!")
    if GnomeTweaks == True:
        print ("Erfolg: Erweiterte Einstellungen installiert!")
    if DevZeug == True:
        print ("Erfolg: Entwicklerzeug installiert!")


######
# Sys-update
######
ClearScreen()
print()
if input(" > System updaten? [y, n]: ") == "y":
    os.system("sudo snap refresh")
    os.system("sudo apt update")
    os.system("sudo apt upgrade -y")
    Sysupdate = True

######
# Gnome-Software
######
ClearScreen()
print()
if input(" > Besseres Softwarecenter installieren? [y, n]: ") == "y":
    os.system("sudo apt-get install -y flatpak")
    os.system("sudo flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
    os.system("sudo snap remove snap-store")
    os.system("sudo apt-get install -y gnome-software-plugin*")
    os.system("gsettings set org.gnome.shell favorite-apps \"$(gsettings get org.gnome.shell favorite-apps | sed s/.$//), 'gnome-software.desktop']\"")
    GnomeSoftware = True

######
# Mausbeschleunigung
######
ClearScreen()
print()
print(" > Besser für Spiele: ")
if input(" > Mausbeschleunigung deaktivieren? [y, n]: ") == "y":
    os.system("gsettings set org.gnome.desktop.peripherals.mouse accel-profile 'flat'")
    Mausbeschleunigung = True

######
# Dash-to-Panel + ArcMenu
######
ClearScreen()
print()
if input(" > Bessere Taskbar installieren? [y, n]: ") == "y":
    os.system("sudo apt install -y chrome-gnome-shell")
    #Installiere extensions
    os.system("sudo apt install -y gnome-shell-extension-dash-to-panel")
    os.system("sudo apt install -y gnome-shell-extension-arc-menu")
    #Aktiviere extensions
    os.system("gnome-extensions enable dash-to-panel@jderose9.github.com")
    os.system("gnome-extensions enable arc-menu@linxgem33.com")
    #Konfiguriere DashToPanel
    os.system("gsettings set org.gnome.shell.extensions.dash-to-panel appicon-margin 4")
    os.system("gsettings set org.gnome.shell.extensions.dash-to-panel appicon-padding 2")
    os.system("gsettings set org.gnome.shell.extensions.dash-to-panel click-action 'TOGGLE-SHOWPREVIEW'")
    os.system("gsettings set org.gnome.shell.extensions.dash-to-panel panel-size 36")
    #Shell neustarten (ist nötig, aber ka warum)
    os.system("killall -3 gnome-shell")
    DashToPanel = True

######
# Besseres Design installieren
######
ClearScreen()
print()
if input("Besseres Design installieren? [y, n]: ") == "y":
    os.system("wget https://github.com/Salatwurzel/DownloadStuff/raw/master/Nordic-darker-standard-buttons.zip")
    os.system("mkdir ~/.themes")
    os.system("unzip Nordic-darker-standard-buttons.zip -d ~/.themes")
    os.system("gsettings set org.gnome.desktop.interface gtk-theme \"Nordic-darker-standard-buttons\"")

######
# Chrome
######
ClearScreen()
print()
if input(" > Google Chrome installieren? [y, n]: ") == "y":
    os.system("wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb")
    os.system("sudo dpkg -i google-chrome-stable_current_amd64.deb")
    os.system("rm google-chrome-stable_current_amd64.deb")
    os.system("")
    GoogleChrome = True

#######
# Piper
#######
ClearScreen()
print()
if input(" > Piper installieren? (für zB Logitech/Steelseries Mäuse) [y, n]: ") == "y":
    os.system("sudo apt install -y ratbagd piper")
    Piper = True

######
# Steam
######
ClearScreen()
print()
if input(" > Steam installieren? [y, n]: ") == "y":
    os.system("sudo apt install -y steam-installer")
    Steam = True

######
# Lutris
######
ClearScreen()
print()
if input(" > Lutris installieren (für Win-Games) [y, n]: ") == "y":
    os.system("sudo add-apt-repository ppa:lutris-team/lutris -y")
    os.system("sudo apt install lutris -y")
    Lutris = True

######
# Gnome-Tweaks
######
ClearScreen()
print()
if input(" > Gnome-Tweaks installieren (erweiterte Einstellungen) [y, n]: ") == "y":
    os.system("sudo apt install -y gnome-tweaks")
    GnomeTweaks = True

######
# DevZeug
######
ClearScreen()
print()
if input(" > Developer-Tools installieren? (.NET5/Java/VSCode usw) [y, n]: ") == "y":
    os.system("sudo apt install python-is-python3")
    #.NET5
    os.system("wget https://packages.microsoft.com/config/ubuntu/20.04/packages-microsoft-prod.deb -O packages-microsoft-prod.deb")
    os.system("sudo dpkg -i packages-microsoft-prod.deb")
    os.system("rm packages-microsoft-prod.deb")
    os.system("sudo apt update")
    os.system("sudo apt install -y apt-transport-https dotnet-sdk-5.0")
    #Java + GCC
    os.system("sudo apt install -y openjdk-11-jdk openjdk-16-jdk gcc make")
    #VSCode
    os.system("sudo snap install code --classic")
    DevZeug = True

#######
# Finished
########
ClearScreen()
print()
print("###################")
print("- Alles erledigt! -")
print("###################")
print()
