from telebot import telegramBot
from urllib.parse import quote_plus


def parseListToString(arr):
    result = ''
    for i in range(len(arr)):
        result += f"/{i} : {arr[i]}\n\n"
    result += "/exit"
    return result


if __name__ == '__main__':
    bot = telegramBot(botToken="", chatID='')#
    while True:
        newmsg, msgtype = bot.waitNewMessage(specifity=True, waittime=30)
        if newmsg and msgtype == "text":
            if bot.getLastMsg() == "/newlead":
                case = 1
                while (case != 69):
                    if case == 1:
                        # shit starts here
                        bot.sendText("Enter Name...\n\n/exit")
                        text = bot.pollResponse(specifity=True, waittime=30)
                        if text == "/exit":
                            case = 69
                            bot.sendText("Cancelling Entry...")
                        elif text == 'null':
                            bot.sendText("Invalid Entry... Try again!")
                        else:
                            name = text
                            case = 2

                    if case == 2:
                        bot.sendText("Enter Company...\n\n/exit")
                        text = bot.pollResponse(specifity=True, waittime=30)
                        if text == "/exit":
                            case = 69
                            bot.sendText("Cancelling Entry...")
                        elif text == 'null':
                            bot.sendText("Invalid Entry... Try again!")
                        else:
                            company = text
                            case = 3

                    if case == 3:
                        bot.sendText("Enter Position\n\n/exit.")
                        text = bot.pollResponse(specifity=True, waittime=30)
                        if text == "/exit":
                            case = 69
                            bot.sendText("Cancelling Entry...")
                        elif text == 'null':
                            bot.sendText("Invalid Entry... Try again!")
                        else:
                            position = text
                            case = 4

                    if case == 4:
                        bot.sendText("Enter Email\n\n/exit.")
                        text = bot.pollResponse(specifity=True, waittime=30)
                        if text == "/exit":
                            case = 69
                            bot.sendText("Cancelling Entry...")
                        elif text == 'null':
                            bot.sendText("Invalid Entry... Try again!")
                        else:
                            email = text
                            case = 5

                    if case == 5:
                        print(name, company, position, email)
                        bot.sendText("You have selected:\n"
                                     + f"Name : {name}\n"
                                     + f"Company : {company}\n"
                                     + f"Position : {position}\n"
                                     + f"Email : {email}\n")
                        bot.sendText("Would you like to push this to CRM?\n\n/yes\n\n/edit\n\n/no")
                        resp = bot.pollResponse(specifity=True, waittime=30)
                        if resp == "/yes":
                            bot.sendText("Pushing to CRM...")
                            case = 6
                        elif resp == '/edit':
                            bot.sendText("Which one would you like to edit?"
                                         + "\n\n/name\n\n/company\n\n/position\n\n/email")
                            resp = bot.pollResponse(specifity=True, waittime=30)
                            if resp in ['/name', '/company', '/position', '/email']:
                                variable = resp.replace('/', '')
                                bot.sendText(f"Please input new {variable}. You can copy the next line as reference...")
                                bot.sendText(vars()[variable])
                                new = bot.pollResponse(specifity=True, waittime=30)
                                vars()[variable] = new
                                bot.sendText("Update Done!")
                        elif resp == "/no":
                            bot.sendText("Cancelling Entry...")
                            case = 69
                        else:
                            bot.sendText("Invalid Entry... Try again!")
                    if case == 6:
                        # post to CRM here
                        # clear memory
                        name = ''
                        company = ''
                        position = ''
                        email = ''
                        case = 69
        elif newmsg and msgtype == "photo":
            case = 0
            while(case!=69):
                if case == 0:
                    bot.sendText("Making predictions, please hold...")
                    try:
                        pred = bot.makePrediction()
                        print(pred)
                        msg = parseListToString(pred)
                        print(msg)
                        case = 1
                    except:
                        bot.sendText("Server is busy... try again in 3 minutes :(")
                        case = 69

                if case == 1:
                    #shit starts here
                    bot.sendText("Please select Name by\n1) Selecting the commands or\n2) Typing it out with the ! keyword (e.g. !Austin)")
                    bot.sendText(quote_plus(msg))
                    text = bot.pollResponse(specifity=True, waittime=30)
                    if text == "/exit":
                        case = 69
                        bot.sendText("Cancelling Entry...")
                    elif "/" in text:
                        nameindex = int(text.replace("/", ""))
                        name = pred[nameindex]
                        case = 2
                    elif "!" in text:
                        name = text.replace("!", "")
                        case = 2
                    else:
                        bot.sendText("Invalid Entry... Try again!")
                        name = text

                if case == 2:
                    bot.sendText("Please select Company by\n1) Selecting the commands or\n2) Typing it out with the ! keyword (e.g. !Austin)")
                    bot.sendText(quote_plus(msg))
                    text = bot.pollResponse(specifity=True, waittime=30)
                    if text == "/exit":
                        case = 69
                        bot.sendText("Cancelling Entry...")
                    elif "/" in text:
                        companyindex = int(text.replace("/", ""))
                        company = pred[companyindex]
                        case = 3
                    elif "!" in text:
                        company = text.replace("!", "")
                        case = 3
                    else:
                        bot.sendText("Invalid Entry... Try again!")
                        company = text

                if case == 3:
                    bot.sendText("Please select Position by\n1) Selecting the commands or\n2) Typing it out with the ! keyword (e.g. !Austin)")
                    bot.sendText(quote_plus(msg))
                    text = bot.pollResponse(specifity=True, waittime=30)
                    if text == "/exit":
                        case = 69
                        bot.sendText("Cancelling Entry...")
                    elif "/" in text:
                        posindex = int(text.replace("/", ""))
                        position = pred[posindex]
                        case = 4
                    elif "!" in text:
                        position = text.replace("!", "")
                        case = 4
                    else:
                        bot.sendText("Invalid Entry... Try again!")
                        position = text

                if case == 4:
                    bot.sendText("Please select Email by\n1) Selecting the commands or\n2) Typing it out with the ! keyword (e.g. !Austin)")
                    bot.sendText(quote_plus(msg))
                    text = bot.pollResponse(specifity=True, waittime=30)
                    if text == "/exit":
                        case = 69
                        bot.sendText("Cancelling Entry...")
                    elif "/" in text:
                        emailindex = int(text.replace("/", ""))
                        email = pred[emailindex]
                        case = 5
                    elif "!" in text:
                        email = text.replace("!", "")
                        case = 5
                    else:
                        bot.sendText("Invalid Entry... Try again!")
                        email = text

                if case == 5:
                    print(name, company, position, email)
                    bot.sendText("You have selected:\n"
                                 + f"Name : {name}\n"
                                 + f"Company : {company}\n"
                                 + f"Position : {position}\n"
                                 + f"Email : {email}\n")
                    bot.sendText("Would you like to push this to CRM?\n\n/yes\n\n/edit\n\n/no")
                    resp = bot.pollResponse(specifity=True, waittime=30)
                    if resp == "/yes":
                        bot.sendText("Pushing to CRM...")
                        case = 6
                    elif resp == '/edit':
                        bot.sendText("Which one would you like to edit?"
                                     + "\n\n/name\n\n/company\n\n/position\n\n/email")
                        resp = bot.pollResponse(specifity=True, waittime=30)
                        if resp in ['/name', '/company', '/position', '/email']:
                            variable = resp.replace('/', '')
                            bot.sendText(f"Please input new {variable}. You can copy the next line as reference...")
                            bot.sendText(vars()[variable])
                            new = bot.pollResponse(specifity=True, waittime=30)
                            vars()[variable] = new
                            bot.sendText("Update Done!")
                    elif resp == "/no":
                        bot.sendText("Cancelling Entry...")
                        case = 69
                    else:
                        bot.sendText("Invalid Entry... Try again!")
                if case == 6:
                    #post to CRM here
                    #clear memory
                    name = ''
                    company = ''
                    position = ''
                    email = ''
                    case = 69
