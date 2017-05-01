from twilio.rest import Client
import feedparser

#This script fetches the latest Quote added in the Inspirational category.
#To switch to your favorite category, just replace the 'Inspiration' in URL with your category.
#Make sure the category exists on QuotesDaddy.com

d = feedparser.parse("https://www.quotesdaddy.com/feed/tagged/Inspirational")
quote = d['entries'][0]['title_detail']['value']

print (quote)

# You need to create a Twilio account to get Account SID and Auth Token
# Twilio provides free account through which you can send and receive FREE SMS.

#Enter everything between the Quotations

# Your Account SID from twilio.com/console
account_sid = "Account SID Here"

# Your Auth Token from twilio.com/console
auth_token  = "Auth Token Here"

client = Client(account_sid, auth_token)

#Enter Your Verified Twilio Number in 'to'.
#Enter the assigned number i.e. through which the sms will be sent in 'from_'
#Don't remove Quotations

message = client.messages.create(
                to="Twilio Verified Number Here", 
                from_="Twilio Assigned Number",
                body=uote)
