import Evaluator
from Parser import Parser
from Slide import Slide

SAME_SIM = -1


class Solver:
    def __init__(self):
        self.photos_arr = []
        self.slide_arr = []
        self.mat = {}
        self.slideshow = []
        self.selected_slide_ndx = None
        self.last_similarity = None

    def create_slides(self, photos_arr):

        horizontal_slides = [Slide(h_photo) for h_photo in photos_arr if not h_photo.isVertical]

        vertical_photos = [v_photo for v_photo in photos_arr if v_photo.isVertical]

        vertical_slides = []
        for idx in range(0, len(vertical_photos) - 1, 2):
            vertical_slides.append(Slide(vertical_photos[idx], vertical_photos[idx+1]))

        slide_arr = horizontal_slides + vertical_slides

        return slide_arr

    def select_slide_idx(self):
        if len(self.slideshow) == 0:
            # dummy choice, slide 0
            return 0

        last_slide = self.slideshow[-1]
        self.last_similarity = {ndx: Evaluator.calcInterest(last_slide, self.slide_arr[ndx]) for ndx in range(len(self.slide_arr))}
        idx_score_pairs = self.last_similarity.items()
        best = max(idx_score_pairs, key=lambda p: p[1])
        return best[0]

    def solve(self, path):
        p = Parser()
        self.photos_arr = p.parse(path)
        self.slide_arr = self.create_slides(self.photos_arr)

        self.selected_slide_ndx = None
        self.slideshow = []

        step = 0
        while len(self.slide_arr) > 0:
            self.selected_slide_ndx = self.select_slide_idx()
            self.slideshow.append(self.slide_arr[self.selected_slide_ndx])
            del self.slide_arr[self.selected_slide_ndx]

            step += 1
            if step % 100 == 0:
                print(step)

    def output_solution(self, path):
        out_lines = []
        out_lines.append(str(len(self.slideshow)) + "\n")
        for slide in self.slideshow:
            out_lines.append(str(slide))

        with open(path, "w") as f:
            f.writelines(out_lines)


if __name__ == '__main__':
    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/a_example.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/a_example.txt")

    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/b_lovely_landscapes.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/b_lovely_landscapes.txt")

    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/c_memorable_moments.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/c_memorable_moments.txt")
    #
    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/d_pet_pictures.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/d_pet_pictures.txt")
    #
    slvr = Solver()
    slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/e_shiny_selfies.txt")
    slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/e_shiny_selfies.txt")