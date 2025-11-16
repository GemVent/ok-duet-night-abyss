import time
import numpy as np
import cv2
import winsound
import win32api, win32con

from ok import BaseTask, Box, Logger, PostMessageInteraction

logger = Logger.get_logger(__name__)

class BaseDNATask(BaseTask):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.key_config = self.get_global_config('Game Hotkey Config')  # 游戏热键配置
        self.afk_config = self.get_global_config('挂机设置')
        self.old_mouse_pos = None

    def in_team(self) -> bool:
        if self.find_one('lv_text', threshold=0.8):
            return True
        return False
    
    def find_start_btn(self, threshold: float = 0, box: Box | None = None, template = None) -> Box | None:
        if isinstance(box, Box):
            self.draw_boxes(box.name, box, "blue")
        return self.find_one('start_icon', threshold=threshold, box=box, template=template)
    
    def find_cancel_btn(self, threshold: float = 0, box: Box | None = None, template = None) -> Box | None:
        if isinstance(box, Box):
            self.draw_boxes(box.name, box, "blue")
        return self.find_one('cancel_icon', threshold=threshold, box=box, template=template)
    
    def find_retry_btn(self, threshold: float = 0, box: Box | None = None, template = None) -> Box | None:
        if isinstance(box, Box):
            self.draw_boxes(box.name, box, "blue")
        return self.find_one('retry_icon', threshold=threshold, box=box, template=template)
    
    def find_quit_btn(self, threshold: float = 0, box: Box | None = None, template=None) -> Box | None:
        if isinstance(box, Box):
            self.draw_boxes(box.name, box, "blue")
        return self.find_one('quit_icon', threshold=threshold, box=box, template=template)
    
    def find_drop_item(self, rates = 2000, threshold: float = 0, box: Box | None = None, template = None) -> Box | None:
        if isinstance(box, Box):
            self.draw_boxes(box.name, box, "blue")
        return self.find_one(f'drop_item_{str(rates)}', threshold=threshold, box=box, template=template)

    def safe_get(self, key, default=None):
        if hasattr(self, key):
            return getattr(self, key)
        return default

    def soundBeep(self, _n=None):
        if hasattr(self, "config") and not self.config.get('发出声音提醒', True):
            return
        if _n is None:
            n = self.afk_config['提示音'] if self.afk_config['提示音'] > 0 else 1
        else:
            n = _n
        for _ in range(n):
            winsound.Beep(523, 150)
            self.sleep(0.3)

    def log_info_notify(self, msg):
        self.log_info(msg, notify=self.afk_config['弹出通知'])

    def move_mouse_to_safe_position(self):
        if self.afk_config["防止鼠标干扰"]:
            self.old_mouse_pos = win32api.GetCursorPos()
            abs_pos = self.executor.interaction.capture.get_abs_cords(self.width_of_screen(0.85), self.height_of_screen(0.6))
            win32api.SetCursorPos(abs_pos)
            self.sleep(0.02)

    def move_back_from_safe_position(self):
        if self.afk_config["防止鼠标干扰"] and self.old_mouse_pos is not None:
            self.sleep(0.02)
            win32api.SetCursorPos(self.old_mouse_pos)
            self.old_mouse_pos = None

    def burst_skill_release(self, skill_type="战技", burst_count=3, burst_interval=0.2):
        """
        短时间内连续释放多次技能的通用方法

        Args:
            skill_type (str): 技能类型 - "战技" 或 "终结技"
            burst_count (int): 连续释放次数
            burst_interval (float): 每次释放之间的间隔时间(秒)
        """
        try:
            char = self.get_current_char()
            if not char:
                return

            for i in range(burst_count):
                if skill_type == "战技":
                    char.send_combat_key()
                elif skill_type == "终结技":
                    char.send_ultimate_key()
                else:
                    self.logger.warning(f"不支持的技能类型: {skill_type}")
                    return

                # 如果不是最后一次释放，等待间隔时间
                if i < burst_count - 1:
                    time.sleep(burst_interval)

        except Exception as e:
            self.logger.warning(f"多次技能释放失败: {e}")


lower_white = np.array([244, 244, 244], dtype=np.uint8)
lower_white_none_inclusive = np.array([243, 243, 243], dtype=np.uint8)
upper_white = np.array([255, 255, 255], dtype=np.uint8)
black = np.array([0, 0, 0], dtype=np.uint8)

def isolate_white_text_to_black(cv_image):
    """
    Converts pixels in the near-white range (244-255) to black,
    and all others to white.
    Args:
        cv_image: Input image (NumPy array, BGR).
    Returns:
        Black and white image (NumPy array), where matches are black.
    """
    match_mask = cv2.inRange(cv_image, black, lower_white_none_inclusive)
    output_image = cv2.cvtColor(match_mask, cv2.COLOR_GRAY2BGR)

    return output_image
