import myarrayutils.sort as sort


def test_BubbleSort_empty_array():
    arr = []
    expected = []
    sort.BubbleSort(arr)
    assert arr == expected


def test_BubbleSort_empty_array_with_reverse():
    arr = []
    expected = []
    sort.BubbleSort(arr, reverse=True)
    assert arr == expected


def test_BubbleSort_int_array():
    arr = [1, 4, 77, 5, 6, 12, 24]
    expected = [1, 4, 5, 6, 12, 24, 77]
    sort.BubbleSort(arr)
    assert arr == expected


def test_BubbleSort_int_array_with_reverse():
    arr = [1, 4, 77, 5, 6, 12, 24]
    expected = [77, 24, 12, 6, 5, 4, 1]
    sort.BubbleSort(arr, reverse=True)
    assert arr == expected


def test_BubbleSort_int_array_with_cmp():
    arr = [1, 4, 77, 5, 6, 12, 24]
    expected = [1, 4, 5, 6, 12, 24, 77]
    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.BubbleSort(arr, cmp=cmp)
    assert arr == expected


def test_BubbleSort_int_array_with_reverse_and_cmp():
    arr = [1, 4, 77, 5, 6, 12, 24]
    expected = [77, 24, 12, 6, 5, 4, 1]
    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.BubbleSort(arr, reverse=True, cmp=cmp)
    assert arr == expected


