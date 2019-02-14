from twilio.rest import Client
# from twilio folder , there is folder called rest which has a class called Client

# Your Account SID from twilio.com/console
account_sid = "AC0a9deed422a5213152532ffa04b1b985"
# Your Auth Token from twilio.com/console
auth_token  = "0dd647f40f4874676abfe3702d1db944"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+917906721486", 
    from_="+18474439657",
    body="this is awesome")

print(message.sid)
