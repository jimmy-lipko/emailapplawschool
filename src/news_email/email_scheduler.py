# Import libraries
import smtplib, ssl
import pandas as pd
import numpy as np
import yaml
import requests
import urllib
from datetime import date
from bs4 import BeautifulSoup
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def emailer(name, reciever_email,sender_email, pwd):
    date = date.today()
    today = date.strftime("%B %d, %Y")
    subject = "Good Morning" + str(name) + "Here is your news for " + str(today) + "."


    message = MIMEMultipart("alternative")
    message["Subject"] = subject
    message["From"] = sender_email
    message["To"] = receiver_email

    result_cnbc = requests.get("https://www.cnbc.com/")
    page_content_cnbc = result_cnbc.content
    soup_cnbc = BeautifulSoup(page_content_cnbc, 'lxml')
    article_cnbc = soup_cnbc.find(lambda tag: tag.name == 'h2' and
                                       tag.get('class') == ['FeaturedCard-packagedCardTitle'])
    cnbc_title = article_cnbc.find("a").attrs['title']
    cnbc_link = article_cnbc.find("a").attrs['href']

    result_fox = requests.get("https://www.foxbusiness.com/")
    page_content_fox = result_fox.content
    soup_fox = BeautifulSoup(page_content_fox, 'lxml')
    article_fox = [soup_fox.find(lambda tag: tag.name == 'div' and
                                       tag.get('class') == ['m'])]

    fox_title = article_fox[0].find_all("a")[-1].find_all("img")[0].attrs['alt']

    fox_link = article_fox[0].find("a").attrs['href']

    result_reuters = requests.get("https://www.reuters.com/legal/")
    page_content_reuters = result_reuters.content
    soup_reuters = BeautifulSoup(page_content_reuters, 'lxml')
    reuters_article = [soup_reuters.find(lambda tag: tag.name == 'a' and
                                       tag.get('class') == ['MediaStoryCard__basic_hero___fSAEnM'])]

    reuters_title = reuters_article[0].find(lambda tag: tag.name == 'span' and
                                       tag.get('class') == ['MediaStoryCard__title___2PHMeX']).contents[0]
    reuters_link = 'https://www.reuters.com' + str(reuters_article[0].attrs['href'])

    result_religion = requests.get('https://www.ncregister.com/')
    page_content_religion = result_religion.content
    soup_religion = BeautifulSoup(page_content_religion, 'lxml')
    article_religion = soup_religion.find(lambda tag: tag.name == 'h2' and
                                       tag.get('class') == ['mainArticle__headline'])
    religion_title = article_religion.find("a").contents[0]
    religion_link =  article_religion.find("a").attrs['href']


    result_nr = requests.get('https://www.nationalreview.com/')
    page_content_nr = result_nr.content
    soup_nr = BeautifulSoup(page_content_nr, 'lxml')
    article_nr = soup_nr.find(lambda tag: tag.name == 'h4' and
                                       tag.get('class') == ['post-list-article__title'])
    nr_title = article_nr.find("a").contents[0]
    nr_link =  article_nr.find("a").attrs['href']

    result_boston = requests.get('https://www.boston.com/')
    page_content_boston = result_boston.content
    soup_boston = BeautifulSoup(page_content_boston, 'lxml')
    article_boston = soup_boston.find(lambda tag: tag.name == 'h2' and
                                       tag.get('class') == ['a-article__title'])
    boston_title = article_boston.find("a").contents[0]
    boston_link =  article_boston.find("a").attrs['href']
    # Create the plain-text and HTML version of your message

    html = """\
    <!DOCTYPE HTML PUBLIC "-//W3C//DTD XHTML 1.0 Transitional //EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
    <html xmlns="http://www.w3.org/1999/xhtml" xmlns:v="urn:schemas-microsoft-com:vml" xmlns:o="urn:schemas-microsoft-com:office:office">
    <head>
    <!--[if gte mso 9]>
    <xml>
      <o:OfficeDocumentSettings>
        <o:AllowPNG/>
        <o:PixelsPerInch>96</o:PixelsPerInch>
      </o:OfficeDocumentSettings>
    </xml>
    <![endif]-->
      <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <meta name="x-apple-disable-message-reformatting">
      <!--[if !mso]><!--><meta http-equiv="X-UA-Compatible" content="IE=edge"><!--<![endif]-->
      <title></title>

        <style type="text/css">
          table, td { color: #000000; } a { color: #0000ee; text-decoration: underline; }
    @media only screen and (min-width: 520px) {
      .u-row {
        width: 500px !important;
      }
      .u-row .u-col {
        vertical-align: top;
      }

      .u-row .u-col-100 {
        width: 500px !important;
      }

    }

    @media (max-width: 520px) {
      .u-row-container {
        max-width: 100% !important;
        padding-left: 0px !important;
        padding-right: 0px !important;
      }
      .u-row .u-col {
        min-width: 320px !important;
        max-width: 100% !important;
        display: block !important;
      }
      .u-row {
        width: calc(100% - 40px) !important;
      }
      .u-col {
        width: 100% !important;
      }
      .u-col > div {
        margin: 0 auto;
      }
    }
    body {
      margin: 0;
      padding: 0;
    }

    table,
    tr,
    td {
      vertical-align: top;
      border-collapse: collapse;
    }

    p {
      margin: 0;
    }

    .ie-container table,
    .mso-container table {
      table-layout: fixed;
    }

    * {
      line-height: inherit;
    }

    a[x-apple-data-detectors='true'] {
      color: inherit !important;
      text-decoration: none !important;
    }

    </style>



    </head>

    <body class="clean-body" style="margin: 0;padding: 0;-webkit-text-size-adjust: 100%;background-color: #f1e4fd;color: #000000">
      <!--[if IE]><div class="ie-container"><![endif]-->
      <!--[if mso]><div class="mso-container"><![endif]-->
      <table style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;min-width: 320px;Margin: 0 auto;background-color: #f1e4fd;width:100%" cellpadding="0" cellspacing="0">
      <tbody>
      <tr style="vertical-align: top">
        <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top">
        <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td align="center" style="background-color: #f1e4fd;"><![endif]-->


    <div class="u-row-container" style="padding: 0px;background-color: transparent">
      <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

    <!--[if (mso)|(IE)]><td align="center" width="500" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
      <div style="width: 100% !important;">
      <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->

    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
      <tbody>
        <tr>
          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">

      <h1 style="margin: 0px; line-height: 140%; text-align: center; word-wrap: break-word; font-weight: normal; font-family: arial,helvetica,sans-serif; font-size: 27px;">
        News Update
      </h1>

          </td>
        </tr>
      </tbody>
    </table>

    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
      <tbody>
        <tr>
          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">

      <table height="0px" align="center" border="0" cellpadding="0" cellspacing="0" width="100%" style="border-collapse: collapse;table-layout: fixed;border-spacing: 0;mso-table-lspace: 0pt;mso-table-rspace: 0pt;vertical-align: top;border-top: 1px solid #BBBBBB;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
        <tbody>
          <tr style="vertical-align: top">
            <td style="word-break: break-word;border-collapse: collapse !important;vertical-align: top;font-size: 0px;line-height: 0px;mso-line-height-rule: exactly;-ms-text-size-adjust: 100%;-webkit-text-size-adjust: 100%">
              <span>&#160;</span>
            </td>
          </tr>
        </tbody>
      </table>

          </td>
        </tr>
      </tbody>
    </table>

      <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
      </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
          <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
      </div>
    </div>



    <div class="u-row-container" style="padding: 0px;background-color: transparent">
      <div class="u-row" style="Margin: 0 auto;min-width: 320px;max-width: 500px;overflow-wrap: break-word;word-wrap: break-word;word-break: break-word;background-color: transparent;">
        <div style="border-collapse: collapse;display: table;width: 100%;background-color: transparent;">
          <!--[if (mso)|(IE)]><table width="100%" cellpadding="0" cellspacing="0" border="0"><tr><td style="padding: 0px;background-color: transparent;" align="center"><table cellpadding="0" cellspacing="0" border="0" style="width:500px;"><tr style="background-color: transparent;"><![endif]-->

    <!--[if (mso)|(IE)]><td align="center" width="500" style="width: 500px;padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;" valign="top"><![endif]-->
    <div class="u-col u-col-100" style="max-width: 320px;min-width: 500px;display: table-cell;vertical-align: top;">
      <div style="width: 100% !important;">
      <!--[if (!mso)&(!IE)]><!--><div style="padding: 0px;border-top: 0px solid transparent;border-left: 0px solid transparent;border-right: 0px solid transparent;border-bottom: 0px solid transparent;"><!--<![endif]-->

    <table style="font-family:arial,helvetica,sans-serif;" role="presentation" cellpadding="0" cellspacing="0" width="100%" border="0">
      <tbody>
        <tr>
          <td style="overflow-wrap:break-word;word-break:break-word;padding:10px;font-family:arial,helvetica,sans-serif;" align="left">

      <div style="line-height: 140%; text-align: left; word-wrap: break-word;">
        <p style="font-size: 14px; line-height: 140%; text-align: left;"><span style="font-size: 18px; line-height: 25.2px;">Good Morning """ + str(name) + """, </span></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px;">Today is """ + str(today) +""".</span></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px;">Here is what is making news this morning...</span></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 20px; line-height: 28px;">CNBC Business</span></strong></p>
    <p style="font-size: 14px; line-height: 140%;"><a href=" """+ str(cnbc_link) +""" " target="_blank" rel="noopener">""" + str(cnbc_title) + """</a></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 20px; line-height: 28px;">Fox Business</span></strong></p>
    <p style="font-size: 14px; line-height: 140%;"><a href=" """+ str(fox_link) +""" " target="_blank" rel="noopener">"""+ str(fox_title) +"""</a></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 20px; line-height: 28px;">Law Article - Reuters</span></strong></p>
    <p style="font-size: 14px; line-height: 140%;"><a href=" """+ str(reuters_link) +""" " target="_blank" rel="noopener">"""+ str(reuters_title) +"""</a></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 20px; line-height: 28px;">Religion</span></strong></p>
    <p style="font-size: 14px; line-height: 140%;"><a href=" """+ str(religion_link) +""" " target="_blank" rel="noopener">"""+ str(religion_title) +"""</a></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 20px; line-height: 28px;">National Review</span></strong></p>
    <p style="font-size: 14px; line-height: 140%;"><a href=" """+ str(nr_link) +""" " target="_blank" rel="noopener">"""+ str(nr_title) +"""</a></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><strong><span style="font-size: 20px; line-height: 28px;">Boston News</span></strong></p>
    <p style="font-size: 14px; line-height: 140%;"><a href=" """+ str(boston_link) +""" " target="_blank" rel="noopener">"""+ str(boston_title) +"""</a></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px;"><span style="line-height: 25.2px; font-size: 18px;">Hope you enjoyed these! Have a spectacular day!</span></span></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px;"><span style="line-height: 25.2px; font-size: 18px;">Love,&nbsp;</span></span></p>
    <p style="font-size: 14px; line-height: 140%;">&nbsp;</p>
    <p style="font-size: 14px; line-height: 140%;"><span style="font-size: 18px; line-height: 25.2px;"><span style="line-height: 25.2px; font-size: 18px;">Jimmy-Bot</span></span></p>
      </div>

          </td>
        </tr>
      </tbody>
    </table>

      <!--[if (!mso)&(!IE)]><!--></div><!--<![endif]-->
      </div>
    </div>
    <!--[if (mso)|(IE)]></td><![endif]-->
          <!--[if (mso)|(IE)]></tr></table></td></tr></table><![endif]-->
        </div>
      </div>
    </div>


        <!--[if (mso)|(IE)]></td></tr></table><![endif]-->
        </td>
      </tr>
      </tbody>
      </table>
      <!--[if mso]></div><![endif]-->
      <!--[if IE]></div><![endif]-->
    </body>

    </html>
    """

    # Turn these into plain/html MIMEText objects

    part1= MIMEText(html, "html")

    # Add HTML/plain-text parts to MIMEMultipart message
    # The email client will try to render the last part first

    message.attach(part1)

    # Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, pwd)
        server.sendmail(
            sender_email, receiver_email, message.as_string()
        )
