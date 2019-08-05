#   _____ _               _     _____         _______                  _       _   _             
#  / ____| |             | |   |_   _|       |__   __|                | |     | | (_)            
# | |  __| |__   ___  ___| |_    | |  _ __      | |_ __ __ _ _ __  ___| | __ _| |_ _  ___  _ __  
# | | |_ | '_ \ / _ \/ __| __|   | | | '_ \     | | '__/ _` | '_ \/ __| |/ _` | __| |/ _ \| '_ \ 
# | |__| | | | | (_) \__ | |_   _| |_| | | |    | | | | (_| | | | \__ | | (_| | |_| | (_) | | | |
#  \_____|_| |_|\___/|___/\__| |_____|_| |_|    |_|_|  \__,_|_| |_|___|_|\__,_|\__|_|\___/|_| |_|
#                                                                                                                                                                                                                                                              
# This script will show information hidden in images
                                                                                       
from PIL import Image
from itertools import product
import math

class ImageDecoder:
    def __init__(self):
        pass

    def decode(self):
        """
        Image decoding.
        :return: encoded message-string
        """

        image_file = input("Enter image name to decode: ")

        image = Image.open(image_file)
        pix = image.load()
        size_x, size_y = image.size

        blocks_size = math.ceil(size_x / 600)

        next_index = product(range(int(size_x/blocks_size)), range(int(size_y/blocks_size)))

        # find number of chunks
        num_of_chuncks = 0
        for i in range(7, -1, -1):
            index = next(next_index)
            index_x = index[0]*blocks_size
            index_y = index[1]*blocks_size

            # averaging the values of the block
            b = pix[index_x, index_y][2]
            for p in range(0, blocks_size):
                b += pix[index_x+p, index_y+p][2]
            b = int(b / blocks_size)
            
            if b>11:
                num_of_chuncks += 2 ** i

        message = []
        for i in range(num_of_chuncks):
            # find length of current chunk
            message_len = 0
            for j in range(7, -1, -1):
                index = next(next_index)
                index_x = index[0]*blocks_size
                index_y = index[1]*blocks_size

                # averaging the values of the block
                b = pix[index_x, index_y][2]
                for p in range(0, blocks_size):
                    b += pix[index_x+p, index_y+p][2]
                b = int(b / blocks_size)
                
                if b>11:
                    message_len += 2 ** j

            for k in range(message_len):
                part = 0
                for j in range(7, -1, -1):
                    index = next(next_index)
                    index_x = index[0]*blocks_size
                    index_y = index[1]*blocks_size
    
                    # averaging the values of the block
                    b = pix[index_x, index_y][2]
                    for p in range(0, blocks_size):
                        b += pix[index_x+p, index_y+p][2]
                    b = int(b / blocks_size)
                    
                    if b>11:
                        part += 2 ** j

                message.append(part)

        print('')
        return bytes(message).decode("utf-8", "replace")


if __name__ == '__main__':
    print("""
  _____ _               _     _____         _______                  _       _   _             
 / ____| |             | |   |_   _|       |__   __|                | |     | | (_)            
| |  __| |__   ___  ___| |_    | |  _ __      | |_ __ __ _ _ __  ___| | __ _| |_ _  ___  _ __  
| | |_ | '_ \ / _ \/ __| __|   | | | '_ \     | | '__/ _` | '_ \/ __| |/ _` | __| |/ _ \| '_ \ 
| |__| | | | | (_) \__ | |_   _| |_| | | |    | | | | (_| | | | \__ | | (_| | |_| | (_) | | | |
 \_____|_| |_|\___/|___/\__| |_____|_| |_|    |_|_|  \__,_|_| |_|___|_|\__,_|\__|_|\___/|_| |_|

Image decoder

    """)

    decoder = ImageDecoder()
    print(decoder.decode())
    print('')
