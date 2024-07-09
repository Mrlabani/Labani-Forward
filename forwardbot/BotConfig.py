from os import environ
class Config(object):
    API_ID = environ.get("API_ID", "22179597")
    API_HASH = environ.get("API_HASH", "72a54a3b2a449b5b7dd0c75da9a1487d")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7208627178:AAEuAUEPUDtn_wVZ9HoAjP5s8nCmEmLkIaI")
    STRING_SESSION = environ.get("STRING_SESSION", "1BVtsOGcBuzvo7Cud7jc2GuXckkGLzdzEFJTMbYku6SMAB4110h9NPtiuMjhIWvsm_CurmgFE5ws4Y2aQQrub5x6kq2HEisTp96r59-X9bXKE27RfnggNFenUPNBEdk6ffwx5KcXoJH_SHILVJ72_fRx5f4xOIgG-ZeO-GhqkWubEspYSXXc5pyJq91ule8BA6-3JsqYfZXF7CX-Uw6Df1zBZ8F97QHZkLdJsehY2SOFlN2ATuioy7-60DCKuvLRV1KQALAYNY5CtaInvtYSllKy4L97EYqgdpBl-DXdXDA251MCxv3FPKCtM-70l4bFiS6oRDugPaTyk3EWChUQqt9MnlKjyQac=")
    SUDO_USERS = environ.get("SUDO_USERS", "6473618718,7037451646")
    COMMAND_HAND_LER = environ.get("COMMAND_HAND_LER", "^/")
    HELP_MSG = """
    💢 **ᴛʜᴇ ᴄᴏᴍᴍᴀɴᴅs ɪɴ ᴛʜᴇ ʙᴏᴛ ᴀʀᴇ:**
    
    🔻 **Command :** /forward
    **Usage : ** Forwards messages from a channel to other.
    🔻 **Command :** /count
    **Usage : ** Returns the Total message sent using the bot.
    🔻 **Command :** /reset
    **Usage : ** Resets the message count to 0.
    🔻 **Command :** /restart
    **Usage : ** Updates and Restarts the Bot.
    🔻 **Command :** /join
    **Usage : ** Joins the channel.
    🔻 **Command :** /help
    **Usage : ** Get the help of this bot.
    🔻 **Command :** /status
    **Usage :** Check current status of Bot.
    🔻 **Command :** /uptime
    **Usage :** Check uptime of Bot.
    
    ⭕ **ʙᴏᴛ ɪs ᴄʀᴇᴀᴛᴇᴅ ʙʏ** **@l_abani**
    """
