from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your id"
# Your Auth Token from twilio.com/console
auth_token  = "Your authentication"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+Your phone number",
    from_="+sending phone from twilio",
    body="Hello\nMessage seny from program!")

print(message.sid)
