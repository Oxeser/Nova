# Nova - Ethical Hacking Toolkit

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![License](https://img.shields.io/badge/License-Educational%20Use%20Only-red)
![Status](https://img.shields.io/badge/Status-Beta-orange)

## Tanıtım

**Nova**, çeşitli protokolleri hedef alan sızma testleri, güvenlik analizleri ve eğitim amaçlı saldırı senaryoları gerçekleştirmek için geliştirilmiş çok yönlü bir araç setidir.

### Dahili Modüller

- **BruteX**  
  SSH, FTP, SFTP, FTPS, POP3, IMAP, MySQL ve RDP servislerine yönelik gelişmiş brute-force saldırıları düzenler. Proxy desteği ve detaylı loglama sistemiyle birlikte.

> Nova yalnızca **eğitimsel amaçlarla** ve **yetkili ortamlarda** kullanılmalıdır. İzinsiz kullanımlar yasaları ihlal eder.

---

## BruteX Özellikleri

- SSH, FTP, SFTP, FTPS, POP3, IMAP, MySQL ve RDP brute-force
- SOCKS5 proxy desteği (RDP hariç)
- Gecikme (delay) ve loglama özelliği
- Tek kullanıcı veya kullanıcı listesi desteği

---

## Kurulum

```bash
git clone https://github.com/kullaniciadi/nova.git
cd nova
pip install -r requirements.txt
python3 Nova.py
