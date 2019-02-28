from Photo import Photo

class Parser:


    def parse(self,input_file):
        photos_arr = []
        with open(input_file) as f:
            lines = f.readlines()
            for idx,line in enumerate(lines[1:]):
                splitted_line = line.strip().split(' ')
                photo = Photo()
                photo.id = idx
                photo.isVertical = splitted_line[0] == 'V'
                photo.tags = set(splitted_line[2:])
                photos_arr.append(photo)

        return photos_arr


if __name__ == '__main__':
    p = Parser()
    photos_arr = p.parse('resources/input/a_example.txt')
    print(','.join(photos_arr))