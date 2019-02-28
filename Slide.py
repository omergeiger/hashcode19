from Parser import Parser
import Evaluator
class Slide:
    def __init__(self,photo1,photo2=None):
        if photo2 is None:
            assert(not photo1.isVertical)
        else:
            assert(photo1.isVertical and photo2.isVertical)
        self.photo1 = photo1
        self.photo2 = photo2
        if (photo2 is not None):
            self.tags = photo1.tags.union(photo2.tags)
        else:
            self.tags = photo1.tags

    def __str__(self):
        if self.photo2 is None:
            out_str = f"{self.photo1.id}\n"
        else:
            out_str = f"{self.photo1.id} {self.photo2.id}\n"
        return out_str

if __name__ == '__main__':
    p = Parser()
    photos_arr = p.parse('resources/input/a_example.txt')

    slide_arr = [
        Slide(photos_arr[0]),
        Slide(photos_arr[1], photos_arr[2]),
        Slide(photos_arr[3])
    ]
    for idx, slide in enumerate(slide_arr[:-1]):
        score = Evaluator.calcInterest(slide, slide_arr[idx+1])
        print("slide 1 tags " + ','.join(slide.tags))
        print("slide 2 tags " + ','.join(slide_arr[idx+1].tags))
        print(score)
        print("--------------")
    #score = Evaluator.calcInterest(photos_arr[0], photos_arr[3])


