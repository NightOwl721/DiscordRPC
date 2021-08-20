import discord_rpc
import time
from win32gui import GetWindowText, GetForegroundWindow

if __name__ == '__main__':
    def readyCallback(current_user):
        print('Our user: {}'.format(current_user))

    def disconnectedCallback(codeno, codemsg):
        print('Disconnected from Discord rich presence RPC. Code {}: {}'.format(
            codeno, codemsg
        ))

    def errorCallback(errno, errmsg):
        print('An error occurred! Error {}: {}'.format(
            errno, errmsg
        ))

    # Note: 'event_name': callback
    callbacks = {
        'ready': readyCallback,
        'disconnected': disconnectedCallback,
        'error': errorCallback,
    }
    discord_rpc.initialize('877507145413849119', callbacks=callbacks, log=False)

    i = 0
    start = time.time()
    while i == 0:
        rpcapp = GetWindowText(GetForegroundWindow())
        rpcapp.replace("*", "")
        if rpcapp == "Task View":
            rpcapp == "Widok zadań"
        if rpcapp == "C:\WINDOWS\system32\cmd.exe":
            rpcapp = "Windows Command Procesor"

        discord_rpc.update_presence(
            **{
                
                'details': 'Apka: ' + rpcapp,
                'start_timestamp': start,
                'large_image_key': 'sowa'
            }
        )

        discord_rpc.update_connection()
        time.sleep(2)
        discord_rpc.run_callbacks()

    discord_rpc.shutdown()