def test_BubbleSort_sorted_int_array():
    arr = [1, 2, 3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    sort.BubbleSort(arr)
    assert arr == expected


def test_BubbleSort_sorted_int_array_with_reverse():
    arr = [1, 2, 3, 4, 5, 6, 7]
    expected = [7, 6, 5, 4, 3, 2, 1]
    sort.BubbleSort(arr, reverse=True)
    assert arr == expected


def test_BubbleSort_sorted_int_array_with_cmp():
    arr = [1, 2, 3, 4, 5, 6, 7]
    expected = [1, 2, 3, 4, 5, 6, 7]
    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.BubbleSort(arr, cmp=cmp)
    assert arr == expected


def test_BubbleSort_sorted_int_array_with_reverse_and_cmp():
    arr = [1, 2, 3, 4, 5, 6, 7]
    expected = [7, 6, 5, 4, 3, 2, 1]
    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.BubbleSort(arr, reverse=True, cmp=cmp)
    assert arr == expected


def test_BubbleSort_string_array():
    arr = ['test', 'quick', 'sort', 'with', 'string',
           'array', 'hope', 'all', 'tests', 'are', 'passed']
    expected = ['all', 'are', 'array', 'hope', 'passed',
                'quick', 'sort', 'string', 'test', 'tests', 'with']
    sort.BubbleSort(arr)
    assert arr == expected


def test_BubbleSort_string_array_with_reverse():
    arr = ['test', 'quick', 'sort', 'with', 'string',
           'array', 'hope', 'all', 'tests', 'are', 'passed']
    expected = ['with', 'tests', 'test', 'string', 'sort',
                'quick', 'passed', 'hope', 'array', 'are', 'all']
    sort.BubbleSort(arr, reverse=True)
    assert arr == expected


def test_BubbleSort_string_array_with_cmp():
    arr = ['test', 'quick', 'sort', 'with', 'string',
           'array', 'hope', 'all', 'tests', 'are', 'passed']
    expected = ['all', 'are', 'array', 'hope', 'passed',
                'quick', 'sort', 'string', 'test', 'tests', 'with']

    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.BubbleSort(arr, cmp=cmp)
    assert arr == expected


def test_BubbleSort_string_array_with_reverse_and_cmp():
    arr = ['test', 'quick', 'sort', 'with', 'string',
           'array', 'hope', 'all', 'tests', 'are', 'passed']
    expected = ['with', 'tests', 'test', 'string', 'sort',
                'quick', 'passed', 'hope', 'array', 'are', 'all']

    def cmp(x, y): return -1 if x < y else 1 if x > y else 0
    sort.BubbleSort(arr, reverse=True, cmp=cmp)
    assert arr == expected


def test_BubbleSort_dict_array_with_cmp():
    arr = [
        {'id': 1, 'age': 20},
        {'id': 2, 'age': 12},
        {'id': 3, 'age': 26},
        {'id': 4, 'age': 30},
        {'id': 5, 'age': 24},
        {'id': 6, 'age': 19},
        {'id': 7, 'age': 11},
    ]
    expected = [
        {'id': 7, 'age': 11},
        {'id': 2, 'age': 12},
        {'id': 6, 'age': 19},
        {'id': 1, 'age': 20},
        {'id': 5, 'age': 24},
        {'id': 3, 'age': 26},
        {'id': 4, 'age': 30},
    ]
    def cmp(x, y): return - \
        1 if x['age'] < y['age'] else 1 if x['age'] > y['age'] else 0
    sort.BubbleSort(arr, cmp=cmp)
    assert arr == expected


def test_BubbleSort_long_int_array():
    arr = [-41491, 23027, 37549, -86228, 24723, 8516, -83818, 30223, -33431, -10888, 91460, -13695, 12336, 6898, 79866,
           -79109, 22664, 21139, -92010, 15314, 51719, -
           17905, 37148, 29079, -95800, 82548, 8690, -15599, 31931, -77813,
           561, 46989, 9519, 1489, 53709, 82605, 10148, -
           44673, 31907, -65768, -31564, 49037, -29907, 44518, -83228,
           22561, -92048, 88989, 50231, 66738, 95463, -45643, -
           32598, -67134, -19728, 2612, -23568, 87626, -56488,
           62442, 69260, -756, 276, 78779, 36819, -54929, 92408, -
           7468, 42799, -48965, 95283, -7829, 10288, 77167,
           38894, 31736, 32241, 72864, 80321, -60819, 36709, 9799, -
           50627, 59084, 34021, -6529, 26438, -61179, 80114,
           -31716, 49915, -58159, -30791, -39732, -8060, -
           44538, 35477, -40348, 85988, 91392, 19287, 83967, 8064,
           -41320, -63261, 91150, 94965, 35472, -33231, 16445, -
           98647, 1356, -79184, -5336, 89904, 69693, -5309, -80126,
           12963, -34530, -8024, -59718, 72028, 53946, -1774, -
           51106, -56593, 19195, 76543, -1104, -61377, -39916,
           -1066, 80472, -25256, -273, 42966, 1275, 53341, -38696, -
           82604, -40543, 31798, -60532, -15584, -90288, 43247,
           -33232, -8893, -23202, -74053, -44039, 38534, -
           85287, 14711, -78876, 84749, 80539, -28085, -36327, -28437,
           -26354, 86105, -76100, 17172, 36532, 39646, -84498, -
           36547, 52666, -4935, 13207, 11368, -91365, -73331,
           -41207, 94218, -46155, -953, -66664, 16884, 35480, -
           76440, 38717, -54140, -99891, -59544, 80633, 89663,
           59545, 81813, -3931, 49735, -6128, -21440, 9786, -
           47920, -4420, -32997, -74330, -55201, -54212, -4274,
           -90335, -73988, -45361, -2683, 22132, -89395, -5506, -
           15938, -35592, -32832, -60332, -20692, -28174, 96927,
           -52246, -68940, -49006, 91360, -77636, 98758, -43098, -
           52032, 12839, -21572, -81256, -70732, -4540, -78662,
           -99324, -98141, 87184, 93587, 67836, 27189, -25628, -
           46346, -40099, -48029, -89520, -14809, -53566, -14370,
           -77775, -92691, 74806, 34510, 45913, -12137, 13817, -
           54706, 46709, -14392, 98738, -49749, 5840, -86291,
           -27837, 41641, 38689, 38360, -60509, -4763, -5751, -
           70853, -48502, 59655, 37546, 57467, 75326, 1649, 48820,
           -56024, 57886, -14360, -26335, 88594, -17896, 15519, -
           78891, -78079, 44232, 6992, 55567, 2070, -52905, 83549,
           67794, 3936, 15347, -82845, 34731, -44073, -90251, -
           41627, -24996, 17305, -33235, -49098, -40995, -56695,
           -2690, 8306, -72998, 16983, 96590, 9173, -77192, -
           51593, 96240, 7040, -20565, -55795, -90400, 69175, 34517,
           88674, 32233, -20301, -22433, -46191, -94119, 77143, 97853, -
           58540, -50039, 61717, -81882, -91730, -27758,
           -70800, -26471, 61960, -98860, -39438, 41300, 5952, -
           50012, 2304, -60688, 76386, -43314, -52345, 58641,
           -20915, 94990, 45680, -86292, 82776, -65762, 27531, 54334, -
           22098, -35985, -98026, -52172, 64812, -84337,
           -74261, 18742, 53807, 1656, -23719, -45663, -27367, -
           43001, 25423, -69651, 66026, 3780, 44103, -91563,
           -24385, 15534, 49014, 34117, 81391, -48062, 36641, -
           52313, 62806, -94558, -77059, 16611, 32701, -43097,
           28976, -66502, 90267, -22755, 80556, -65577, 84370, 90871, -
           40312, -11819, -44159, 72927, -48685, -83182,
           -55964, 78855, 10100, -61486, -40188, -78259, -
           28766, 67871, 72963, 34307, 32362, -24716, -49347, 75268,
           83947, -57385, 11468, -20448, -86161, 1998, 15439, -
           13456, 6956, 9185, -18525, -21365, -27431, -40741, -3447,
           91799, 53005, 37374, 66586, 57928, -60908, 49386, -
           45033, 96326, 94072, -9560, 89077, 91303, 3874, 81883,
           30645, 34494, 51631, -70406, 84904, 15028, 44803, -
           77355, 34301, 23065, 25870, -37028, -74525, 3758, -72328,
           95560, 21779, 72888, 27666, -50220, 5249, 34498, -
           72493, -68385, 33019, -58597, 38156, -14558, -38023,
           -27613, 3093, 11745, 31495, -31556, 90913, -80118, -
           66040, 12352, -765, -76468, -82161, 29601, 86522, 95197,
           89533, -99397, -89660, -23038, -30821, -54128, -
           88544, 47714, -24014, 89637, 17584, -95951, 19004, -89383,
           -83688, -57100, -7493, -9729, -23157, -38458, -31749, -
           89661, 95147, -12257, 44041, -30854, -56350, 21465,
           -24854, 97752, 12007, -36558, -11463, -85491, -
           56084, 15332, -77266, 68844, -52530, -66264, 44726, -83493,
           12714, 52115, 26119, -76304, 52058, 74292, -50433, -
           86809, 18868, -44525, -94767, -62826, -53333, 99992,
           -40958, 74681, 39405, 52472, -94096, 46488, 67041, -
           28787, -67105, 61568, -34046, 29156, 55506, -30799,
           -78628, 61418, -81117, -42039, -79341, 39600, -
           8747, 28757, -32098, -93395, 75342, -88704, 69415, -96440,
           -84846, 35729, 72146, -80337, -87684, -25071, -98094, -
           59128, -94464, -34332, 86374, 45714, 21794, 98994,
           -94266, -68238, -2652, 67462, 54792, -16001, 33601, -
           35088, -23079, 50886, 95317, -83465, -1113, 75832,
           -7961, -5934, 27131, 38156, 7469, 58443, -77927, -
           96181, -94804, 15958, 6590, -63325, 89201, -430, -25434,
           -97456, -40806, -44659, 12091, -31223, 31312, 87579, -
           28871, 39472, 28689, 64003, -46237, -65764, -18924,
           16074, 8718, -83579, 19641, -99076, 39764, 51033, -
           84674, 37867, -25185, -66417, -43706, -28096, -4397,
           14213, -89974, 40452, 45705, -52575, 54121, -68958, -
           40507, -23157, 13155, 11979, 80848, -82838, 32453,
           70161, 74695, -98930, -51136, 75040, 30817, -26204, 25866, -
           98861, 23453, -77091, 86819, -24469, -98602,
           -35027, 40086, -87628, -67215, 10870, -36496, 49221, -
           13598, -50561, 79156, 78478, -8264, 97087, -17917,
           29691, 80500, 72770, -2876, -
           37473, 16008, 49485, 83865, 37868, 60299, 59866, -63710, 99080, -47582, -17955,
           30625, 86434, 44147, 76732, -88427, 78164, 45815, -
           47580, -92009, -85564, -4274, 60672, -46273, -75267,
           59110, 82438, 73648, 13121, -13887, 43218, -369, -10228, -
           67454, 90950, -6911, -26997, 17710, 82278, -42748,
           -35936, -26951, 18944, 7776, 13833, -50235, 96501, -
           85969, -67866, -89602, 28844, -42119, 98739, 37681,
           52808, 17407, 72344, -51229, 58709, 42984, -82526, -
           13091, 95588, 6363, -59739, -70540, 59925, -16977, 14249,
           35535, -24980, 87776, 44708, -3844, -992, 24255, 70772, -
           61885, 44546, 65295, -75476, 60311, 4378, 13365,
           -59700, -67694, 35735, 37277, -11679, 24996, -
           44485, 90397, 45601, 12566, 50681, -47642, 82935, -51789,
           -74293, 90016, -14510, -18184, -5271, -48291, -7950, -
           14050, 77603, -2064, -98691, 16305, 9335, -84818,
           24192, -81829, -1352, 16313, -17587, 63760, -
           29906, 62751, 94309, 60193, -59571, 20758, 85574, -54857, 28966,
           -50824, -58493, -30995, -79714, -33516, -37715, 75720, -
           88274, -53358, -61906, -53453, -24190, -8678, 26370,
           27388, 88494, 8295, 60955, -59756, 30311, 51639, 97382, -
           22706, 1213, 48510, -75713, 64760, -2556, -34321,
           -55732, -19219, -38397, -5791, -97817, -38598, 59125, -
           39952, -76086, 61832, 98631, -90372, -14237, 77585,
           72911, 52696, 8718, -61973, 83438, -17001, -23264, -
           34319, -91838, -406, -30252, 43299, 90476, 13372, -42028,
           35026, -86517, 52786, -71865, -48296, 3900, 54882, 23119, -
           58991, -59838, 84604, 66229, -3977, -94090,
           -17174, -13905, 61504, 9275, -27044, 95526, -75644, -
           39143, 76175, 69278, -65100, 95173, 34236, -21122,
           14400, 85486, -58476, -74439, -25639, -48045, -86605, -
           7405, 37694, -41813, -37105, 51636, -63814, -61416,
           584, -45693, -31768, -41699, 19262, -25832, 73077, -
           8541, -21476, 45889, -41935, 23284, -64835, -58485,
           27253, 43121, -92097, -41912, -9321, -89810, 31425, -
           76444, -97322, -91718, -97839, -3118, -32697, -70034,
           -45500, 54972, 97665, -82066, 86653, 19346, -
           50063, 19279, 98513, -68883, -83102, -48956, 85594, -61374,
           -70808, -2523, 94615, -21967, 58395, -
           60930, 42440, 61441, 2494, 25361, -76654, 20718, 67921, 52536, 21563,
           85382, 23967, -58025, -3003, -37452, 90944, -93315, -
           34992, 53624, 80383, -97027, -32807, -96997, -64448,
           84423, -92561, -68957, -26631, 40964, -54838, 79244, 7633, 75704, 82462, -1845]
    expected = [-99891, -99397, -99324, -99076, -98930, -98861, -98860, -98691, -98647, -98602, -98141, -98094, -98026,
                -97839, -97817, -97456, -97322, -97027, -96997, -
                96440, -96181, -95951, -95800, -94804, -94767, -94558,
                -94464, -94266, -94119, -94096, -94090, -93395, -
                93315, -92691, -92561, -92097, -92048, -92010, -92009,
                -91838, -91730, -91718, -91563, -91365, -90400, -
                90372, -90335, -90288, -90251, -89974, -89810, -89661,
                -89660, -89602, -89520, -89395, -89383, -88704, -
                88544, -88427, -88274, -87684, -87628, -86809, -86605,
                -86517, -86292, -86291, -86228, -86161, -85969, -
                85564, -85491, -85287, -84846, -84818, -84674, -84498,
                -84337, -83818, -83688, -83579, -83493, -83465, -
                83228, -83182, -83102, -82845, -82838, -82604, -82526,
                -82161, -82066, -81882, -81829, -81256, -81117, -
                80337, -80126, -80118, -79714, -79341, -79184, -79109,
                -78891, -78876, -78662, -78628, -78259, -78079, -
                77927, -77813, -77775, -77636, -77355, -77266, -77192,
                -77091, -77059, -76654, -76468, -76444, -76440, -
                76304, -76100, -76086, -75713, -75644, -75476, -75267,
                -74525, -74439, -74330, -74293, -74261, -74053, -
                73988, -73331, -72998, -72493, -72328, -71865, -70853,
                -70808, -70800, -70732, -70540, -70406, -70034, -
                69651, -68958, -68957, -68940, -68883, -68385, -68238,
                -67866, -67694, -67454, -67215, -67134, -67105, -
                66664, -66502, -66417, -66264, -66040, -65768, -65764,
                -65762, -65577, -65100, -64835, -64448, -63814, -
                63710, -63325, -63261, -62826, -61973, -61906, -61885,
                -61486, -61416, -61377, -61374, -61179, -60930, -
                60908, -60819, -60688, -60532, -60509, -60332, -59838,
                -59756, -59739, -59718, -59700, -59571, -59544, -
                59128, -58991, -58597, -58540, -58493, -58485, -58476,
                -58159, -58025, -57385, -57100, -56695, -56593, -
                56488, -56350, -56084, -56024, -55964, -55795, -55732,
                -55201, -54929, -54857, -54838, -54706, -54212, -
                54140, -54128, -53566, -53453, -53358, -53333, -52905,
                -52575, -52530, -52345, -52313, -52246, -52172, -
                52032, -51789, -51593, -51229, -51136, -51106, -50824,
                -50627, -50561, -50433, -50235, -50220, -50063, -
                50039, -50012, -49749, -49347, -49098, -49006, -48965,
                -48956, -48685, -48502, -48296, -48291, -48062, -
                48045, -48029, -47920, -47642, -47582, -47580, -46346,
                -46273, -46237, -46191, -46155, -45693, -45663, -
                45643, -45500, -45361, -45033, -44673, -44659, -44538,
                -44525, -44485, -44159, -44073, -44039, -43706, -
                43314, -43098, -43097, -43001, -42748, -42119, -42039,
                -42028, -41935, -41912, -41813, -41699, -41627, -
                41491, -41320, -41207, -40995, -40958, -40806, -40741,
                -40543, -40507, -40348, -40312, -40188, -40099, -
                39952, -39916, -39732, -39438, -39143, -38696, -38598,
                -38458, -38397, -38023, -37715, -37473, -37452, -
                37105, -37028, -36558, -36547, -36496, -36327, -35985,
                -35936, -35592, -35088, -35027, -34992, -34530, -
                34332, -34321, -34319, -34046, -33516, -33431, -33235,
                -33232, -33231, -32997, -32832, -32807, -32697, -
                32598, -32098, -31768, -31749, -31716, -31564, -31556,
                -31223, -30995, -30854, -30821, -30799, -30791, -
                30252, -29907, -29906, -28871, -28787, -28766, -28437,
                -28174, -28096, -28085, -27837, -27758, -27613, -
                27431, -27367, -27044, -26997, -26951, -26631, -26471,
                -26354, -26335, -26204, -25832, -25639, -25628, -
                25434, -25256, -25185, -25071, -24996, -24980, -24854,
                -24716, -24469, -24385, -24190, -24014, -23719, -
                23568, -23264, -23202, -23157, -23157, -23079, -23038,
                -22755, -22706, -22433, -22098, -21967, -21572, -
                21476, -21440, -21365, -21122, -20915, -20692, -20565,
                -20448, -20301, -19728, -19219, -18924, -18525, -
                18184, -17955, -17917, -17905, -17896, -17587, -17174,
                -17001, -16977, -16001, -15938, -15599, -15584, -
                14809, -14558, -14510, -14392, -14370, -14360, -14237,
                -14050, -13905, -13887, -13695, -13598, -13456, -
                13091, -12257, -12137, -11819, -11679, -11463, -10888,
                -10228, -9729, -9560, -9321, -8893, -8747, -8678, -
                8541, -8264, -8060, -8024, -7961, -7950, -7829,
                -7493, -7468, -7405, -6911, -6529, -6128, -5934, -
                5791, -5751, -5506, -5336, -5309, -5271, -4935, -4763,
                -4540, -4420, -4397, -4274, -4274, -3977, -3931, -
                3844, -3447, -3118, -3003, -2876, -2690, -2683, -2652,
                -2556, -2523, -2064, -1845, -1774, -1352, -1113, -
                1104, -1066, -992, -953, -765, -756, -430, -406, -369,
                -273, 276, 561, 584, 1213, 1275, 1356, 1489, 1649, 1656, 1998, 2070, 2304, 2494, 2612, 3093, 3758, 3780,
                3874, 3900, 3936, 4378, 5249, 5840, 5952, 6363, 6590, 6898, 6956, 6992, 7040, 7469, 7633, 7776, 8064,
                8295, 8306, 8516, 8690, 8718, 8718, 9173, 9185, 9275, 9335, 9519, 9786, 9799, 10100, 10148, 10288,
                10870, 11368, 11468, 11745, 11979, 12007, 12091, 12336, 12352, 12566, 12714, 12839, 12963, 13121, 13155,
                13207, 13365, 13372, 13817, 13833, 14213, 14249, 14400, 14711, 15028, 15314, 15332, 15347, 15439, 15519,
                15534, 15958, 16008, 16074, 16305, 16313, 16445, 16611, 16884, 16983, 17172, 17305, 17407, 17584, 17710,
                18742, 18868, 18944, 19004, 19195, 19262, 19279, 19287, 19346, 19641, 20718, 20758, 21139, 21465, 21563,
                21779, 21794, 22132, 22561, 22664, 23027, 23065, 23119, 23284, 23453, 23967, 24192, 24255, 24723, 24996,
                25361, 25423, 25866, 25870, 26119, 26370, 26438, 27131, 27189, 27253, 27388, 27531, 27666, 28689, 28757,
                28844, 28966, 28976, 29079, 29156, 29601, 29691, 30223, 30311, 30625, 30645, 30817, 31312, 31425, 31495,
                31736, 31798, 31907, 31931, 32233, 32241, 32362, 32453, 32701, 33019, 33601, 34021, 34117, 34236, 34301,
                34307, 34494, 34498, 34510, 34517, 34731, 35026, 35472, 35477, 35480, 35535, 35729, 35735, 36532, 36641,
                36709, 36819, 37148, 37277, 37374, 37546, 37549, 37681, 37694, 37867, 37868, 38156, 38156, 38360, 38534,
                38689, 38717, 38894, 39405, 39472, 39600, 39646, 39764, 40086, 40452, 40964, 41300, 41641, 42440, 42799,
                42966, 42984, 43121, 43218, 43247, 43299, 44041, 44103, 44147, 44232, 44518, 44546, 44708, 44726, 44803,
                45601, 45680, 45705, 45714, 45815, 45889, 45913, 46488, 46709, 46989, 47714, 48510, 48820, 49014, 49037,
                49221, 49386, 49485, 49735, 49915, 50231, 50681, 50886, 51033, 51631, 51636, 51639, 51719, 52058, 52115,
                52472, 52536, 52666, 52696, 52786, 52808, 53005, 53341, 53624, 53709, 53807, 53946, 54121, 54334, 54792,
                54882, 54972, 55506, 55567, 57467, 57886, 57928, 58395, 58443, 58641, 58709, 59084, 59110, 59125, 59545,
                59655, 59866, 59925, 60193, 60299, 60311, 60672, 60955, 61418, 61441, 61504, 61568, 61717, 61832, 61960,
                62442, 62751, 62806, 63760, 64003, 64760, 64812, 65295, 66026, 66229, 66586, 66738, 67041, 67462, 67794,
                67836, 67871, 67921, 68844, 69175, 69260, 69278, 69415, 69693, 70161, 70772, 72028, 72146, 72344, 72770,
                72864, 72888, 72911, 72927, 72963, 73077, 73648, 74292, 74681, 74695, 74806, 75040, 75268, 75326, 75342,
                75704, 75720, 75832, 76175, 76386, 76543, 76732, 77143, 77167, 77585, 77603, 78164, 78478, 78779, 78855,
                79156, 79244, 79866, 80114, 80321, 80383, 80472, 80500, 80539, 80556, 80633, 80848, 81391, 81813, 81883,
                82278, 82438, 82462, 82548, 82605, 82776, 82935, 83438, 83549, 83865, 83947, 83967, 84370, 84423, 84604,
                84749, 84904, 85382, 85486, 85574, 85594, 85988, 86105, 86374, 86434, 86522, 86653, 86819, 87184, 87579,
                87626, 87776, 88494, 88594, 88674, 88989, 89077, 89201, 89533, 89637, 89663, 89904, 90016, 90267, 90397,
                90476, 90871, 90913, 90944, 90950, 91150, 91303, 91360, 91392, 91460, 91799, 92408, 93587, 94072, 94218,
                94309, 94615, 94965, 94990, 95147, 95173, 95197, 95283, 95317, 95463, 95526, 95560, 95588, 96240, 96326,
                96501, 96590, 96927, 97087, 97382, 97665, 97752, 97853, 98513, 98631, 98738, 98739, 98758, 98994, 99080,
                99992]
    sort.BubbleSort(arr)
    assert arr == expected
