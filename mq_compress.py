def compress(points, precision):
   oldLat = 0
   oldLng = 0
   len_pts = len(points)
   index = 0
   encoded = ''
   precision = pow(10, precision)
   while (index < len_pts):
      #  Round to N decimal places
      lat = int(round(points[index] * precision));
      index = index + 1
      lng = int(round(points[index] * precision));
      index = index + 1

      #  Encode the differences between the points
      encoded += encodeNumber(lat - oldLat);
      encoded += encodeNumber(lng - oldLng);
      
      oldLat = lat;
      oldLng = lng;
   
   return encoded


def encodeNumber(num):
   num = num << 1
   if (num < 0):
      num = ~(num)
   
   encoded = ''
   while (num >= 0x20):
      encoded += chr((0x20 | (num & 0x1f)) + 63)
      num >>= 5
   
   encoded += chr(num + 63)
   return encoded

