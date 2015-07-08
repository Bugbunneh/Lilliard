import ch
import random
import sys
import re
if sys.version_info[0] > 2:
  import urllib.request as urlreq
else:
  import urllib2 as urlreq

  
finally:
    
    if con:
        con.close()
 
 
##Dance moves!
#kinda useless
 
dancemoves = [
  "(>^.^)>",
  "(v^.^)v",
  "v(^.^v)",
  "<(^.^<)"
]
 
class TestBot(ch.RoomManager):
  def onInit(self):
    self.setNameColor("F9F")
    self.setFontColor("F33")
    self.setFontFace("1")
    self.setFontSize(10)
    self.enableBg()
    self.enableRecording()
 

#This is what will be printed on your python console when event called
 
  def onConnect(self, room):
    print("Connected")
 
  def onReconnect(self, room):
    print("Reconnected")
 
  def onDisconnect(self, room):
    print("Disconnected")
 
 
 
  def onMessage(self, room, user, message):
   try:
    if room.getLevel(self.user) > 0:
      print(user.name, message.body)
    else:
      print(user.name, message.body)
    if self.user == user: return
    if message.body[0] == "!":   ##Here is the Prefix part
      data = message.body[1:].split(" ", 1)
      if len(data) > 1:
        cmd, args = data[0], data[1]
      else:
        cmd, args = data[0], ""
 

      if cmd == "ev" or cmd == "eval" or cmd == "e":
          ret = eval(args)
          if ret == None:
            room.message("Done.")
            return
          room.message(str(ret))
 
        ##Say
        #Make your bot say what you want
      if cmd == "say":
        room.message(args)
 
        ##Random User
        #What's this for ? this one cmd will make your boy say the name of a random user in a room
      if cmd == "randomuser":
        room.message(random.choice(room.usernames))
 
        ##Check Level
        #This one cmd is tho make your bot say your mod level in the current room you're in
      elif cmd == "mylvl":
        room.message("Your mod level: %i" %(room.getLevel(user)))
 
        ##List Mods
        #List of Mods and Owner name in the current room you're in
      elif cmd == "mods":
        room.message(", ".join(room.modnames + [room.ownername]))
 
        ##DANCE!!!!
        #Dance ? Of Course !!! ^_^
      elif cmd == "dance":
        for i, msg in enumerate(dancemoves):
          self.setTimeout(i / 2, room.message, msg)
         
        ##Check if Mod
        #not really important
      elif cmd == "ismod":
        user = ch.User(args)
        if room.getLevel(user) > 0:
          room.message("yesh")
        else:
          room.message("nope")
   except Exception as e:
      try:
        et, ev, tb = sys.exc_info()
        lineno = tb.tb_lineno
        fn = tb.tb_frame.f_code.co_filename
        room.message("[Expectation Failed] %s Line %i - %s"% (fn, lineno, str(e)))
        return
      except:
        room.message("Undescribeable error detected !!")
        return
 
  ##Other Crap here, Dont worry about it
 
  def onFloodWarning(self, room):
    room.reconnect()
 
  def onJoin(self, room, user):
   print(user.name + " joined the chat!")
 
  def onLeave(self, room, user):
   print(user.name + " left the chat!")
 
  def onUserCountChange(self, room):
    print("users: " + str(room.usercount))
 
  def onMessageDelete(self, room, user, msg):
    print("MESSAGE DELETED: " + user.name + ": " + msg.body)
 
 
if __name__ == "__main__": TestBot.easy_start()
