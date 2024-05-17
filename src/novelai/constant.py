from enum import Enum

from .types import HostInstance

HEADERS = {
    "Content-Type": "application/json",
    "Origin": "https://novelai.net",
    "Referer": "https://novelai.net",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
}


class Host(Enum):
    API = HostInstance(
        url="https://api.novelai.net", accept="application/x-zip-compressed"
    )
    WEB = HostInstance(url="https://image.novelai.net", accept="binary/octet-stream")


class Endpoint(Enum):
    LOGIN = "/user/login"
    USERDATA = "/user/data"
    IMAGE = "/ai/generate-image"


class Model(Enum):
    V3 = "nai-diffusion-3"
    ANIMEV3 = V3
    V3INP = "nai-diffusion-3-inpainting"
    ANIMEV3INP = V3INP
    FURRY = "nai-diffusion-furry"
    FURRYINP = "furry-diffusion-inpainting"
    FURRYV3 = "nai-diffusion-furry-3"


class Controlnet(Enum):
    PALETTESWAP = "hed"
    FORMLOCK = "midas"
    SCRIBBLER = "fake_scribble"
    BUILDINGCONTROL = "mlsd"
    LANDSCAPER = "uniformer"


class Action(Enum):
    GENERATE = "generate"
    INPAINT = "infill"
    IMG2IMG = "img2img"


class Resolution(Enum):
    SMALL_PORTRAIT = (512, 768)
    SMALL_LANDSCAPE = (768, 512)
    SMALL_SQUARE = (640, 640)
    NORMAL_PORTRAIT = (832, 1216)
    NORMAL_LANDSCAPE = (1216, 832)
    NORMAL_SQUARE = (1024, 1024)
    LARGE_PORTRAIT = (1024, 1536)
    LARGE_LANDSCAPE = (1536, 1024)
    LARGE_SQUARE = (1472, 1472)
    WALLPAPER_PORTRAIT = (1088, 1920)
    WALLPAPER_LANDSCAPE = (1920, 1088)


class Sampler(Enum):
    EULER = "k_euler"
    EULER_ANC = "k_euler_ancestral"
    DPM2S_ANC = "k_dpmpp_2s_ancestral"
    DPM2M = "k_dpmpp_2m"
    DPMSDE = "k_dpmpp_sde"
    DDIM = "ddim_v3"


class Noise(Enum):
    NATIVE = "native"
    KARRAS = "karras"
    EXPONENTIAL = "exponential"
    POLYEXPONENTIAL = "polyexponential"


class UndesiredPreset(Enum):
    HEAVY = [
        "nsfw",
        "{{worst quality}}",
        "[displeasing]",
        "{unusual pupils}",
        "guide lines",
        "{{unfinished}}",
        "{bad}",
        "url",
        "artist name",
        "{{tall image}}",
        "mosaic",
        "{sketch page}",
        "comic panel",
        "impact (font)",
        "[dated]",
        "{logo}",
        "ych",
        "{what}",
        "{where is your god now}",
        "{distorted text}",
        "repeated text",
        "{floating head}",
        "{1994}",
        "{widescreen}",
        "absolutely everyone",
        "sequence",
        "{compression artifacts}",
        "hard translated",
        "{cropped}",
        "{commissioner name}",
        "unknown text",
        "high contrast",
    ]
    LIGHT = [
        "nsfw",
        "{worst quality}",
        "guide lines",
        "unfinished",
        "bad",
        "url",
        "tall image",
        "widescreen",
        "compression artifacts",
        "unknown text",
    ]
    HUMAN = [
        "nsfw",
        "lowres",
        "{bad}",
        "error",
        "fewer",
        "extra",
        "missing",
        "worst quality",
        "jpeg artifacts",
        "bad quality",
        "watermark",
        "unfinished",
        "displeasing",
        "chromatic aberration",
        "signature",
        "extra digits",
        "artistic error",
        "username",
        "scan",
        "[abstract]",
        "bad anatomy",
        "bad hands",
        "@_@",
        "mismatched pupils",
        "heart-shaped pupils",
        "glowing eyes",
    ]
    NONE = []

    def __int__(self):
        match self:
            case UndesiredPreset.HEAVY:
                return 0
            case UndesiredPreset.LIGHT:
                return 1
            case UndesiredPreset.HUMAN:
                return 2
            case _:
                return 3
