import smtplib

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

followup_contents = {
    "samsung": "<h1>We have a Galaxy S9 discount just for you!</h1><img src=\"https://d1ic4altzx8ueg.cloudfront.net/finder-us/wp-uploads/2017/08/get-deal.jpeg\">",
    "couple": "<h1>Because couples that buy phone plans together, stay together!</h1><img src=\"https://www.t-mobile.com/content/dam/t-mobile/deals/background-images/240226_Q1_Plans-Plus-Affordable.desktop.jpg\">",
    "family": "<h1>We know geting plans for everyone in the family can be exhausting... Not anymore!</h1><img src=\"https://www.tmonews.com/wp-content/uploads/2016/09/tmobileonefourthlinefree-660x467.png\">",
    "switch": "<h1>Switch to T-Mobile and get your previous plan covered by us!</h1><img src=\"https://www.truthinadvertising.org/wp-content/uploads/2016/08/T-Mobile-ditch-and-switch.gif\">",
    "trade": "<h1>Get the latest discounts when you trade your old phone!</h1><img src=\"https://zdnet1.cbsistatic.com/hub/i/2016/09/09/14890fb6-232d-4170-85c4-37705300e1cd/4bcec0a6aacf2ae6109ee4e2d9892b83/iphone-7-trade-in-t-mobile-pricing.jpg\">",
    "apple": "<h1>Heard you didn't want your apple purchases to break your bank?</h1><img src=\"https://cdn.macrumors.com/article-new/2014/12/iphone-t-mobile.jpg\">",
}

def send_email(addr, followups):
    # Create message container - the correct MIME type is multipart/alternative.
    msg = MIMEMultipart('alternative')
    msg['Subject'] = "Tmobile Followup"
    msg['From'] = "c2cfaceio@email.com"
    msg['To'] = addr

    # Create the body of the message (a plain-text and an HTML version).
    text = "It was great talking to you over at T-Mobile!"
    html = """
    <html>
      <head></head>
      <body>
        <h1>It was great talking to you at T-Mobile!</h1>
        <h2>Thanks for trusting in us one more time</h2>
        <p>As we hope to improve our customer service, we would love to hear from you what you have to say about the past visit to one of our stores.</p>
        <a href="https://www.t-mobile.com/feedback.html"></a>
        <h4>Also, here are some things you might be interested in based on your visit today:</h4>
        """ + "\n".join([followup_contents[item.lower()] for item in followups if item in followup_contents]) + """
      </body>
    </html>
    """

    # Record the MIME types of both parts - text/plain and text/html.
    part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # Attach parts into message container.
    # According to RFC 2046, the last part of a multipart message, in this case
    # the HTML message, is best and preferred.
    msg.attach(part1)
    msg.attach(part2)
    # Send the message via local SMTP server.
    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    mail.login('c2cfaceio', 'faceiofaceio')
    mail.sendmail("c2cfaceio@email.com", addr, msg.as_string())
    mail.quit()

if __name__ == "__main__":
    # emails = ["davi.nakajima.an@gmail.com", "gabriel.nakajima.an@gmail.com", "mszylkowski09@gmail.com"]
    # emails = ["mszylkowski09@gmail.com"]
    emails = ["gabriel.nakajima.an@gmail.com"]
    for email in emails:
        send_email(email, ["samsung", "family", "switch"])
    print("All emails sent")
