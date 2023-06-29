import requests

username = input("ENTER USERNAME: ")

def get_info(username):
    try:
        response = requests.get(f'https://www.tiktok.com/@{username}')
        patrek = response.text

        getting = str(patrek.split('"UserModule":')[1]).split('"RecommendUserList"')[0]
        
        try:
            id = str(getting.split('id":"')[1]).split('",')[0]
        except:
            id = ""
        
        try:
            name = str(getting.split('nickname":"')[1]).split('",')[0]
        except:
            name = ""
        
        try:
            bio = str(getting.split('signature":"')[1]).split('",')[0]
        except:
            bio = ""
        
        try:
            country = str(getting.split('region":"')[1]).split('",')[0]
        except:
            country = ""
        
        try:
            private = str(getting.split('privateAccount":')[1]).split(',"')[0]
        except:
            private = ""
        
        try:
            followers = str(getting.split('followerCount":')[1]).split(',"')[0]
        except:
            followers = ""
        
        try:
            following = str(getting.split('followingCount":')[1]).split(',"')[0]
        except:
            following = ""
        
        try:
            like = str(getting.split('heart":')[1]).split(',"')[0]
        except:
            like = ""
        
        try:
            video = str(getting.split('videoCount":')[1]).split(',"')[0]
        except:
            video = ""
        
        kls = f"""───────────────
ᴜѕᴇʀɴᴀᴍᴇ ➢ {username}
ɴᴀᴍᴇ ➢ {name}
ғᴏʟʟᴏᴡᴇʀѕ ➢ {followers}
ғᴏʟʟᴏᴡɪɴɢ ➢ {following}
ʟɪᴋᴇ ➢ {like}
ᴠɪᴅᴇᴏ ➢ {video}
ᴘʀɪᴠᴀᴛᴇ ➢ {private}
ᴄᴏᴜɴᴛʀʏ ➢ {country}
ɪᴅ ➢ {id}
ʙɪᴏ ➢ {bio}
        ───────────────"""
        
        print(kls)
    
    except:
        print("BAD USERNAME")

get_info(username)
