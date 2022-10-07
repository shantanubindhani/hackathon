import vonage

client = vonage.Client(key="078900dc", secret="rgTCxideCclgE1gA")
sms = vonage.Sms(client)

clients = ["918917322838", "917265878284"]

message = "hmmmmmm bleh!."

for clientNumber in clients:
    responseData = sms.send_message(
        {
            "from": "Vonage APIs",
            "to": clientNumber,
            "text": message,
        }
    )

    if responseData["messages"][0]["status"] == "0":
        print("Message sent successfully.")
    else:
        print(f"Message failed with error: {responseData['messages'][0]['error-text']}")