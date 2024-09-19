import os
from PIL import Image,ExifTags

# point 14
img_folder = r'D:\fourth-year\Second-Term\Geographic-Information-Systems\project\images'
img_contents = os.listdir(img_folder)

for image in img_contents:
    full_path = os.path.join(img_folder,image)
    print "full_path: " + full_path

    pillow_img = Image.open(full_path)
    exif = {ExifTags.TAGS[k]: v for k, v in pillow_img._getexif().items()if k in ExifTags.TAGS}
#poitn 15
    print  exif

    gps_all = {}
    try:
        for key in exif['GPSInfo'].keys():
            decoded_value = ExifTags.GPSTAGS.get(key)
            gps_all[decoded_value] = exif['GPSInfo'][key]

        long_ref = gps_all.get('GPSLongitudeRef')
        long = gps_all.get('GPSLongitude')

        lat_ref = gps_all.get('GPSLatitudeRef')
        lat = gps_all.get('GPSLatitude')
#point 17

        print "long: "+long_ref, " ", long
        print "lat: "+lat_ref, " ", lat
    except:
        print "This image has no GPS Info in it {}".format(full_path)
        pass