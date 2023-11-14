# Template of Finger class

# Relationship 

# Finger
# box
# fingerIndex
# mask
# pairs of keypoints


# Three fingerBone boxes with one figner's root point/
class Finger:
    def __init__(self, fingerIndex) -> None:
        assert fingerIndex in [0, 1, 2, 3, 4], "fingerIndex is not in the list [0, 1, 2, 3, 4]"
        print("Created Object finger" + str(fingerIndex) ) 
        self.fingerIndex = fingerIndex

        # fingerIndex => keypoints index of the finger
        # keypoints index => index of root point of the finger

        # 1 root point + 3 bone boxes
        root_point = None
        self.y0 = root_point
        self.box1 = dict()
        self.box2 = dict()
        self.box3 = dict()

        # bone box property: 
        # <center_point> = center of the box
        # <vector> = 2D vector started from center point pointing to the y_bigger keypoint, the length of vector is half length of the 'height' of the box of bone.
        # <conner points> = 'left_top', 'left_bottom', 'right_top', 'right_bottom'
        self.box1['center_point'] = None
        self.box1['vector'] = None 
        self.box1['left_top'] = None; self.box1['left_bottom'] = None
        self.box1['right_top'] = None; self.box1['right_bottom'] = None

        self.box2['center_point'] = None
        self.box2['vector'] = None 
        self.box2['left_top'] = None; self.box1['left_bottom'] = None
        self.box2['right_top'] = None; self.box1['right_bottom'] = None

        self.box3['center_point'] = None
        self.box3['vector'] = None 
        self.box3['left_top'] = None; self.box1['left_bottom'] = None
        self.box3['right_top'] = None; self.box1['right_bottom'] = None
