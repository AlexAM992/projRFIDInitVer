#!/usr/bin/python
#try to import modules
try:
    import pygtk
    import gtk
    import gtk.glade
    import serial_read as sr
    import mqtt_ops as mops
except:
    print("Problems on importing modules")
    pass

'''
Main Grafic Interface class
'''
class MainGui:
    def __init__(self):
        self.gladefile = "Acces_Control_v2.ui"
        self.builder = gtk.Builder()              
        self.builder.add_from_file(self.gladefile) #this build the app and delivers the handler
        self.builder.connect_signals(self)
        self.window = self.builder.get_object("gtk_wnd")
        self.editIDCard=self.builder.get_object("gtk_edt_card_id")
        self.window.show()
    #define signlas behavior
    def on_gtk_wnd_destroy(self,object,data=None):
        print("quit with x")
        gtk.main_quit()
    
    def on_gtkbtn_clear_clicked(self,button,data=None):
        self.editIDCard.set_text("")      
        
    def on_gtk_btn_get_access_clicked(self,button,data=None):
        self.editIDCard.set_text(" ")
        cardId=sr.serialRead()
        self.editIDCard.set_text(cardId) # use get_text to obtain string
        if( sr.ALLOWSERIAL1 in cardId ):
            mops.MQTT_Session("Acces OK")
        else:
            mops.MQTT_Session("Acces Not OK")



if __name__ == "__main__":
    main=MainGui()
    gtk.main()

#192.168.43.157

 

