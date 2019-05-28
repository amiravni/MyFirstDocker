# encoding: utf-8
# module cairo._cairo calls itself cairo
# from /usr/lib/python3/dist-packages/cairo/_cairo.cpython-35m-x86_64-linux-gnu.so
# by generator 1.147
# no doc

# imports
import cairo as __cairo


# Variables with simple values

ANTIALIAS_DEFAULT = 0
ANTIALIAS_GRAY = 2
ANTIALIAS_NONE = 1
ANTIALIAS_SUBPIXEL = 3

CONTENT_ALPHA = 8192
CONTENT_COLOR = 4096

CONTENT_COLOR_ALPHA = 12288

EXTEND_NONE = 0
EXTEND_PAD = 3
EXTEND_REFLECT = 2
EXTEND_REPEAT = 1

FILL_RULE_EVEN_ODD = 1

FILL_RULE_WINDING = 0

FILTER_BEST = 2
FILTER_BILINEAR = 4
FILTER_FAST = 0
FILTER_GAUSSIAN = 5
FILTER_GOOD = 1
FILTER_NEAREST = 3

FONT_SLANT_ITALIC = 1
FONT_SLANT_NORMAL = 0
FONT_SLANT_OBLIQUE = 2

FONT_WEIGHT_BOLD = 1
FONT_WEIGHT_NORMAL = 0

FORMAT_A1 = 3
FORMAT_A8 = 2
FORMAT_ARGB32 = 0

FORMAT_RGB16_565 = 4

FORMAT_RGB24 = 1

HAS_ATSUI_FONT = 0

HAS_FT_FONT = 1

HAS_GLITZ_SURFACE = 0

HAS_IMAGE_SURFACE = 1

HAS_PDF_SURFACE = 1

HAS_PNG_FUNCTIONS = 1

HAS_PS_SURFACE = 1

HAS_QUARTZ_SURFACE = 0

HAS_SVG_SURFACE = 1

HAS_USER_FONT = 1

HAS_WIN32_FONT = 0
HAS_WIN32_SURFACE = 0

HAS_XCB_SURFACE = 1

HAS_XLIB_SURFACE = 1

HINT_METRICS_DEFAULT = 0
HINT_METRICS_OFF = 1
HINT_METRICS_ON = 2

HINT_STYLE_DEFAULT = 0
HINT_STYLE_FULL = 4
HINT_STYLE_MEDIUM = 3
HINT_STYLE_NONE = 1
HINT_STYLE_SLIGHT = 2

LINE_CAP_BUTT = 0
LINE_CAP_ROUND = 1
LINE_CAP_SQUARE = 2

LINE_JOIN_BEVEL = 2
LINE_JOIN_MITER = 0
LINE_JOIN_ROUND = 1

OPERATOR_ADD = 12
OPERATOR_ATOP = 5
OPERATOR_CLEAR = 0
OPERATOR_DEST = 6

OPERATOR_DEST_ATOP = 10
OPERATOR_DEST_IN = 8
OPERATOR_DEST_OUT = 9
OPERATOR_DEST_OVER = 7

OPERATOR_IN = 3
OPERATOR_OUT = 4
OPERATOR_OVER = 2
OPERATOR_SATURATE = 13
OPERATOR_SOURCE = 1
OPERATOR_XOR = 11

PATH_CLOSE_PATH = 3

PATH_CURVE_TO = 2

PATH_LINE_TO = 1

PATH_MOVE_TO = 0

PS_LEVEL_2 = 0
PS_LEVEL_3 = 1

REGION_OVERLAP_IN = 0
REGION_OVERLAP_OUT = 1
REGION_OVERLAP_PART = 2

SUBPIXEL_ORDER_BGR = 2
SUBPIXEL_ORDER_DEFAULT = 0
SUBPIXEL_ORDER_RGB = 1
SUBPIXEL_ORDER_VBGR = 4
SUBPIXEL_ORDER_VRGB = 3

version = '1.10.0'

# functions

def cairo_version(*args, **kwargs): # real signature unknown
    pass

def cairo_version_string(*args, **kwargs): # real signature unknown
    pass

# classes

