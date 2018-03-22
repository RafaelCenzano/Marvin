from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "Your id"
# Your Auth Token from twilio.com/console
auth_token  = "your token"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+Your phone number",
    #phone number given by twilio
    from_="+sending phone from twilio",
    #Message with multi-line message
    body="Hello\nMessage sent from program!")

#print(message.sid)
