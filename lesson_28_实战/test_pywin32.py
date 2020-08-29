import win32com.client
speaker = win32com.client.Dispatch('SAPI.SpVoice')
speaker.Speak('您好,小姐姐，能加个微信吗？')