import sys
import socket
from datetime import datetime

portas_well_known = {
    "FTP (Data)": 20,
    "FTP (Controle)": 21,
    "SSH": 22,
    "Telnet": 23,
    "SMTP": 25,
    "DNS (Serviço de Nome de Domínio)": 53,
    "HTTP": 80,
    "HTTPS (TLS/SSL)": 443,
    "SNMP (Simple Network Management Protocol)": 161,
    "SNMP (Trap)": 162,
    "DHCP (Cliente)": 68,
    "DHCP (Servidor)": 67,
    "TFTP (Trivial File Transfer Protocol)": 69,
    "HTTP (Proxy)": 8080,
    "POP3 (Post Office Protocol - Versão 3)": 110,
    "IMAP (Internet Message Access Protocol)": 143,
    "LDAP (Lightweight Directory Access Protocol)": 389,
    "HTTPS (TLS/SSL) (Alternativo)": 8443,
    "Microsoft SMB": 445,
    "MySQL": 3306,
    "RDP (Remote Desktop Protocol)": 3389,
    "VNC (Virtual Network Computing)": 5900,
    "NTP (Network Time Protocol)": 123,
    "Syslog": 514,
    "AFP (Apple Filing Protocol)": 548,
    "PostgreSQL": 5432,
    "RADIUS (Remote Authentication Dial-In User Service)": 1812,
    "RADIUS (Accounting)": 1813,
    "LDAP (TLS/SSL)": 636,
    "Microsoft RPC": 135,
    "NetBIOS": 137,
    "NetBIOS Datagram Service": 138,
    "NetBIOS Session Service": 139,
    "ISAKMP/IPsec": 500,
    "L2TP (Layer 2 Tunneling Protocol)": 1701,
    "PPTP (Point-to-Point Tunneling Protocol)": 1723,
    "IMAPS (IMAP com TLS/SSL)": 993,
    "POP3S (POP3 com TLS/SSL)": 995,
}

def scan_ports(target, start_port, end_port, timeout):

    print("-" * 50)
    print("Varredura no Alvo: " + target)
    print("Varredura iniciada em:" + str(datetime.now()))
    print("-" * 50)

    try:
        for port in range(start_port, end_port + 1):
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(timeout)

            result = s.connect_ex((target, port))
            if result == 0:
                if port in portas_well_known.values():
                    print("Porta {} está aberta - {}".format(port, list(portas_well_known.keys())[list(portas_well_known.values()).index(port)]))
                else:
                    print("Porta {} está aberta".format(port))
            else:
                print("Porta {} - time out".format(port))

            s.close()

    except KeyboardInterrupt:
        print("\nPrograma encerrado")
        sys.exit()
    except socket.gaierror:
        print("\nNome do host não pôde ser resolvido")
        sys.exit()
    except socket.error as e:
        print("\nServidor não está respondendo: {}".format(e))
        sys.exit()

if __name__ == "__main__":
    target = input("Informe o nome do host ou o endereço IP do alvo: ")
    start_port = int(input("Informe a porta inicial: "))
    end_port = int(input("Informe a porta final: "))
    timeout = float(input("Informe o valor de timeout (em segundos): "))

    scan_ports(target, start_port, end_port, timeout)