class Context(object):
    # no doc
    def append_path(self, *args, **kwargs): # real signature unknown
        pass

    def arc(self, *args, **kwargs): # real signature unknown
        pass

    def arc_negative(self, *args, **kwargs): # real signature unknown
        pass

    def clip(self, *args, **kwargs): # real signature unknown
        pass

    def clip_extents(self, *args, **kwargs): # real signature unknown
        pass

    def clip_preserve(self, *args, **kwargs): # real signature unknown
        pass

    def close_path(self, *args, **kwargs): # real signature unknown
        pass

    def copy_clip_rectangle_list(self, *args, **kwargs): # real signature unknown
        pass

    def copy_page(self, *args, **kwargs): # real signature unknown
        pass

    def copy_path(self, *args, **kwargs): # real signature unknown
        pass

    def copy_path_flat(self, *args, **kwargs): # real signature unknown
        pass

    def curve_to(self, *args, **kwargs): # real signature unknown
        pass

    def device_to_user(self, *args, **kwargs): # real signature unknown
        pass

    def device_to_user_distance(self, *args, **kwargs): # real signature unknown
        pass

    def fill(self, *args, **kwargs): # real signature unknown
        pass

    def fill_extents(self, *args, **kwargs): # real signature unknown
        pass

    def fill_preserve(self, *args, **kwargs): # real signature unknown
        pass

    def font_extents(self, *args, **kwargs): # real signature unknown
        pass

    def get_antialias(self, *args, **kwargs): # real signature unknown
        pass

    def get_current_point(self, *args, **kwargs): # real signature unknown
        pass

    def get_dash(self, *args, **kwargs): # real signature unknown
        pass

    def get_dash_count(self, *args, **kwargs): # real signature unknown
        pass

    def get_fill_rule(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def get_group_target(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_cap(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_join(self, *args, **kwargs): # real signature unknown
        pass

    def get_line_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def get_miter_limit(self, *args, **kwargs): # real signature unknown
        pass

    def get_operator(self, *args, **kwargs): # real signature unknown
        pass

    def get_scaled_font(self, *args, **kwargs): # real signature unknown
        pass

    def get_source(self, *args, **kwargs): # real signature unknown
        pass

    def get_target(self, *args, **kwargs): # real signature unknown
        pass

    def get_tolerance(self, *args, **kwargs): # real signature unknown
        pass

    def glyph_extents(self, *args, **kwargs): # real signature unknown
        pass

    def glyph_path(self, *args, **kwargs): # real signature unknown
        pass

    def has_current_point(self, *args, **kwargs): # real signature unknown
        pass

    def identity_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def in_fill(self, *args, **kwargs): # real signature unknown
        pass

    def in_stroke(self, *args, **kwargs): # real signature unknown
        pass

    def line_to(self, *args, **kwargs): # real signature unknown
        pass

    def mask(self, *args, **kwargs): # real signature unknown
        pass

    def mask_surface(self, *args, **kwargs): # real signature unknown
        pass

    def move_to(self, *args, **kwargs): # real signature unknown
        pass

    def new_path(self, *args, **kwargs): # real signature unknown
        pass

    def new_sub_path(self, *args, **kwargs): # real signature unknown
        pass

    def paint(self, *args, **kwargs): # real signature unknown
        pass

    def paint_with_alpha(self, *args, **kwargs): # real signature unknown
        pass

    def path_extents(self, *args, **kwargs): # real signature unknown
        pass

    def pop_group(self, *args, **kwargs): # real signature unknown
        pass

    def pop_group_to_source(self, *args, **kwargs): # real signature unknown
        pass

    def push_group(self, *args, **kwargs): # real signature unknown
        pass

    def push_group_with_content(self, *args, **kwargs): # real signature unknown
        pass

    def rectangle(self, *args, **kwargs): # real signature unknown
        pass

    def rel_curve_to(self, *args, **kwargs): # real signature unknown
        pass

    def rel_line_to(self, *args, **kwargs): # real signature unknown
        pass

    def rel_move_to(self, *args, **kwargs): # real signature unknown
        pass

    def reset_clip(self, *args, **kwargs): # real signature unknown
        pass

    def restore(self, *args, **kwargs): # real signature unknown
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        pass

    def save(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def select_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def set_antialias(self, *args, **kwargs): # real signature unknown
        pass

    def set_dash(self, *args, **kwargs): # real signature unknown
        pass

    def set_fill_rule(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def set_font_size(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_cap(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_join(self, *args, **kwargs): # real signature unknown
        pass

    def set_line_width(self, *args, **kwargs): # real signature unknown
        pass

    def set_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def set_miter_limit(self, *args, **kwargs): # real signature unknown
        pass

    def set_operator(self, *args, **kwargs): # real signature unknown
        pass

    def set_scaled_font(self, *args, **kwargs): # real signature unknown
        pass

    def set_source(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_rgb(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_rgba(self, *args, **kwargs): # real signature unknown
        pass

    def set_source_surface(self, *args, **kwargs): # real signature unknown
        pass

    def set_tolerance(self, *args, **kwargs): # real signature unknown
        pass

    def show_glyphs(self, *args, **kwargs): # real signature unknown
        pass

    def show_page(self, *args, **kwargs): # real signature unknown
        pass

    def show_text(self, *args, **kwargs): # real signature unknown
        pass

    def stroke(self, *args, **kwargs): # real signature unknown
        pass

    def stroke_extents(self, *args, **kwargs): # real signature unknown
        pass

    def stroke_preserve(self, *args, **kwargs): # real signature unknown
        pass

    def text_extents(self, *args, **kwargs): # real signature unknown
        pass

    def text_path(self, *args, **kwargs): # real signature unknown
        pass

    def transform(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        pass

    def user_to_device(self, *args, **kwargs): # real signature unknown
        pass

    def user_to_device_distance(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class FontFace(object):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class FontOptions(object):
    # no doc
    def get_antialias(self, *args, **kwargs): # real signature unknown
        pass

    def get_hint_metrics(self, *args, **kwargs): # real signature unknown
        pass

    def get_hint_style(self, *args, **kwargs): # real signature unknown
        pass

    def get_subpixel_order(self, *args, **kwargs): # real signature unknown
        pass

    def set_antialias(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_metrics(self, *args, **kwargs): # real signature unknown
        pass

    def set_hint_style(self, *args, **kwargs): # real signature unknown
        pass

    def set_subpixel_order(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Pattern(object):
    # no doc
    def get_extend(self, *args, **kwargs): # real signature unknown
        pass

    def get_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def set_extend(self, *args, **kwargs): # real signature unknown
        pass

    def set_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Gradient(__cairo.Pattern):
    # no doc
    def add_color_stop_rgb(self, *args, **kwargs): # real signature unknown
        pass

    def add_color_stop_rgba(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Surface(object):
    # no doc
    def copy_page(self, *args, **kwargs): # real signature unknown
        pass

    def create_similar(self, *args, **kwargs): # real signature unknown
        pass

    def finish(self, *args, **kwargs): # real signature unknown
        pass

    def flush(self, *args, **kwargs): # real signature unknown
        pass

    def get_content(self, *args, **kwargs): # real signature unknown
        pass

    def get_device_offset(self, *args, **kwargs): # real signature unknown
        pass

    def get_fallback_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_options(self, *args, **kwargs): # real signature unknown
        pass

    def mark_dirty(self, *args, **kwargs): # real signature unknown
        pass

    def mark_dirty_rectangle(self, *args, **kwargs): # real signature unknown
        pass

    def set_device_offset(self, *args, **kwargs): # real signature unknown
        pass

    def set_fallback_resolution(self, *args, **kwargs): # real signature unknown
        pass

    def show_page(self, *args, **kwargs): # real signature unknown
        pass

    def write_to_png(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ImageSurface(__cairo.Surface):
    # no doc
    @classmethod
    def create_for_data(cls, *args, **kwargs): # real signature unknown
        pass

    @classmethod
    def create_from_png(cls, *args, **kwargs): # real signature unknown
        pass

    def format_stride_for_width(self, *args, **kwargs): # real signature unknown
        pass

    def get_data(self, *args, **kwargs): # real signature unknown
        pass

    def get_format(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_stride(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class LinearGradient(__cairo.Gradient):
    # no doc
    def get_linear_points(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class Matrix(object):
    # no doc
    @classmethod
    def init_rotate(cls, *args, **kwargs): # real signature unknown
        pass

    def invert(self, *args, **kwargs): # real signature unknown
        pass

    def multiply(self, *args, **kwargs): # real signature unknown
        pass

    def rotate(self, *args, **kwargs): # real signature unknown
        pass

    def scale(self, *args, **kwargs): # real signature unknown
        pass

    def transform_distance(self, *args, **kwargs): # real signature unknown
        pass

    def transform_point(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __getitem__(self, *args, **kwargs): # real signature unknown
        """ Return self[key]. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    def __mul__(self, *args, **kwargs): # real signature unknown
        """ Return self*value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __repr__(self, *args, **kwargs): # real signature unknown
        """ Return repr(self). """
        pass

    def __rmul__(self, *args, **kwargs): # real signature unknown
        """ Return value*self. """
        pass

    __hash__ = None


class PDFSurface(__cairo.Surface):
    # no doc
    def set_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class PSSurface(__cairo.Surface):
    # no doc
    def dsc_begin_page_setup(self, *args, **kwargs): # real signature unknown
        pass

    def dsc_begin_setup(self, *args, **kwargs): # real signature unknown
        pass

    def dsc_comment(self, *args, **kwargs): # real signature unknown
        pass

    def get_eps(self, *args, **kwargs): # real signature unknown
        pass

    def ps_level_to_string(self, *args, **kwargs): # real signature unknown
        pass

    def restrict_to_level(self, *args, **kwargs): # real signature unknown
        pass

    def set_eps(self, *args, **kwargs): # real signature unknown
        pass

    def set_size(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class RadialGradient(__cairo.Gradient):
    # no doc
    def get_radial_circles(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class RectangleInt(object):
    # no doc
    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    def __str__(self, *args, **kwargs): # real signature unknown
        """ Return str(self). """
        pass

    height = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """height of the rectangle"""

    width = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """width of the rectangle"""

    x = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """X coordinate of the left side of the rectangle"""

    y = property(lambda self: object(), lambda self, v: None, lambda self: None)  # default
    """Y coordinate of the the top side of the rectangle"""


    __hash__ = None


class Region(object):
    # no doc
    def contains_point(self, *args, **kwargs): # real signature unknown
        pass

    def contains_rectangle(self, *args, **kwargs): # real signature unknown
        pass

    def copy(self, *args, **kwargs): # real signature unknown
        pass

    def equal(self, *args, **kwargs): # real signature unknown
        pass

    def get_extents(self, *args, **kwargs): # real signature unknown
        pass

    def get_rectangle(self, *args, **kwargs): # real signature unknown
        pass

    def intersect(self, *args, **kwargs): # real signature unknown
        pass

    def is_empty(self, *args, **kwargs): # real signature unknown
        pass

    def num_rectangles(self, *args, **kwargs): # real signature unknown
        pass

    def subtract(self, *args, **kwargs): # real signature unknown
        pass

    def translate(self, *args, **kwargs): # real signature unknown
        pass

    def union(self, *args, **kwargs): # real signature unknown
        pass

    def xor(self, *args, **kwargs): # real signature unknown
        pass

    def __eq__(self, *args, **kwargs): # real signature unknown
        """ Return self==value. """
        pass

    def __ge__(self, *args, **kwargs): # real signature unknown
        """ Return self>=value. """
        pass

    def __gt__(self, *args, **kwargs): # real signature unknown
        """ Return self>value. """
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    def __le__(self, *args, **kwargs): # real signature unknown
        """ Return self<=value. """
        pass

    def __lt__(self, *args, **kwargs): # real signature unknown
        """ Return self<value. """
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass

    def __ne__(self, *args, **kwargs): # real signature unknown
        """ Return self!=value. """
        pass

    __hash__ = None


class ScaledFont(object):
    # no doc
    def extents(self, *args, **kwargs): # real signature unknown
        pass

    def get_font_face(self, *args, **kwargs): # real signature unknown
        pass

    def get_scale_matrix(self, *args, **kwargs): # real signature unknown
        pass

    def text_extents(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class SolidPattern(__cairo.Pattern):
    # no doc
    def get_rgba(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class SurfacePattern(__cairo.Pattern):
    # no doc
    def get_filter(self, *args, **kwargs): # real signature unknown
        pass

    def get_surface(self, *args, **kwargs): # real signature unknown
        pass

    def set_filter(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class SVGSurface(__cairo.Surface):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class ToyFontFace(__cairo.FontFace):
    # no doc
    def get_family(self, *args, **kwargs): # real signature unknown
        pass

    def get_slant(self, *args, **kwargs): # real signature unknown
        pass

    def get_weight(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class XCBSurface(__cairo.Surface):
    # no doc
    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


class XlibSurface(__cairo.Surface):
    # no doc
    def get_depth(self, *args, **kwargs): # real signature unknown
        pass

    def get_height(self, *args, **kwargs): # real signature unknown
        pass

    def get_width(self, *args, **kwargs): # real signature unknown
        pass

    def __init__(self, *args, **kwargs): # real signature unknown
        pass

    @staticmethod # known case of __new__
    def __new__(*args, **kwargs): # real signature unknown
        """ Create and return a new object.  See help(type) for accurate signature. """
        pass


# variables with complex values

CAPI = None # (!) real value is '<capsule object "cairo.CAPI" at 0x7f7e42491600>'

version_info = (
    1,
    10,
    0,
)

__loader__ = None # (!) real value is '<_frozen_importlib_external.ExtensionFileLoader object at 0x7f7e429be0b8>'

__spec__ = None # (!) real value is "ModuleSpec(name='cairo._cairo', loader=<_frozen_importlib_external.ExtensionFileLoader object at 0x7f7e429be0b8>, origin='/usr/lib/python3/dist-packages/cairo/_cairo.cpython-35m-x86_64-linux-gnu.so')"

