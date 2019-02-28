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

    def get_interest_mat(self, slide_arr):
        mat = {}
        num_slides = len(slide_arr)
        for idx1 in range(num_slides):
            row = {}
            for idx2 in range(num_slides):
                if idx1 == idx2:
                    sim = SAME_SIM
                else:
                    sim = Evaluator.calcInterest(slide_arr[idx1], slide_arr[idx2])
                row[idx2] = sim
            mat[idx1] = row
        return mat

    def remove_slide(self, idx):
        self.last_similarity = dict(self.mat[self.selected_slide_ndx])

        assert (idx in self.mat)
        del self.mat[self.selected_slide_ndx]
        for ref_idx in self.mat:
            assert idx in self.mat[ref_idx]
            del self.mat[ref_idx][idx]

    def select_slide_idx(self):
        if self.last_similarity is  None:
            # dummy choice, slide 0
            return 0
        idx_score_pairs = self.last_similarity.items()
        best = max(idx_score_pairs, key=lambda p: p[1])
        return best[0]

    def solve(self, path):
        p = Parser()
        self.photos_arr = p.parse(path)
        self.slide_arr = self.create_slides(self.photos_arr)

        print('got slides')

        self.mat = self.get_interest_mat(self.slide_arr)

        print('got mat')

        self.selected_slide_ndx = None
        self.slideshow = []

        step = 0
        while len(self.mat) > 0:
            self.selected_slide_ndx = self.select_slide_idx()
            self.slideshow.append(self.slide_arr[self.selected_slide_ndx])
            self.remove_slide(self.selected_slide_ndx)

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

    slvr = Solver()
    slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/b_lovely_landscapes.txt")
    slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/b_lovely_landscapes.txt")

    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/c_memorable_moments.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/c_memorable_moments.txt")
    #
    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/d_pet_pictures.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/d_pet_pictures.txt")
    #
    # slvr = Solver()
    # slvr.solve(path="/Users/ogeiger/git/hashcode19/resources/input/e_shiny_selfies.txt")
    # slvr.output_solution("/Users/ogeiger/git/hashcode19/resources/solutions/e_shiny_selfies.txt")