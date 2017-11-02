from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))
from_addr  ='1485072401@qq.com'
password = 'xzroswxqltgaggjf'
# 输入收件人地址:
#to_addr = 'gentlemen_zhang@163.com'
# 输入SMTP服务器地址:



def SendEmail(code,email):
    to_addr = email
    msg = MIMEText('hello,your code is ' + code, 'plain', 'utf-8')
    msg['From'] = _format_addr('GoodLand <%s>' % from_addr)
    msg['Subject'] = Header('来自CherryLand的注册验证码', 'utf-8').encode()
    server = smtplib.SMTP_SSL(host='smtp.qq.com', port=465)
    server.set_debuglevel(1)
    server.login(from_addr, password)
    server.sendmail(from_addr, [to_addr], msg.as_string())
    server.quit()