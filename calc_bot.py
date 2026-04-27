import re
from telegram.ext import ApplicationBuilder,CommandHandler,MessageHandler,filters
TOKEN="8674305541:AAFBY0C6VfWlR-kw8EFwTHccXTHmngyvA8U"
S=re.compile(r"^[\d\s\+\-\*\/\.\(\)]+$")
def cx(e):
 e=e.strip()
 if not S.match(e):return None
 try:
  r=eval(e)
  return str(int(r))if isinstance(r,float)and r.is_integer()else str(r)
 except:return None
async def st(u,c):await u.message.reply_text("Send math like 25*4")
async def hd(u,c):
 r=cx(u.message.text)
 await u.message.reply_text(u.message.text+"="+r if r else "Invalid")
app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",st))
app.add_handler(MessageHandler(filters.TEXT&~filters.COMMAND,hd))
app.run_polling()
