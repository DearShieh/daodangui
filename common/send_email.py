import smtplib
from email.mime.text import MIMEText
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart

class SendEmail:
    global send_user
    global email_host
    global password
    send_user = "tester_zx@163.com"
    email_host = "smtp.163.com"
    password = "SJDHDKXBYMSSKWCF"
    def send_email(self, user_list, sub, content, report_name):
        # 发件人
        user = "Carl" + "<" + send_user + ">"
        message = MIMEMultipart()
        message.attach(MIMEText(content, 'plain', 'utf-8'))

        # 添加附件
        with open(report_name, 'rb') as f:
            mime = MIMEBase('html', 'html', filename=report_name)  # 创建表示附件的MIMEBase对象，重新命名为test.png
            mime.add_header('Content-Disposition', 'attachment', filename='APIdaodangui_report.html')
            mime.set_payload(f.read())  # 读取附件内容
            mime.add_header('Content-ID', '<0>')
            mime.add_header('X-Attachment-Id', '0')
            encoders.encode_base64(mime)

        message['Subject'] = sub
        message['From'] = user
        message['To'] = ";".join(user_list)
        message.attach(mime)
        server = smtplib.SMTP()
        server.connect(email_host)
        server.login(send_user, password)
        server.sendmail(user, user_list, message.as_string())
        server.close()



# if __name__ == '__main__':
#     send = SendEmail()
#     user_list = ['zhilei@llzey.com']
#     sub = "接口自动化测试"
#     content = "hahh"
#     send.send_email(user_list, sub, content)