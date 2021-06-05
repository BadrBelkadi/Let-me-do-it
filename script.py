import webbrowser
import time
import os


def run():
    # Path for the apps to run
    # Make sure you replace them with the path of the path you want to run
    To_do_List = r'C:\Users\"Badreddine Belkadi"\AppData\Local\Programs\todoist\Todoist.exe'

    Vs_Code = r'C:\Users\"Badreddine Belkadi"\AppData\Local\Programs\"Microsoft VS Code"\Code.exe'

    cmd = r'%windir%\system32\cmd.exe'

    # Commands to run in CMD
    run_td = f'start {To_do_List}'
    run_vs = f'start {Vs_Code}'
    run_cmd = f'start {cmd}'

    # Running the commands
    os.system(run_vs)
    time.sleep(1)
    os.system(run_cmd)
    time.sleep(1)
    os.system(run_td)
    time.sleep(1)

    # Websites to open on the browser
    # Add other websites you use on your daily routine
    Google = 'https://google.com/'
    E_mail = 'https://mail.google.com/mail/'
    Github = 'https://github.com/'
    Stackoverflow = 'https://stackoverflow.com'
    Spotify = 'https://open.spotify.com/'

    # Opening the websites
    webbrowser.open(Google)
    time.sleep(1)
    webbrowser.open_new_tab(E_mail)
    time.sleep(1)
    webbrowser.open_new_tab(Github)
    time.sleep(1)
    webbrowser.open_new_tab(Stackoverflow)
    time.sleep(1)
    webbrowser.open_new_tab(Spotify)

    # Open other websites using  webbrowser.open(Your_website)


if __name__ == '__main__':
    run()
