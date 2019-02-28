from Parser import Parser

class Evaluator:
    pass





def calcInterest(photo1, photo2):
    photos_intersection = photo1.tags.intersection(photo2.tags)
    diff_1 = photo1.tags - photo2.tags
    diff_2 = photo2.tags - photo1.tags
    min_score = min(len(diff_1),len(diff_2),len(photos_intersection))
    # print(len(diff_1),len(diff_2),len(photos_intersection))
    return min_score


if __name__ == '__main__':
    p = Parser()
    photos_arr = p.parse('resources/input/a_example.txt')
    for idx, photo in enumerate(photos_arr[:-1]):
        score = calcInterest(photo, photos_arr[idx+1])
        print("photo 1 tags " + ','.join(photo.tags))
        print("photo 2 tags " + ','.join(photos_arr[idx+1].tags))
        print(score)
        print("--------------")
    score = calcInterest(photos_arr[0], photos_arr[3])
    print(score)