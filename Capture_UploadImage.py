import cv2
import time
import random
import dropbox

start_time = time.time()

def take_snapshot():
    number = random.randint(0, 100)
    videoCapture = cv2.VideoCapture(1)

    result = True
    while(result):
        ret, frame = videoCapture.read()

        img_name = "img" + str(number) + ".png"
        cv2.imwrite(img_name, frame)
        start_time = time.time
        result = False
    return img_name
    print("snapshot taken!!")

    videoCapture.release()
    cv2.destroyAllWindows()

def upload_file(img_name):
    access_token = "sl.A8HsaOc6WplgElRXtYJEnGp-LKrFSX0x9zE-X7h0wOGhRpc5B8xWc7TM-ohsn_PrYVvFpMplVvEQmxAMlaS8kIAuogNURur99TRNL-aed_v4qHKBhBQ7W9Hy3PoMiFCB4qebVF6XIJs"
    file = img_name
    file_from = file
    file_to = "/testFolder/" + (img_name)
    dbx = dropbox.Dropbox(access_token)

    with open(file_from, 'rb') as f:
        dbx.files_upload(f.read(), file_to, mode=dropbox.files.WriteMode.overwrite)
        print("file uploaded!!")

def main():
    while(True):
        if((time.time() - start_time) >= 5):
            name = take_snapshot()
            upload_file(name)

main()