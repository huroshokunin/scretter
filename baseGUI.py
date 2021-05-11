import tkinter
from tkinter import ttk, filedialog
import tweepy

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def askfolder():
    #参照ボタン機能
    path = filedialog.askopenfilename()
    f_path.set(path)

def do_Tweet():
    api.update_status("ソフトウェアからツイートしてます")


#GUIの色々
m_window = tkinter.Tk()
m_window.title("TEST")
m_window.geometry("400x200")

m_frame = ttk.Frame(m_window)
m_frame.grid(column=0, row=0, sticky=tkinter.NSEW, padx=5, pady=10)


f_path = tkinter.StringVar()

#ウィジェット追加
f_label = ttk.Label(m_frame, text="folder")
f_box = ttk.Entry(m_frame, textvariable=f_path)
f_button = ttk.Button(m_frame, text="reference", command=askfolder)
Twe_button = ttk.Button(m_frame, text="Tweet!", command=do_Tweet)


#ボタン配置
f_label.grid(column=0, row=0, pady=10)
f_box.grid(column=1, row=0, sticky=tkinter.EW, padx=5)
f_button.grid(column=2, row=0)
Twe_button.grid(column=2, row=1)

m_window.columnconfigure(0, weight=1)
m_window.rowconfigure(0, weight=1)
m_frame.columnconfigure(1, weight=1)
Twe_button.columnconfigure(0, weight=1)



m_window.mainloop()
