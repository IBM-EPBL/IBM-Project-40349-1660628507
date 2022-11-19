import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import *
import base64

message = Mail()

to_email ='sasikala051982@gmail.com'
from_email ='mohanapriyav1101@gmail.com'
SENDGRID_API_KEY =("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"
)



message.to = [To(email = to_email, name="Sasikala" , p=0)]
message.from_email = From(email= from_email, name="SendGrid Demo Message", p=1)
message.subject=Subject("This si test email send by sendgrid")
message.content=[
    Content(
        mime_type="text/html",
        content="<p>Hello Dear,</p> <p>This is test email using <b> Sendgrid</b>.</p>",
    )
]

#send the attachment 
filename ="text.txt"
path = os.path.join(os.getcwd(), filename)


file= open(path, "rb")
content = base64.b64encode(file.read())
content = content.decode("utf-8")

message.attachment=[
    Attachment(
        file_content=FileContent(content),
        file_name=FileName(filename),
        file_type=FileType("text/txt"),
        disposition=Disposition("attachment"),
    )
]

sendgrid_client = SendGridAPIClient(SENDGRID_API_KEY)
response = sendgrid_client.send(message)

print(response.status_code)
print(response.body)
print(response.headers)

